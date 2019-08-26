#!/usr/bin/env python3

def synoms():
    import vim, requests, json, os
    def _get_my_key():
        plugin_root_dir = vim.eval('s:plugin_root_dir')
        file = os.path.normpath(os.path.join(plugin_root_dir, '..', 'data', 'my-key'))
        try:
            with open(file, 'r') as f:
                key = f.read()
        except FileNotFoundError as e:
            print('Synom ERROR: File with API key not found')
            exit()
        return str(key.strip())

    def _get_current_word():
        return vim.eval("expand(\"<cword>\")")

    def _get_synoms(word):
        headers = {}
        headers['x-rapidapi-host'] = 'wordsapiv1.p.rapidapi.com'
        headers['x-rapidapi-key'] = _get_my_key()
        url = 'https://wordsapiv1.p.rapidapi.com/words/{}/synonyms'.format(word)
        try:
            with requests.request('GET', url, headers=headers) as resp:
                data = resp.text
        except requests.exceptions.RequestException as e:
            print('Synom ERROR: Error with retriving data from Words API server')
            exit()
        obj = json.loads(data)
        if obj is not None and isinstance(obj, dict) and 'synonyms' in obj.keys():
            return ', '.join(obj['synonyms'])
        else:
            return '--- No synonyms ---'

    print(_get_synoms(_get_current_word()))
