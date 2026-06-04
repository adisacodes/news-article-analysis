import re
from collections import Counter

with open("News Article for Python Assessment.txt", "r") as file:
    article = file.read()


def count_specific_word(text, word):
    if not text or not word:
        return 0
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())


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
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
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


print("=" * 50)
print(" NEWS ARTICLE TEXT ANALYSIS RESULTS")
print("=" * 50)
print(f"\nWord count for 'apple': {count_specific_word(article, 'apple')}")
print(f"Most common word: '{identify_most_common_word(article)}'")
print(f"Average word length: {calculate_average_word_length(article):.2f} characters")
print(f"Number of paragraphs: {count_paragraphs(article)}")
print(f"Number of sentences: {count_sentences(article)}")
print("\n" + "=" * 50)
