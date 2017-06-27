#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch

# variables
esHost = 'http://localhost:9200' # defineo host do elasticsearch

# principal
es = Elasticsearch([esHost])

#clusterHealth = es.cluster.health()
#print(es.cluster.health())

catAllocation = es.cat.allocation(format='json',v='true')

print('shards: ' + catAllocation[0]['shards'])
print('disco total: ' + catAllocation[0]['disk.total'])
print('disco em uso: ' + catAllocation[0]['disk.used'])
print('indices: ' + catAllocation[0]['disk.indices'])
print('disco livre: ' + catAllocation[0]['disk.avail'])
print('percentual em uso: ' + catAllocation[0]['disk.percent'] + '%')
