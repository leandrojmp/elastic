# es2csv-top10.py

## description

This is a simple Python script that makes a top 10 query in elasticsearch and save the result as a csv file.

## query

The query has a simple key-value filter and aggregate the count using another field, the range is the last 24 hours.

The example below runs a query filtering by a field named `status` with the value `NEW` and aggregate the results with the count of the field `store`

```
 { "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "analyze_wildcard": true,
            "query": "status:NEW"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-24h",
              "format": "epoch_millis"
            }
          }
        }
      ],
      "must_not": []
    }
  },
  "size": 0,
  "_source": {
    "excludes": []
  },
  "aggs": {
    "2": {
      "terms": {
        "field": "stores",
        "size": 10,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}
```

## usage

```
python3 es2csv-top10.py -c columnName
```

You need to pass the name of the column you want as the first field in the .csv file.

For example, using the command `python3 es2csv-top10.py -c src_ip`, the header output will be `src_ip,count`

```
src_ip,count
1.1.1.1,1981281
8.8.8.8,787321
```

