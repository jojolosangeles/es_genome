import sys
from time import sleep

# see https://elasticsearch-dsl.readthedocs.io/en/latest/
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

index = sys.argv[1]
file_path = sys.argv[2]
species = sys.argv[3]
chromosome = sys.argv[4]

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

# create the index
class DataSegment(Document):
    raw_data = Text(analyzer='my_analyzer', fields={'raw': Keyword()})
    species = Text(analyzer='keyword')
    chromosome = Text(analyzer='keyword')
    location = Integer()

    class Index:
        name = index
        settings = {
          "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        return super(DataSegment, self).save(** kwargs)

# create the mappings in elasticsearch
#DataSegment.init()

# process each line, load into index
location = 0
ndocs = 0
with open(file_path, "r") as inFile:
    for line in inFile:
        ndocs += 1
        line = line.strip()
        data = DataSegment(raw_data=line, species=species, chromosome=chromosome, location=location)
        data.save()
        print(f"Loaded doc {ndocs} location {location}")
        #sleep(1)
        location += len(line)

print(f"loaded {ndocs} documents, {location} values")