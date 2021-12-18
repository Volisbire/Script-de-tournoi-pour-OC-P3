 Script-de-tournoi-pour-OC-P4
 =============================


Le programme permet de créer et gérer un tournoi d'echec a 8 joueurs.
--------------------------------------------------------------------------


Installation
------------
1. Python3 doit etre installe sur votre systeme : https://www.python.org/

2. L'utilisation d'un environnement virtuel est fortement recommandé:

py -m venv c:\path\to\myenv

3. Pour installer les bibliotheques necessaires:

py -m pip install -r requirements.txt


Utilisation
-----------
* Placez vous dans le dossier ou vous avez clonez ce repository puis éxécutez :
py -m main.py
* Le fichier Main contient un booléen qui genere automatiquement les 8 joueurs si testmode=True
* Pour génerer les 8 joueurs manuellement : testmode=False
