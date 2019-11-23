# see https://pynative.com/python-generate-random-string/
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# see https://elasticsearch-dsl.readthedocs.io/en/latest/
from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class DataSegment(Document):
    raw_data = Text(analyzer='keyword', fields={'raw': Keyword()})
    species = Text(analyzer='keyword')
    chromosome = Text(analyzer='keyword')

    class Index:
        name = 'test_data'
        settings = {
          "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        return super(DataSegment, self).save(** kwargs)


# create the mappings in elasticsearch
DataSegment.init()

# create and save and article
s = randomString(1000)
data = DataSegment(meta={'id': 42}, raw_data=s, species='human', chromosome='2a')
data.save()

article = DataSegment.get(id=42)
print(article.chromosome)

# Display cluster health
print(connections.get_connection().cluster.health())

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

s = Search(using=client, index="test_data") \
    .query("match", species="human")

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.species, hit.chromosome)
