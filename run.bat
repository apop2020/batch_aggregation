IF EXIST data\out RMDIR /S /Q data\out
docker build -t batch_aggregation .
docker rm -f batch_aggregation_runner || true
docker run --name batch_aggregation_runner --env-file config.env batch_aggregation 
docker cp -q batch_aggregation_runner:/data/out data
docker rm -f batch_aggregation_runner || true

