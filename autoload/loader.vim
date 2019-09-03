let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
if !has('python3')
    echom 'Synom ERROR: Vim needs to be compiled with +python3, in order for Synom to work.'
endif

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path[0:0] = [python_root_dir]
import synom
EOF

function! loader#Synonyms()
    python3 synom.get_handler().synonyms()
endfunction

function! loader#Definitions()
    python3 synom.get_handler().definitions()
endfunction

