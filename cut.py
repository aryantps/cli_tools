import argparse
import sys

class Cutter:
    """Class to cut out selected portions from each line in a file."""
    
    def __init__(self, delimiter='\t', fields=None, files=None):
        """
        Initialize Cutter object with delimiter, fields and files.

        Parameters:
        delimiter (str): delimiter character to separate fields (default '\t')
        fields (str): field selection string, indicating which fields to select
        files (list of str): list of input files to process
        """
        self.delimiter = delimiter
        self.fields = fields
        self.files = files

    def cut(self):
        """
        Process the input stream by reading line by line and printing the selected fields.

        Returns:
        None
        """
        input_stream = self.read_input(self.files)
        for line in input_stream:
            processed_line = self.process_line(line)
            print(processed_line)

    def process_line(self, line):
        """
        Process a single line of input by splitting it into fields and selecting the specified fields.

        Parameters:
        line (str): input line to process

        Returns:
        str: processed line with selected fields separated by the specified delimiter
        """

        # Split the line into fields using the specified delimiter
        fields = line.strip().split(self.delimiter)

        # Select the fields specified in the field selection
        selected_fields = [fields[i-1] for i in self.parse_field_selection(self.fields)]

        # Join the selected fields back together using the delimiter
        return self.delimiter.join(selected_fields)

    @classmethod
    def parse_field_selection(cls, field_selection):
        """
        Parse the field selection string into a list of selected field indices.

        Parameters:
        field_selection (str): field selection string, indicating which fields to select

        Returns:
        list of int: list of selected field indices
        """
        selected_fields = []
        # Split the field selection into ranges and individual fields
        for field_range in field_selection.split(','):
            # Split each field range into its start and end points
            for field in field_range.split():
                if '-' in field:
                    start, end = field.split('-')
                    # Add a range of fields if a hyphen is present
                    selected_fields += range(int(start), int(end)+1)
                else:
                    # Add a single field if no hyphen is present
                    selected_fields.append(int(field))
        return selected_fields

    @classmethod
    def read_input(cls, files):
        """
        Read the input stream from a list of files.

        Parameters:
        files (list of str): list of input files to read

        Returns:
        file object: input stream as a file object
        """
        # If no input files are specified or a hyphen is present, read from standard input
        if not files or files == ['-']:
            input_stream = sys.stdin
        else:
            # Otherwise, read from the specified files
            input_stream = open(files[0])
            # If multiple files are specified, concatenate them using itertools.chain
            if len(files) > 1:
                for file in files[1:]:
                    input_stream = chain(input_stream, open(file))
        return input_stream


def main():
    parser = argparse.ArgumentParser(description='Cut out selected portions from each line in a file.')
    parser.add_argument('-d', '--delimiter', default='\t', help='use DELIM instead of TAB as the field delimiter character')
    parser.add_argument('-f', '--fields', required=True, help='select only these fields')
    parser.add_argument('files', nargs='*', help='input files')
    args = parser.parse_args()

    cutter = Cutter(delimiter=args.delimiter, fields=args.fields, files=args.files)
    cutter.cut()


if __name__ == '__main__':
    main()