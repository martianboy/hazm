
from .PeykareReader import PeykareReader
from .BijankhanReader import BijankhanReader
from .HamshahriReader import HamshahriReader
from .DadeganReader import DadeganReader
from .SentenceTokenizer import SentenceTokenizer
from .WordTokenizer import WordTokenizer
from .Normalizer import Normalizer
from .Stemmer import Stemmer
from .Lemmatizer import Lemmatizer
from .POSTagger import POSTagger
from .Chunker import Chunker
from .DependencyParser import DependencyParser

sentence_tokenizer = SentenceTokenizer()
sent_tokenize = lambda text: sentence_tokenizer.tokenize(text)
word_tokenizer = WordTokenizer()
word_tokenize = lambda text: word_tokenizer.tokenize(text)
