# CS2FS converter

A small tool to convert **CodeSnippets** exports into **FluentSnippets**-importable JSON.  

## Features

- Detects PHP, PHP+HTML content, CSS, and JS snippets  
- Strips wrapping `<p>` tags from descriptions  
- Preserves source tags, with sensible fallbacks  
- Outputs a ready-to-import `.json` for FluentSnippets (v10.51+)  
- Includes a one-click “Convert & Save” button in Jupyter  

## Installation

1. Clone this repo:  
   ```bash
   git clone https://github.com/FollaKy/CS2FS.git
   cd CS2FS/converter
