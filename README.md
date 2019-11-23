### tokenizers for importing genome data into Elasticsearch

Basic test
```
curl -XPOST 'localhost:9200/_analyze?pretty' -H 'Content-Type: application/json' -d'
{
    "tokenizer": "keyword",
    "char_filter": [ "html_strip" ],
    "text": "<p>I&apos;m so <b>sad</b>!</p"
}'

```

Replace specific patterns with space

### library

Using 6.5 elasticsearch locally

Python libraries major version must match:

pip install elasticsearch==
pip install elasticsearch_dsl==

These show the versions available

(useful when switching to later version)

```pip install -r requirements.txt```

*activate*

```source ~/.virtualenvs/es_genome/bin/activate```

```deactivate```

*hook direnv into bash so that pythonpath set for this project*
This is in .bash_profile
```eval "$(direnv hook bash)"```
