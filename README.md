# UE19 : Labo09-10:
Dans ce labo, nous apprenons à utiliser git et à utiliser docker pour conteneuriser une application faites en python.
- App.py : contient notre application écrite en python, cette application est non imposée tant qu'elle contient une api, j'ai donc fait un bot discord qui fait appel à une api pour convertir une devise dans une autre.
- Dockerfile : le fichier qui permet de créer l'image et de lancer le conteneur de app.py;
- requirements.txt : permet d'installer nos dépendances.
## Installation : 
Cloner le repo : 

`git clone https://github.com/Mogfrat/UE19_LABO09-10.git`

installer les requirements :

`pip install -r requirements.txt`

Build l'image docker :
`docker build -t nom_de_tag`

Lancer le conteneur : 
`docker run -it --rm --name nom_du_conteneur_que_vous_souhaitez`
## Comment utiliser : 
Modifier le token du bot par le votre que vous aurez générer <a href="https://discord.com/developers/applications">ici</a>. Voir la <a href="https://discord.com/developers/docs/getting-started">doc</a>. 

Vous devez créer la commande via leur <a href="https://discord.com/developers/docs/interactions/application-commands#making-a-global-command">api</a>

Connectez vous à discord, ajoutez le bot à un serveur ou lui envoyer la commande par message privé : 

`/convert devise_base devise_destination montant`

ex:
`/convert EUR USD 500`
