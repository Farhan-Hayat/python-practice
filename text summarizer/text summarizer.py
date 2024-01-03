from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

def text_summarizer(text, num_sentences):
    sentences = sent_tokenize(text)
    
    words = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.casefold() not in stop_words]
    
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    
    word_frequencies = {}
    for word in stemmed_words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence):
            stemmed_word = stemmer.stem(word)
            if stemmed_word in word_frequencies:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_frequencies[stemmed_word]
                else:
                    sentence_scores[sentence] = word_frequencies[stemmed_word]
    
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    summary = ' '.join(summarized_sentences)
    
    return summary

text = '''
According to reports, the leaders of INEOS are ‘worried’ about Sir Jim Ratcliffe’s prolonged attempt to buy Man Utd from the Glazer family.

Ratcliffe has been the owner of Ligue 1 outfit Nice since 2019 but he has actively looked to gain control of a Premier League club over the past year.

The British billionaire was interested in Chelsea before Todd Boehly’s consortium completed their takeover last year.

 He turned his attention to Man Utd after the Glazers put the Premier League up for sale towards the end of last year. At the time, they claimed that they would be “evaluating all options”.

Ratcliffe has been leading the race to buy Man Utd along with Sheikh Jassim. They are both interested in becoming the club’s new majority stakeholder.

Sheikh Jassim is only interested in a full takeover, while Ratcliffe is willing to keep the Glazer family on board with a reduced stake of 20%.

Miguel Delaney in the Independent believes Man Utd bidders are ‘hopeful there will be an announcement regarding a preferred bidder by the close of the domestic season, and potentially as early as Friday this week.’

He adds: ‘Although that is already much later than expected, and will bring some more clarity, sources with knowledge of the situation are describing it as “another milestone of constant milestones” in a process that could yet go on months.’

Now a report from RMC Sport (via Sport Witness) claims the leaders of INEOS have ‘worries’ about the bid for Man Utd.

INEOS are said to be wary about the ‘problems’ this takeover is causing for Nice. The French club’s season has featured ‘more lows than highs’ and there is the feeling that Ratcliffe are ‘more concerned with that takeover effort than preparing Nice for next season’.


'''

summary = text_summarizer(text , 1)
print(summary)
