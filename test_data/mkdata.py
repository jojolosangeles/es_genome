import click
import string
import random

@click.command()
@click.option("--data", default="100x10k", help="number of lines, size of each line, e.g. 100x10k or 100kx10k")
@click.option("--cutsize", default=3, help="size of cut section")
@click.option("--ncut", default=3, help="number of cut sections")
@click.option("--alpha", default=string.ascii_lowercase,
              help="The alphabet to use when generating string.")
@click.option("--index", default="acgt_index", help="name of index to load")
@click.option("--seed", default=0, help="Random number generation seed")

def mkdata(data, alpha, seed, cutsize, ncut, index):
    random.seed(seed)

    xp = dict(k=1e3, m=1e6, b=1e9)
    def to_int(s):
        if s[-1] in xp:
            return int(s[0:-1])*int(xp[s[-1]])
        else:
            return int(s)

    def num_and_size(data_spec):
        data = data_spec.split("x")
        n = to_int(data[0])
        size = to_int(data[1])
        return (n, size)

    n, size = num_and_size(data)
    print(f"python ../analyzers/gen_analyzer.py --template ../analyzers/cut_seq_analyzer.template --size {cutsize} --n {ncut} --alpha {alpha} > data/cut_seq.json")
    print(f"python gen_data.py --size {size} --n {n} --alpha {alpha} > data/acgt.txt")
    print(f"curl -XDELETE localhost:9200/{index} | jq .")
    print(f"curl -XPUT localhost:9200/{index} -d @data/cut_seq.json -H 'Content-Type: application/json' | jq '.acknowledged'")
    print(f"sleep 3")
    print(f"python ../es_loader/line_loader.py {index} ./data/acgt.txt sp1 ch1")
    print(f"sleep 3")
    print(f"curl localhost:9200/{index}/_search | jq .")


if __name__ == '__main__':
    mkdata()