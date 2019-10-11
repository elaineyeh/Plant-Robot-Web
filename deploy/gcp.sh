cd ~/Plant-Robot-Web
git pull
cat key.json | gcloud auth activate-service-account --key-file=-
docker login -u oauth2accesstoken -p "$(gcloud auth application-default print-access-token)" https://asia.gcr.io
docker-compose pull && docker-compose up -d --no-deps
