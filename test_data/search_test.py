import click
import random
import string
from random import randint
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

@click.command()
@click.option("--file", default="./data/acgt.txt", help="path to data file with raw data lines")
@click.option("--index", default="acgt_index", help="name of index to search")
@click.option("--seed", default=0, help="Random number generation seed")
@click.option("--fuzz", default=0, help="number of values to randomly change")
@click.option("--alpha", default=string.ascii_lowercase,
              help="The alphabet to use when generating string.")

def search_test(file, index, seed, fuzz, alpha):
    random.seed(seed)

    # this is the data in the index
    data_lines = []
    with open(file, "r") as inFile:
        data_lines = inFile.readlines()
    number_lines = len(data_lines)
    line_len = len(data_lines[0].strip())

    # pick a line at random
    random_line_offset = randint(0, number_lines-1)
    expected_location = random_line_offset*line_len
    print(random_line_offset, expected_location)
    random_line = data_lines[random_line_offset].strip()
    if (fuzz > 0):
        sarray = list(random_line)
        for i in range(fuzz):
            fuzz_offset = randint(0, line_len-1)
            sarray[fuzz_offset] = random.choice(alpha)
        random_line = "".join(sarray)
    random_offset = randint(0, line_len-1100)
    data = random_line[random_offset:random_offset+1000]

    # prepare to search
    client = Elasticsearch()
    searcher = Search(index=index)[0:1].using(client).query("match", raw_data=data)
    response = searcher.execute()
    for hit in searcher:
        print(f"expected location {expected_location}, actual location {hit.location}, score {hit.meta.score}")


if __name__ == '__main__':
    search_test()