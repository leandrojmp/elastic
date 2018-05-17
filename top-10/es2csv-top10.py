from datetime import datetime
from elasticsearch import Elasticsearch
from sys import argv, exit
from os import remove 

# check the script parameters

if "-c" in argv:
    try:
        if (argv[argv.index("-c") + 1]) is not None:
            columnName = argv[argv.index("-c") + 1]
    except:
        print("Wrong usage: use the option -c <columnName>")
        exit()
else:
    exit()

# esHost is an array with the hosts in the cluster
esHost = ['http://10.111.2.25:9200','http://10.111.2.26:9200','http://10.111.2.27:9200']

es = Elasticsearch(esHost) # create the object es

qry = open("es2csv-top10.qry","r").read() # open and read the file with the query request

result = es.search(index="fw-traffic-*",body=qry) # store the result of the query

totalHits = result['hits']['total'] # get the total hits

# check if the query returned any hit
if totalHits > 0:
    # remove the csv file if it exists
    try: 
        remove('es2csv-top10.csv')
    except OSError:
        pass
    es2csv = open('es2csv-top10.csv','a') # create a file to store the results
    print(columnName + "," + "count",file=es2csv)
    for hit in result['aggregations']['2']['buckets']:
        print(str(hit['key']) + "," + str(hit['doc_count']),file=es2csv)
