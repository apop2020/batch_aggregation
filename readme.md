# Batch data aggregation same
# purpose
To perform simple data aggreation using pyspark, as per document AN-BatchAggregationCodingChallenge-240723-1546-366
* Note: document is deliberatly omitted

## requirements
    docker
    windows

## Architecture Overview
    Program conists of 2 components, a sample data generator (optional), which deposits data in data/in  and a data summarizer which outputs to data/out.   The summeraizer code is conained in main.py, and is meant to be run inside docker. To do so, execute run.bat.
## usage
1. Regenerate data by running populatedata.py  (optional)
1. modify config.env to set the desired time-window for sumarizaation (default is 1 day)
1. run run.bat
1. colect results from data\out
