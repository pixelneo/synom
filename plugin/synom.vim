let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import synom
EOF
function! Synonyms()
    python3 synom.get_handler().synonyms()
endfunction

function! Definitions()
    python3 synom.get_handler().definitions()
endfunction

command! -nargs=0 SynomS call Synonyms()
command! -nargs=0 SynomD call Definitions()

