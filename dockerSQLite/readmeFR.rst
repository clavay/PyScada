Installer PyScada via Docker sur Windows
========================================

1. Télécharger l’ensemble du dossier.

2. Lancer Docker Desktop.

3. Pour utiliser sous Linux, éditer `docker-compose.yml` dans le fichier `dockerSQLITE.zip` et commenter les lignes ainsi :

   ::

      #- "c:/temp/pyscada_docker:/src/pyscada/shared" # windows
      - "/tmp/pyscada_docker:/src/pyscada/shared" # linux

4. Exécuter

   ::

      docker-compose-full.bat

   et attendre la fin.

5. Aller sur la page http://127.0.0.1:8090

6. Se connecter via:

   ::

      identifiant : pyscada
      mot de passe : pyscada

Mise à jour ou installation de plugins
======================================

1. Mettre les zip dans :

   ::

      # Windows
      c:\temp\pyscada_docker\plugins
      # Linux
      /tmp/pyscada_docker/plugins


2. Exécuter

   ::

      docker-compose-upgradeZip

Sauvegarder et restaurer la base de données
===========================================

1. Copier ou restaurer le fichier :

   ::

      # Windows
      c:\temp\pyscada_docker\sqlite_db\PyScada_db
      # Linux
      /tmp/pyscada_docker/sqlite_db/PyScada_db

