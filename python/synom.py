#!/usr/bin/env python3

def synoms():
    import vim, requests, json, os, builtins
    class mydict(dict):
        pass
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

    def _get_data_from_server(word, what=''):
        headers = {}
        headers['x-rapidapi-host'] = 'wordsapiv1.p.rapidapi.com'
        headers['x-rapidapi-key'] = _get_my_key()
        url = 'https://wordsapiv1.p.rapidapi.com/words/{}/{}'.format(word, what)
        try:
            with requests.request('GET', url, headers=headers) as resp:
                data = resp.text
        except requests.exceptions.RequestException as e:
            print('Synom ERROR: Error occured when retrieving data from Words API server')
            exit()
        obj = json.loads(data)
        return obj 

    def _get_synoms(word):
        obj = _get_data_from_server(word, 'synonyms')
        if obj is not None and isinstance(obj, dict) and 'synonyms' in obj.keys():
            return ', '.join(obj['synonyms'])
        else:
            return '--- No synonyms ---'

    def _get_it_all(word):
        def set_value(d, d2, k, k2):
            if k2 in d2:
                d[k] = d2

        out_list = {}
        obj = _get_data_from_server(word)
        if obj is not None and isinstance(obj, dict) and isinstance(obj['results'], list):

            out_list['word'] = obj['word']      # add searched word
            out_list['meanings'] = []

            for meaning in obj['results']:
                x = {}
                x['def'] = meaning['definition']
                x['s
                out_list['meanings'].append(




        else:
            return '--- Error when parsin response ---'
            

    # print(_get_synoms(_get_current_word()))
    vim.command("set buftype=nofile")
    vim.command("pedit! /tmp/Synom-temp-file")
