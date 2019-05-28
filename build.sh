rm -rf ./docker/context/dockerdist/*
cp -Rf ./geotrouvethon.iml ./docker/context/dockerdist/
cp -Rf ./geotrouvethon.py ./docker/context/dockerdist/
cp -Rf ./entrypoint.sh ./docker/context/dockerdist/
cp -Rf ./requirements.txt ./docker/context/dockerdist/

docker-compose -f ./docker/geotrouvethon.yml build
