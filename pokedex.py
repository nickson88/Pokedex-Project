# import json
# ## Open the JSON file of pokemon data
# pokedex = open("./pokedex.json", encoding="utf8")
# ## create variable "data" that represents the enitre pokedex list
# data = json.load(pokedex)
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def language():
    ask = input("What language would you like? 1 English, 2 Japanese, 3 Chinese, 4 French")
    for pokemon in data:
        if ask == "1":
            print(pokemon["name"]["english"])
        elif ask == "2":
            print(pokemon["name"]["japanese"])   
        elif ask == "3":
            print(pokemon["name"]["chinese"])
        elif ask == "4":
            print(pokemon["name"]["french"]) 
language()
def type():
    ask = input("What pokemon type are you looking for?")
    found = False
    for pokemon in data:
        if ask in [pokemon_type.lower() for pokemon_type in pokemon["type"]]:
            print(pokemon["name"]["english"])
            found = True
    if not found:
        print(f"There is no valid {ask} type")
type()
def search():
    ask = input("What specific pokemon are you looking for?")
    found = False
    for pokemon in data:
        if ask in [pokemon_name.lower() for pokemon_name in pokemon["name"]]:
            print(pokemon["name"]["english"])
            found = True
        if not found:
            print(f"There is no {ask} you searched for.")
search()