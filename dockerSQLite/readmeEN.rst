Install PyScada using Docker on Windows
=======================================

1. Download this folder.

2. Launch Docker Desktop.

3. To use under Linux, edit the `docker-compose.yml` in the `dockerSQLITE.zip` file and comment line like this :

   ::

      #- "c:/temp/pyscada_docker:/src/pyscada/shared" # windows
      - "/tmp/pyscada_docker:/src/pyscada/shared" # linux

4. Run

   ::

      docker-compose-full.bat

   and wait until the end.

5. Open the page http://127.0.0.1:8090

6. Connect using :

   ::

      user : pyscada
      password : pyscada

Upgrade or install plugins
==========================

1. Copy zip in :

   ::

      # Windows
      c:\temp\pyscada_docker\plugins
      # Linux
      /tmp/pyscada_docker/plugins

2. Run

   ::

      docker-compose-upgradeZip

Save or restore the database
============================

1. Copy or restore the file :

   ::

      # Windows
      c:\temp\pyscada_docker\sqlite_db\PyScada_db
      # Linux
      /tmp/pyscada_docker/sqlite_db/PyScada_db

