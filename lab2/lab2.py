from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from nltk.tag import pos_tag
from nltk.corpus import reuters

def read_file_to_string(fileName: str):
    try:
        with open(fileName, mode='r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
        return None
    finally:
        file.close()


filename: str = "text3.txt"

text = read_file_to_string(filename)

# Розбиваємо текст на речення
sentences = sent_tokenize(text)

# Вибираємо третє речення (індекс 2, оскільки індекси починаються з 0)
third_sentence = sentences[2]

# а) Пораховуємо кількість слів у третьому реченні (без пунктуації та інших спеціальних символів)
words = word_tokenize(third_sentence)
cleaned_words = [word.lower() for word in words if word.isalnum()]  # Видаляємо всі знаки пунктуації
word_count = len(cleaned_words)
print("Кількість слів у третьому реченні:", word_count)

# б) Видаляємо стоп-слова
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in cleaned_words if word not in stop_words]

# в) Знаходимо 10 слів, які зустрічаються найчастіше
word_freq = Counter(filtered_words)
top_10_words = word_freq.most_common(10)
print("Топ 10 слів, які зустрічаються найчастіше:")
for word, freq in top_10_words:
    print(f"{word}: {freq}")

# Завантажуємо корпус Reuters та вибираємо тексти категорії cocoa
cocoa_docs = reuters.fileids(categories='cocoa')

# Вибираємо третій текст категорії cocoa (індекс 2, оскільки індекси починаються з 0)
third_cocoa_text = reuters.raw(fileids=cocoa_docs[2])
print("\nthird cocoa text:\n" + third_cocoa_text)

# Розбиваємо текст на речення
sentences = sent_tokenize(third_cocoa_text)

# а) Виводимо речення з другого до передостаннього
print("Речення з другого до передостаннього:")
for sentence in sentences[1:-1]:
    print(sentence)

# б) Вибираємо дієслова з тексту та обчислюємо їх частоту
verbs = []
for sentence in sentences:
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        if tag.startswith('VB'):  # VB - дієслово
            verbs.append(word.lower())

# Знаходимо 8 дієслів, які зустрічаються найчастіше
verb_freq = Counter(verbs)
top_8_verbs = verb_freq.most_common(8)
print("\n8 найчастіше зустрічаючихся дієслів:")
for verb, freq in top_8_verbs:
    print(f"{verb}: {freq}")