# Synom
A Plugin to Vim which prints definitions, synonyms, part of speech tag, derivations, and examples for the current word in buffer.
Uses [WordsAPI](https://www.wordsapi.com) (there are 2500 free requests a day).

### Work in progress
This is very much work in progress.
Although the plugin works, its commands may change in future versions.

## Instalation
If you use Vundle, add `Plugin 'pixelneo/vim-synonym-lookup'` to your `.vimrc` file.

To make the plugin work, you need an API key for WordsAPI. 
Add this line to your `.vimrc` file:

~~~
let g:words_api = '<your-api-key>'`
~~~

For example: `let g:words_api = 'n58234s43gmshd2ef5sa54fh0421p1784d1psqd25efza4f890'`.

## Usage
The plugin uses several commands:

| Command | Description |
|---------|-------------|
| SynomD | Display all information about the current word in the preview window |
| SynomS | Print all synonyms for the current word |

