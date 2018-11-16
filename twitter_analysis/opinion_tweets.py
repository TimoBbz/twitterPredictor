from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

def textblob_analysis(tweet):
    text = TextBlob(tweet, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return text.sentiment[0]
