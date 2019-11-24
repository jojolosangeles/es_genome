import click
import string
import random
from string import Template
from test_data.randstr import randomString


@click.command()
@click.option("--analyzer", default="my_analyzer", help="Name of generated analyzer")
@click.option("--template", default="cut_seq_analyzer.template", help="path to input file containing template")
@click.option("--size", default=3, help="Size of random cut-out sequence.")
@click.option("--alpha", default=string.ascii_lowercase,
              help="The alphabet to use when generating cut-out sequence.")
@click.option("--n", default=3, help="Number of entries to create")
@click.option("--seed", default=0, help="Random number generation seed")


def gen_analyzer(analyzer, template, size, alpha, n, seed):
    random.seed(seed)

    def get_analyzer_template(template):
        with open(template, "r") as inFile:
            content = inFile.read()
            return Template(content)

    def generate_cut_sequences(n, size, alpha):
        result = []
        for i in range(n):
            result.append(randomString(size, alpha))
        param = "|".join(result)
        return param

    analyzer_template = get_analyzer_template(template)
    cut_sequences = generate_cut_sequences(n, size, alpha)
    print(analyzer_template.substitute(ANALYZER_NAME=analyzer, CUT_SEQUENCES=cut_sequences))


if __name__ == '__main__':
    gen_analyzer()
