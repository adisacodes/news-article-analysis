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
        print(count)
        return count


def identify_most_common_word(text):
    if not text.strip():
        print(None)
        return None
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        print(None)
        return None
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0][0]
    print(most_common)
    return most_common



def calculate_average_word_length(text):
    if not text.strip():
        print(0)
        return 0
    words = re.findall(r'\b\w+\b', text)
    total_length = 0
    for word in words:
        total_length += len(word)
    if len(words) == 0:
        print(0)
        return 0
    average = total_length / len(words)
    print(average)
    return average


def count_paragraphs(text):
    if not text.strip():
        print(1)
        return 1
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    count = len(paragraphs)
    print(count)
    return count


def count_sentences(text):
    if not text.strip():
        print(0)
        return 0
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    count = len(sentences)
    print(count)
    return count


count_specific_word(article, 'apple')
identify_most_common_word(article)
calculate_average_word_length(article)
count_paragraphs(article)
count_sentences(article)
