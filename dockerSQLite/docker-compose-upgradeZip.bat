docker container stop pyscada nginx
docker container exec pyscada /bin/sh -c "for file in `ls -1 /src/pyscada/shared/plugins/*.zip`; do pip3 install $file; done"
docker container start pyscada nginx
