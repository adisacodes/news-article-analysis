import re
from collections import Counter

with open("News Article for Python Assessment.txt", "r") as file:
    article = file.read()



def count_specific_word(text, word):
    if not text or not word:
        return 0
    else:
        words = re.findall(r'\b\w+\b', text.lower())
        count = 0
        index = 0
        while index < len(words):
            if words[index] == word.lower():
                count += 1
            index += 1
        return count



def identify_most_common_word(text):
    if not text.strip():
        return None
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    if not text.strip():
        return 0
    words = re.findall(r'\b\w+\b', text)
    total_length = 0
    for word in words:
        total_length += len(word)
    if len(words) == 0:
        return 0
    return total_length / len(words)



def count_paragraphs(text):
    if not text.strip():
        return 1
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    if not text.strip():
        return 0
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    return len(sentences)



print("Word count for 'apple':", count_specific_word(article, 'apple'))
print("Most common word:", identify_most_common_word(article))
print("Average word length:", calculate_average_word_length(article))
print("Number of paragraphs:", count_paragraphs(article))
print("Number of sentences:", count_sentences(article))
