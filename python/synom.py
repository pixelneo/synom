#!/usr/bin/env python3
import vim
import requests
import json
import os
import builtins

class IAmExiting(Exception):
    pass

class mydict(dict):
    def set_from(self, key, dict2, key2):
        '''
            Sets a value from `dict2[key2]` to `key` if `key2` exists in dict2, otherwise does nothing.
        '''
        if key2 in dict2.keys():
            self[key] = dict2[key2]

    def set_from_string(self, key, dict2, key2):
        '''
            Sets a concatenation of values from `dict2[key2]` to `key` if `key2` exists in dict2, otherwise does nothing.
        '''
        if key2 in dict2.keys():
            self[key] = ', '.join(dict2[key2])

builtins.dict = mydict

def _get_my_key():
    try:
        key = vim.eval('g:words_api')
    except vim.error as e:
        print('Synom ERROR: API key has to be set in g:words_api variable.')
        raise IAmExiting
    return str(key.strip())

def _get_current_word():
    return vim.eval("expand(\"<cword>\")").lower()

class Synom:
    def __init__(self, word):
        self.word = word

    def _get_data_from_server(self,what=''):
        headers = {}
        headers['x-rapidapi-host'] = 'wordsapiv1.p.rapidapi.com'
        headers['x-rapidapi-key'] = _get_my_key()
        url = 'https://wordsapiv1.p.rapidapi.com/words/{}/{}'.format(self.word, what)
        try:
            with requests.request('GET', url, headers=headers) as resp:
                data = resp.text
        except requests.exceptions.RequestException as e:
            print('Synom ERROR: Error occured when retrieving data from Words API server')
            raise IAmExiting
        obj = json.loads(data)
        return obj 

    def get_synoms(self):
        obj = self._get_data_from_server('synonyms')
        try:
            return ', '.join(obj['synonyms'])
        except (TypeError, KeyError) as e:
            return '--- No synonyms ---'

    def get_it_all(self):
        out_list = dict() 
        obj = self._get_data_from_server()
        try:
            out_list['word'] = obj['word']      # add searched word
            out_list['meanings'] = []

            for meaning in obj['results']:
                x = dict() 
                x.set_from('def', meaning, 'definition')
                x.set_from('pos', meaning, 'partOfSpeech')
                x.set_from_string('synonyms', meaning, 'synonyms')
                x.set_from_string('derivation', meaning, 'derivation')
                x.set_from_string('examples', meaning, 'examples')
                out_list['meanings'].append(x)

            t = ['\n'.join(['{}:  {}'.format(k.upper(),v) for k,v in meaning.items()]) for meaning in out_list['meanings']]
            mns = ''.join(['\n',32*'-','\n\n']).join(t)
            result = '{}: {}\n\n{}'.format('Word', out_list['word'], mns)
            return result
        except TypeError as e:
            return '--- Error when parsin response ---'
        except KeyError as e:
            print('--- Word has not been found ---')
            raise IAmExiting

def synonyms():
    try:
        handler = Synom(_get_current_word())
        print(handler.get_synoms())
    except IAmExiting as e:
        pass

def definitions():
    try:
        handler = Synom(_get_current_word())
        with open('/tmp/Synom-temp-file', 'w') as f:
            f.write(handler.get_it_all())
        vim.command("pedit! /tmp/Synom-temp-file")
    except IAmExiting as e:
        pass

