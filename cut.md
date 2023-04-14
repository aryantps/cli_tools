### DESCRIPTION

`cut.py` is a Python script that emulates the functionality of the UNIX `cut` command. It reads from one or more input files and extracts selected fields from each line, according to user-specified criteria.

The script provides the following options:

- `-d DELIM`, `--delimiter DELIM`: use `DELIM` instead of TAB as the field delimiter character.
- `-f FIELDS`, `--fields FIELDS`: select only these fields.
- `FILES`: one or more input files to process. If not provided, reads from standard input.

### OPTIONS

`-d DELIM`, `--delimiter DELIM` : Use `DELIM` instead of TAB as the field delimiter character.

`-f FIELDS`, `--fields FIELDS` : Select only the specified fields. `FIELDS` is a comma-separated list of field ranges, where each range is either a field number or a range of field numbers specified in the form `m-n`.

### How to Use the "cut.py" Script

To use the "cut.py" script, follow these steps:

1. Navigate to the directory where the cut.py file is saved.
2. Run the script using the following command:

`python cut.py [OPTIONS] [FILES]`

The [OPTIONS] correspond to the command line options you want to pass to the cut command (e.g. -f 1,2), and the [FILES] correspond to the input files you want to process.

### USAGE

Here are some examples of how to use the cut.py script:

#### Example 1

Print out the second field (-f2) from each line in the sample.tsv file:

`python cut.py -f 2 sample.tsv`

#### Example 2

Print out the first field (-f1) from each line in the fourchords.csv file, using a comma as the delimiter:

`python cut.py -f 1 -d , fourchords.csv`

#### Example 3

Print out the first and second fields (-f1,2) from each line in the sample.tsv file:

`python cut.py -f 1,2 sample.tsv`

#### Example 4

Read the last 5 lines from the fourchords.csv file, and print out the first two fields (-f1,2), using a comma as the delimiter:

`tail -n 5 fourchords.csv | python cut.py -f 1,2 -d ,`
