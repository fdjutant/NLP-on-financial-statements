"""Count words."""
import string
import re

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # TODO: Convert to lowercase
    text = text.lower()
    
    # TODO: Split text into tokens (words), leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    no_punct = text.translate(str.maketrans('', '', string.punctuation))
    no_special = re.sub(r'[^a-zA-Z0-9\s]', '', no_punct)
    words = no_special.split()
    
    # TODO: Aggregate word counts using a dictionary
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    # print(counts)

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
