import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist

f1=open('viki5.txt','r', encoding="UTF-8") # текст в файле
text= f1.read()
text = text.lower() 
text_tokens = word_tokenize(text) # получили список слов (токенов)
text = nltk.Text(text_tokens)

stop_words = stopwords.words('russian')# заносим стоп-слова в переменную
stop_words.extend(['!', ',', '.', '(', ')', '«', '»'])
set_stop = set(stop_words) # создаем множество

filtered_sentence = []
for w in text: 
    if w not in set_stop: 
        filtered_sentence.append(w) 

fdist = FreqDist(filtered_sentence)
print(fdist) #  сколько оригинальных слов (samples) и сколько всего (utcomes)
print(fdist.most_common(15)) # заданное количество самых частых

