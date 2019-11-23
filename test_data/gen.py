import click
import string
import random
from test_data.randstr import randomString

@click.command()
@click.option("--size", default=10, help="Size of random string.")
@click.option("--alpha", default=string.ascii_lowercase,
              help="The alphabet to use when generating string.")
@click.option("--n", default=3, help="Number of entries to create")
@click.option("--seed", default=0, help="Random number generation seed")

def gen_data(size, alpha, n, seed):
    random.seed(seed)
    for i in range(n):
        print(randomString(size, alpha))

if __name__ == '__main__':
    gen_data()