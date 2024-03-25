tar -xf dockerSQLITE.zip
call docker-compose-load.bat
cd dockerSQLITE
call docker-compose-up.bat
copy pyscada\PyScada_db C:\Temp\pyscada_docker\sqlite_db
cd ..