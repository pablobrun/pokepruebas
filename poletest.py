import unittest
import requests
import json
from getData import getData
#este texto es para la rama de desarrollo


class pokemonTest(unittest.TestCase):

    def test_search_valid_pokemon(self):
        my_data = getData()
        pokemon = my_data.get('kakuna')
        my_pokemon = pokemon.json()
        with open('kakuna.json') as kakuna:
            data = json.load(kakuna)

        self.assertEqual(data['weight'], my_pokemon['weight'])

        for i in my_pokemon['moves']:
            #print(i['move']['name'])
            self.assertTrue(i['move']['name'] in data['moves'])

    def test_search_pokemon_by_number(self):
        my_data = getData()
        pokemon = my_data.get('1')
        my_pokemon = pokemon.json()
        self.assertEqual(200, pokemon.status_code)
        #self.assertEqual(my_pokemon['name'], 'bulbasaur')