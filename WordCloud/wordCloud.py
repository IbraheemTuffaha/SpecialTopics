import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import PorterStemmer

ps = PorterStemmer()

f = open("file.txt", "r")
data = nltk.word_tokenize(' '.join(f.readlines()))

mylist = ["great", "taking", "liked", "start", "provide", "came", "better", "much",
"find", "lot", "found", "now", "really", "mostly", "good", "started", "fine",
"loved", "makes", "using", "need", "things", "without"]
for word in mylist:
	while word in data: data.remove(word)

data = ' '.join(data);

def generate_wordcloud(text):
	wordcloud = WordCloud(
												stopwords=STOPWORDS,
												width=1280,
												height=720,
												background_color="white").generate(text);
	plt.figure(figsize=(12.8, 7.2))
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.tight_layout(pad=0)
	plt.axis("off")
	plt.savefig('wordcloud.png', bbox_inches='tight')
	plt.show()

generate_wordcloud(data)