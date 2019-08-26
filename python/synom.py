#!/usr/bin/env python3
import vim, requests, json, os

def _get_my_key():
    plugin_root_dir = vim.eval('s:plugin_root_dir')
    file = os.path.normpath(os.path.join(plugin_root_dir, '..', 'data', 'my-key'))
    with open(file, 'r') as f:
        key = f.read()
    return str(key.strip())

def _get_current_word():
    return vim.eval("expand(\"<cword>\")")

def _get_synoms(word):
    headers = {}
    headers['x-rapidapi-host'] = 'wordsapiv1.p.rapidapi.com'
    headers['x-rapidapi-key'] = _get_my_key()
    url = 'https://wordsapiv1.p.rapidapi.com/words/{}/synonyms'.format(word)
    with requests.request('GET', url, headers=headers) as resp:
        data = resp.text
    obj = json.loads(data)
    return ', '.join(obj['synonyms'])

def synoms():
    print(_get_synoms(_get_current_word()))
