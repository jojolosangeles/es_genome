### Searching genome data with Elasticsearch

DNA in all life forms has a couple of cool properties:

1. All life forms have the same ancestor
2. DNA changes very slowly

This means that it's when searching for a specific DNA sequence it will be found in multiple
species, usually the best match being with closely related species.

### Searching with Elasticsearch

Elasticsearch has a few properties that make it good for searching genome data.  Even though it is 
designed for searching text, the tools are not in any way limited to human language text.  It's 
really more accurate to say that it searches for sequences in text.

### How to search a genome

By "search a genome" I mean given some random long DNA sequence, we search for that sequence in
a database of genomes, and return which species/chromosomes match.  It *sounds* like this might
involve some super powers, but if it does, Elasticsearch has those powers.

Here's how it is done here:

### Custom Tokenizer

Since DNA between species changes slowly, the first step is to toss out a lot of the data.  It's
not actually tossed out, it's in Elasticsearch, but as far as how it is searched, we get rid of much
of it.

So here's a sequence:

```
TAGCTTAATGGTATCACATTGACAAACACGGCATTAAGTAGCGACGAAACGGGATTTGCCTGACCGGGGAGAAGCCGGTCGATCAG
```

Suppose I just toss out some pieces of it, like GT/TA/GG.

Elasticsearch will do that for me, and I'll get this:

``` 
--GCT--ATG--ATCACATTGACAAACAC--CAT--A--AGCGACGAAAC--GATTTGCCTGACC----AGAAGCCG--CGATCAG
```

Then let's say these are "words", but I don't want any words shorter than 8 characters.

Elasticsearch will do that too:


``` 
------------ATCACATTGACAAACAC----------AGCGACGAAAC--GATTTGCCTGACC----AGAAGCCG----------
```

This is a custom analyzer.

When you search for a sequence, it goes through the same analyzer.  So it isn't
actually searching for that whole sequence.  But it doesn't matter, 
because *DNA changes very slowly*.

### Not much code

At a high level, here's what the code does:

1. break up long sequence into segments
2. store each segment in Elasticsearch

After that, search just does what it does.

### Some subtle things about DNA

DNA is actually two sequences, so when searching or putting data into 
Elasticsearch, you really don't know which "direction" of the sequence
you are getting.

This just means the search actually needs to be two searches, one for one
direction, the second for the opposite direction.

### What about losing data at boundaries

*DNA changes very slowly*

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

### test data

```python test_data/gen.py --help```


