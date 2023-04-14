import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Error: Incorrect number of command line arguments")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read database file into a variable
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        str_sequences = header[1:]
        csv_data = list(csv_reader)

    # Read DNA sequence file into a variable
    with open(dna_filename, 'r') as dna_file:
        dna_sequence = dna_file.read()

    # Find longest match of each STR in DNA sequence
    str_counts = []
    for str_sequence in str_sequences:
        str_count = longest_match(dna_sequence, str_sequence)
        str_counts.append(str_count)

    # Check database for matching profiles
    match = False
    for row in csv_data:
        name = row[0]
        individual_str_counts = [int(count) for count in row[1:]]
        if str_counts == individual_str_counts:
            print(name)
            match = True
            break
    if not match:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    # Return longest run found
    return longest_run


main()
