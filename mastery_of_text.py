# downloading the text
import urllib.request

url = "https://www.gutenberg.org/cache/epub/10/pg10.txt"

try:
    save_path = "pg10.txt"
    urllib.request.urlretrieve(url, save_path)
    print(f"File successfully downloaded to {save_path}")

    with open(save_path, "r", encoding="utf-8") as f:
        pg10 = f.read()

except Exception as e:
    print(f"An error occurred: {e}")


# counting the number of lines the string has
num_lines = len(pg10.splitlines())
print("Number of lines:", num_lines)


# counting the number of words the string has
import re

words = re.findall(r"[a-zA-Z]+", pg10)
num_words = len(words)
print("Number of words:", num_words)


# counting the number of times the word "apostle" appears (ignoring capitalization)
apostle_count = sum(1 for word in words if word.lower() == "apostle")
print("Occurrences of 'apostle':", apostle_count)


# counting the most common word (ignoring capitalization)
from collections import Counter

word_counts = Counter(word.lower() for word in words)
most_common_word = word_counts.most_common(1)[0][0]
print("Most common word:", most_common_word)