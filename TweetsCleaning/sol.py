import pandas as pd
import re, nltk
from nltk.corpus import stopwords

# defining constants
STOP_WORDS = set(stopwords.words('english'))
STEMMER = nltk.stem.SnowballStemmer('english')
FILE_NAME = 'EI-oc-En-joy-train'


def stripID(s):
	try: return re.split(r'-', s)[2]
	except IndexError: return "-1"


def cleanTweets(s):
	# convert all the tweet to lowercase
	s = s.lower()

	# substitute tags
	s = re.sub(r'(^|\s+)@\S+', " tagaddr", s)
	
	# substitute emails
	s = re.sub(r'\S+@\S+\.\S+', "emailaddr", s)

	# substitute links
	s = re.sub(r'\S*://\S*', "linkaddr", s)

	# remove punctuation
	s = re.sub(r'[^\w]', ' ', s)

	# remove stop words and stemming
	tokens = nltk.word_tokenize(s)
	tokens = [word for word in tokens if word not in STOP_WORDS]
	tokens = [STEMMER.stem(word) for word in tokens]

	return ' '.join(tokens)

def stripNumber(s):
	try: return re.split(r':', s)[0]
	except IndexError: return "-1"


# read csv file into DataFrame
table = pd.read_csv(FILE_NAME + '.txt', delimiter='\t');

# remove ID prefix
table["ID"] = table["ID"].apply(stripID)

# clean tweets
table["Tweet"] = table["Tweet"].apply(cleanTweets)

# delete 'Affect Dimension' column
table = table.drop(columns="Affect Dimension") 

# keep 'Intensity Class' numbers only
table["Intensity Class"] = table["Intensity Class"].apply(stripNumber)

# save into csv file
table.to_csv(FILE_NAME + '_fixed' + '.txt', sep='\t', index=False)