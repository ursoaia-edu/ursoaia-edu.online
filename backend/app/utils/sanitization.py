import bleach
from typing import Dict, List, Any

ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 's', 'h1', 'h2', 'h3',
    'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'a', 'img', 'blockquote',
    'pre', 'code', 'div', 'span', 'table', 'thead', 'tbody', 'tr', 'th', 'td'
]

ALLOWED_ATTRS: Dict[str, List[str]] = {
    'a': ['href', 'title', 'target', 'rel'],
    'img': ['src', 'alt', 'width', 'height'],
    'div': ['class', 'data-type', 'data-*'],
    'span': ['class', 'style'],
    'table': ['class'],
    'td': ['colspan', 'rowspan'],
    'th': ['colspan', 'rowspan'],
}


def sanitize_html(content: str) -> str:
    return bleach.clean(content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)


def sanitize_tiptap_content(content: Dict[str, Any]) -> Dict[str, Any]:
    if not content or 'type' not in content:
        return content
    
    def sanitize_node(node: Dict[str, Any]) -> Dict[str, Any]:
        if node.get('type') == 'text' and 'text' in node:
            node['text'] = bleach.clean(node['text'], tags=[], strip=True)
        elif 'content' in node and isinstance(node['content'], list):
            node['content'] = [sanitize_node(child) for child in node['content']]
        elif 'marks' in node and isinstance(node['marks'], list):
            for mark in node['marks']:
                if mark.get('type') == 'link' and 'attrs' in mark:
                    href = mark['attrs'].get('href', '')
                    if not href.startswith(('http://', 'https://', '/', 'mailto:')):
                        mark['attrs']['href'] = '#'
        return node
    
    return sanitize_node(content)