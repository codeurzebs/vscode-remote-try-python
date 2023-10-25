#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")
# write a function that chooses randomly between three options: rock, paper or scissors
import random
def choix_ordinateur():
    choix = random.randint(1,3)
    if choix == 1:
        choix = "pierre"
    elif choix == 2:
        choix = "feuille"
    else:
        choix = "ciseaux"
    return choix

rejouer = 1

while rejouer == 1:
    # The player can choose one of three options: rock, paper or scissors.
    choix = input("Choisissez entre pierre, feuille ou ciseaux : ")
    print("Vous avez choisi : ", choix)
    # The computer chooses one of three options: rock, paper or scissors.
    choix_ordi = choix_ordinateur()
    print("L'ordinateur a choisi : ", choix_ordi)
    # The winner is chosen according to the following rules:
    # rock beats scissors
    # scissors beats paper
    # paper beats rock
    if choix == choix_ordi:
        print("Egalité")
    elif choix == "pierre" and choix_ordi == "ciseaux":
        print("Vous avez gagné")
    elif choix == "feuille" and choix_ordi == "pierre":
        print("Vous avez gagné")
    elif choix == "ciseaux" and choix_ordi == "feuille":
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")
    # The game is played again until the player decides to stop.
    rejouer = int(input("Voulez-vous rejouer ? 1 pour oui, 0 pour non : "))

print("Fin du jeu Merci d'avoir joué au jeu de CodeurZEBS")


