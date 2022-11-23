# RB_LG_Database_project3
Création d'une base de données et de son API

Le but de ce projet est de peupler une base de données et de la requêter via une API. Afin de créer cette base de données, nous avons décidé de mettre en place une base de données relationnelle en utilisant les données de Netflix, téléchargées sur Kaggle.

    Etapes:
        1) my_db.py:
            - Le fichier my_db.py permet de créer une base de données "my_dabase.db".
            - Une fois notre base de données créée, on va créer un tableau qui va contenir notre dataset Netflix. Ainsi, notre base de donnés est prête à être requêté.

        2) db_api.py:
            - Le fichier db_api.py est l'API, elle contient 5 chemins.
            - /update/insert: permet d'insérer un tuple d'élément dans la base de données.
            - /update/delete: permet de supprimer un tuple d'élément de la base de données.
            - /display/type: permet d'afficher le type.
            - /display/title: permet d'afficher le titre.
            - /display/title/country: permet d'afficher les titres groupés par pays.

        3) Lancer l'API
            a) Si on veut lancer l'api seule, il est possible de lancer la commande suivante: docker image build . -t db_api:1.0.1
                - Cette commande va créer l'image de notre API à partir de notre Dockerfile.
                - On pourra donc lancer la commande suivante afin de lancer notre API: • docker container run -it db_api:1.0.1
            b) Pour lancer l'API avec docker-compose, on utilise notre fichier setup.sh:
                - On exécute la commande suivante: bash setup.sh

