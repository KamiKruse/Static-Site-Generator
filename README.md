# Static Site Generator

A Python-based basic static site generator that converts Markdown files to styled HTML pages.

## Features

- Converts Markdown files to styled HTML pages
- Supports common Markdown syntax:
  - Headers (h1-h6)
  - Bold and italic text
  - Code blocks and inline code
  - Ordered and unordered lists
  - Blockquotes
  - Images and links
- Recursive directory processing
- Unit testing coverage

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KamiKruse/Static-Site-Generator
    cd Static-Site-Generator
    ```

## Usage

1. Place your Markdown content files in the `content` directory
2. Run the generator by running
    ```bash
    ./main.sh
    ```
3. Visit `http://localhost:8888` in your browser


## Testing

 1. Run the test suite:
    ```bash
    ./test.sh
    ```
2. The test suite includes unit tests for:
  - Markdown block splitting
  - Delimiter processing
  - Image and link parsing
  - Text node conversion
  - HTML node generation
  - Markdown extraction


## Markdown Support

### Supported Syntax

- Headers: `# H1` through `###### H6`
- Bold: `**bold text**`
- Italic: `*italic text*`
- Code blocks: 
  ````
  ```
  code block
  ```
  ````
- Inline code: `` `inline code` ``
- Lists:
  - Ordered: `1. First item`
  - Unordered: `- Item` or `* Item`
- Blockquotes: `> quote`
- Links: `[text](url)`
- Images: `![alt text](image-url)`

