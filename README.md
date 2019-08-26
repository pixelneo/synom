# Synom
A Plugin to ViM which prints synonyms for the current word in buffer.
Uses [WordsAPI]("https://www.wordsapi.com") (there are 2500 free requests)

## Instalation
If you use Vundle, add `Plugin 'pixelneo/synom'` to your `.vimrc` file.

To make the plugin work, you need an API key for WordsAPI. 
Add that to `.vimrc/bundle/synom/data/my-key` (e.g. `n58234s43gmshd2ef5sa54fh0421p1784d1psqd25efza4f890`)

## Usage
In Vim, write `:Syn` in normal mode to find the synonyms.
