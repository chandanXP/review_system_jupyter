import nltk

nltk.download('punkt')
# nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

import gensim
from gensim.models import Word2Vec


