# mobile network client

докер:
`docker build --tag=mariamsu/asvk_client:latest --tag=mariamsu/asvk_client:2 . .` - сбилдить
`docker run  --rm --net=host  -e HOST="0.0.0.0" -e PORT=5019 -it mariamsu/asvk_client` - запустить