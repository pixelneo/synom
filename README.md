# Synom
A Plugin to Vim which prints synonyms or definition, POS etc. for the current word in buffer.
Uses [WordsAPI](https://www.wordsapi.com) (there are 2500 free requests a day).

### Work in progress
This is very much work in progress.
Although the plugin works, its commands may change in future versions.

## Instalation
If you use Vundle, add `Plugin 'pixelneo/synom'` to your `.vimrc` file.

To make the plugin work, you need an API key for WordsAPI. 
Add this line to your `.vimrc` file:

~~~
let g:words\_api = '<your-api-key>'`
~~~

For example: `let g:words\_api = 'n58234s43gmshd2ef5sa54fh0421p1784d1psqd25efza4f890'`

## Usage
In Vim, write `SynomD` to get information about the current word (definition of all meanings, derivation, ...) in the preview buffer.

Write `:SynomS` to find the synonyms and print them.
<!--![usage](https://media.giphy.com/media/SsfjIS3pcY8aP2TkEy/giphy.gif)-->
