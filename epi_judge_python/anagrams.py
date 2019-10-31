from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    # Time complexity : O(n m log m) where n is number of strings and m is the max length of a string
    # space complexity : O(n m)
    sorted_dict = {}
    for string in dictionary:
        sorted_key = ''.join(sorted(string))
        if sorted_key in sorted_dict:
            sorted_dict[sorted_key] += [string]
        else:
            sorted_dict[sorted_key] = [string]

    return [group for group in sorted_dict.values() if len(group) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
