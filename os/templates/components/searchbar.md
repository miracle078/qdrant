# SearchBar Component
**UUID:** 2b8f4e9a-5c7d-4f3e-8a6c-9d5f2e7a3b1c

Search input with button.

```javascript
TemplateEngine.registerComponent('SearchBar', comp => {
  const props = comp.props || {};
  const placeholder = props.placeholder || 'Search...';
  const button = props.button || 'Search';
  const action = props.action || 'handleSearch';

  return `
<div class="search-bar">
  <input
    type="text"
    placeholder="${placeholder}"
    class="search-input"
    id="search-input"
  />
  <button onclick="${action}()" class="search-button">
    ${button}
  </button>
</div>
  `.trim();
});
```

## Usage

```markdown
## SearchBar
placeholder: "Search across modalities..."
button: "Search"
action: "HybridSearch.search"
```
