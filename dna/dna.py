import csv
import sys


def main():

    # check for if we get 2 command-line arguments
    if len(sys.argv) != 3:
        print("usage: dna.py __.csv __.txt")
        return 1

    # open a database of people with their sequences
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        database = list(reader) # list of dictionaries

    # open a text file with a particular sequence
    with open(sys.argv[2], "r") as file:
        sequence = file.read()

    # get all the possible sequences that can be checked
    sequences = set()
    for seq in database:
        sequences.update(seq.keys())
        sequences.remove("name")

    # look for the longest match of each sequence that can be checked
    person = dict()
    for subsequence in sequences:
        person[subsequence] = longest_match(sequence, subsequence)

    # check database for matching profiles
    counter = 0
    for item in database:
        for seq in sequences:

            if int(person[seq]) == int(item[seq]):
                counter += 1

            if counter == len(person):
                print(item['name'])
                return

        counter = 0

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
