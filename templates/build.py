#!/usr/bin/env python3
"""
Template Builder
UUID: 5f8e2a9c-3d7b-4f1e-9a6c-8d5f7e2b3a1c

Builds HTML files from markdown templates, inspired by Ignition Perspective.

Usage:
    python templates/build.py                    # Build all templates
    python templates/build.py dashboard          # Build specific template
    python templates/build.py --watch            # Watch mode
"""

import re
import sys
from pathlib import Path


def parse_frontmatter(markdown):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\n(.*?)\n---', markdown, re.DOTALL)
    if not match:
        return {}, markdown

    meta = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            meta[key.strip()] = value.strip()

    content = markdown[match.end():].strip()
    return meta, content


def parse_components(markdown):
    """Extract component blocks from markdown."""
    components = []
    pattern = r'##\s+(\w+)\s*\n(.*?)(?=\n##\s+\w+|\Z)'

    for match in re.finditer(pattern, markdown, re.DOTALL):
        comp_type = match.group(1)
        comp_content = match.group(2).strip()
        components.append({
            'type': comp_type,
            'content': comp_content
        })

    return components


def render_component(component):
    """Render a component to HTML."""
    comp_type = component['type']
    content = component['content']

    # Simple component rendering (can be extended)
    renderers = {
        'Header': lambda c: f'<header><h1>{c}</h1></header>',
        'Footer': lambda c: f'<footer>{c}</footer>',
        'Container': lambda c: f'<div class="container">{c}</div>',
        'Button': lambda c: f'<button>{c}</button>',
        'BootScreen': lambda c: f'<div class="boot-screen"><pre>{c}</pre></div>',
    }

    renderer = renderers.get(comp_type, lambda c: f'<div class="{comp_type.lower()}">{c}</div>')
    return renderer(content)


def build_html(template_path, output_path=None):
    """Build HTML from template."""
    markdown = template_path.read_text()
    meta, content = parse_frontmatter(markdown)
    components = parse_components(content)

    title = meta.get('title', 'Chazon')
    modules = meta.get('modules', '[]')

    # Build HTML
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        f'  <meta charset="UTF-8">',
        f'  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'  <title>{title}</title>',
        f'  <script src="modules/template-engine.md"></script>',
        '</head>',
        '<body>',
    ]

    # Render components
    for comp in components:
        html_parts.append(render_component(comp))

    html_parts.extend([
        '</body>',
        '</html>'
    ])

    html = '\n'.join(html_parts)

    # Write output
    if output_path:
        output_path.write_text(html)
        print(f'Built: {output_path}')
    else:
        print(html)

    return html


def main():
    """Main entry point."""
    templates_dir = Path(__file__).parent / 'views'
    output_dir = Path(__file__).parent.parent

    if len(sys.argv) > 1 and sys.argv[1] != '--watch':
        # Build specific template
        name = sys.argv[1]
        template_path = templates_dir / f'{name}.md'
        output_path = output_dir / f'{name}.html'
        build_html(template_path, output_path)
    else:
        # Build all templates
        for template_path in templates_dir.glob('*.md'):
            output_path = output_dir / f'{template_path.stem}.html'
            build_html(template_path, output_path)


if __name__ == '__main__':
    main()
