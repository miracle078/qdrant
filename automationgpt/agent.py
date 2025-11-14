"""
AutomationGPT Agent - RAG pipeline with Claude
ISA-95/88/18.2 expert system
"""

import os
import time
import logging
from typing import List, Dict, Any, Optional
import anthropic

from .auto_array import AutoArray, get_auto_array

logger = logging.getLogger(__name__)


class AutomationGPT:
    """
    RAG-based agent for ISA standards expertise
    """

    def __init__(self, auto_array: Optional[AutoArray] = None):
        """
        Initialize AutomationGPT agent

        Args:
            auto_array: AutoArray instance for search
        """
        self.array = auto_array or get_auto_array()
        self.memory = []  # Conversation history
        self.system_prompt = """You are AutomationGPT, an expert in industrial automation standards.

You specialize in:
- ISA-95: Enterprise-Control System Integration (Levels 0-4)
- ISA-88: Batch Control (Equipment, Procedures, Recipes)
- ISA-18.2: Alarm Management and Rationalization

When answering:
1. Use the provided CONTEXT from retrieved documents
2. Cite sources with [standard:section] format
3. Provide practical examples when relevant
4. Explain complex concepts clearly
5. If context is insufficient, acknowledge limitations

You have access to:
- ISA standard documents and specifications
- PLC code examples (Ladder Logic, Structured Text, SCL)
- Process diagrams (P&ID, HMI screens, control loops)
- Educational audio content (ISA songs and explanations)
- Training videos and documentation"""

        # Initialize Anthropic client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            logger.warning("ANTHROPIC_API_KEY not set - LLM features disabled")
            self.client = None
        else:
            self.client = anthropic.Anthropic(api_key=api_key)
            logger.info("AutomationGPT initialized with Claude")

    async def query(
        self,
        question: str,
        mode: str = 'hybrid',
        max_context: int = 5,
        include_memory: bool = True
    ) -> Dict[str, Any]:
        """
        Answer question using RAG pipeline

        Args:
            question: User question
            mode: Search mode ('hybrid', 't', 'c', 'i', 'a')
            max_context: Maximum context documents
            include_memory: Include conversation history

        Returns:
            Response with answer, sources, and metadata
        """
        start_time = time.time()

        # 1. RETRIEVE relevant context
        if mode == 'hybrid':
            context_results = await self.array.hybrid_search(question, k_per_mode=2)
        else:
            search_results = await self.array.search(question, mode=mode, k=max_context)
            context_results = [
                {
                    'id': r.id,
                    'score': r.score,
                    'payload': r.payload
                }
                for r in search_results
            ]

        # 2. FORMAT context
        context_str = self._format_context(context_results[:max_context])

        # 3. BUILD prompt
        prompt = self._build_prompt(question, context_str, include_memory)

        # 4. GENERATE answer
        if self.client:
            answer = await self._generate_answer(prompt)
        else:
            answer = self._fallback_answer(context_results)

        # 5. UPDATE memory
        memory_entry = {
            'question': question,
            'answer': answer,
            'context': context_results[:3],
            'timestamp': time.time(),
            'mode': mode
        }
        self.memory.append(memory_entry)

        # Keep last 20 interactions
        if len(self.memory) > 20:
            self.memory = self.memory[-20:]

        retrieval_time = time.time() - start_time

        return {
            'answer': answer,
            'sources': context_results[:max_context],
            'mode': mode,
            'retrieval_time': retrieval_time,
            'context_count': len(context_results)
        }

    def _format_context(self, results: List[Dict[str, Any]]) -> str:
        """Format search results as context"""
        if not results:
            return "No relevant context found."

        context_parts = []
        for i, result in enumerate(results, 1):
            payload = result['payload']

            # Extract relevant fields based on what's available
            if 'std' in payload:
                # ISA standard
                std = payload.get('std', '?')
                sec = payload.get('sec', '?')
                txt = payload.get('txt', '')
                context_parts.append(f"[{std}:{sec}] {txt[:300]}")

            elif 'code' in payload:
                # Code snippet
                lang = payload.get('lang', '?')
                fn = payload.get('fn', '?')
                code = payload.get('code', '')
                context_parts.append(f"[CODE:{lang}/{fn}]\n{code[:200]}")

            elif 'desc' in payload:
                # Image/diagram
                desc = payload.get('desc', '')
                img_type = payload.get('type', '?')
                context_parts.append(f"[DIAGRAM:{img_type}] {desc}")

            elif 'title' in payload:
                # Audio/video
                title = payload.get('title', '?')
                lyr = payload.get('lyr', payload.get('trans', ''))
                ts = payload.get('ts', 0)
                context_parts.append(f"[AUDIO:{title}@{ts}s] {lyr[:200]}")

            else:
                # Generic
                txt = payload.get('txt', str(payload))
                context_parts.append(f"[DOC] {txt[:300]}")

        return "\n\n".join(context_parts)

    def _build_prompt(
        self,
        question: str,
        context: str,
        include_memory: bool
    ) -> str:
        """Build complete prompt for LLM"""
        parts = [self.system_prompt]

        # Add relevant memory if enabled
        if include_memory and self.memory:
            recent = self.memory[-3:]
            memory_str = "\n".join([
                f"Q: {m['question']}\nA: {m['answer'][:100]}..."
                for m in recent
            ])
            parts.append(f"\n\nRECENT CONVERSATION:\n{memory_str}")

        # Add context
        parts.append(f"\n\nCONTEXT:\n{context}")

        # Add question
        parts.append(f"\n\nQUESTION: {question}\n\nANSWER:")

        return "\n".join(parts)

    async def _generate_answer(self, prompt: str) -> str:
        """Generate answer using Claude"""
        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text

        except Exception as e:
            logger.error(f"Claude API error: {e}")
            return f"Error generating response: {str(e)}"

    def _fallback_answer(self, context_results: List[Dict]) -> str:
        """Fallback answer when Claude is unavailable"""
        if not context_results:
            return "No relevant information found."

        # Return top context as answer
        top = context_results[0]['payload']
        return f"Based on available context: {str(top)[:500]}..."

    def clear_memory(self):
        """Clear conversation memory"""
        self.memory = []
        logger.info("Memory cleared")

    def get_stats(self) -> Dict[str, Any]:
        """Get agent statistics"""
        return {
            'memory_entries': len(self.memory),
            'total_queries': len(self.memory),
            'collections': self.array.qdrant.get_collection_stats()
        }


# Singleton
_agent = None


def get_agent() -> AutomationGPT:
    """Get or create AutomationGPT singleton"""
    global _agent
    if _agent is None:
        _agent = AutomationGPT()
    return _agent
