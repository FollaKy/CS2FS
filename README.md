# CS2FS converter

A small tool to convert **CodeSnippets** exports into **FluentSnippets**-importable JSON.  

## Features

- Detects PHP, PHP+HTML content, CSS, and JS snippets  
- Strips wrapping `<p>` tags from descriptions  
- Preserves source tags, with sensible fallbacks  
- Outputs a ready-to-import `.json` for FluentSnippets (v10.51+)  
- Includes a one-click “Convert & Save” button in Jupyter  

## Usage

Jupyter Notebooks:
- download CodeSnippets2FluentSnippets.ipynb locally
- open with Jupyter Notebooks
- run the cell
- click on Upload File and select your CodeSnippets json export
- change the output file if needed
- click on Convert & Save
- a json file compatible with FluentSnippets is saved in the same directory as the source file
- import into FluentSnippets

Python script:
- download CodeSnippets2FluentSnippets.py locally
- rename (a shorter name might be conveninent)
- run 

   python CodeSnippets2FluentSnippets.py input.json output.json

- replace input and output with the appropriate file names.