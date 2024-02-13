import warnings
from gensim.models import Word2Vec
import gensim
from nltk.tokenize import sent_tokenize, word_tokenize
import pronouncing
warnings.filterwarnings('ignore')

poem = [
    "On the top of a hill on the Island of Zort",
    "Lived a bird called the Ruckus, whose favorite sport",
    "Was making loud noises. It gave him a thrill",
    "To be known as the loudest-mouthed bird on the hill.",
    "Then, one day, he thought, 'I can be louder still!'",
    "'My voice is terrific. It ought to be heard",
    "On many more islands than this,' said the bird.",
    "So he made his voice stronger, 'till, one day, he found",
    "That he'd learned how to make a tremendous big sound",
    "That shook every island for fifty miles 'round!",
    "",
    "'I say!' laughed the Ruckus. 'I am a great guy!",
    "'But I can do better than that if I try.",
    "'I'll build up my voice. Why, I'll practice a year!",
    "'I'll cook up a noise that the whole world will hear!'",
    "And, after he'd practiced for fifty-two weeks,",
    "The Ruckus let loose with a mouthful of shrieks",
    "That burst from his throat like the moans and the groans",
    "Of then thousand elephants blowing trombones!",
    "He yapped and he yodeled! He Yelped and he yilped!",
    "He gargled! He snargled! He burped and he bilped!",
    "And the sound went to China and knocked down three cats.",
    "And, in England, it blew off eight bus drivers' hats!",
    "",
    "'Oh, boy!' bragged the Ruckus. 'I'm really some bird!",
    "'I've opend my mouth and I've made myself heard!'",
    "",
    "Then a little old worm crawled up out of the ground.",
    "'That's true.' said the worm. 'That was quite a big sound.",
    "'But I have a question to ask, if I may...",
    "'You made yourself heard. But just what did you say?'",
    "And the worm turned his back and slid softly away.",
]

# statistical analysis on the poem

def filter_line(line: str):
    #filter any punctuation and numbers
    return ''.join([c for c in line if c.isalpha() or c == ' ']).lower()

def words_in_line(line: str):
    # split the line into words
    return filter_line(line).split()

def sort_pattern_by_frequency(patterns: dict):
    # sort patterns by frequency
    return sorted(patterns.items(), key=lambda x: x[1], reverse=True)

# total lines
def total_lines(poem):
    return len(poem)

print(total_lines(poem), 'total lines')

# relationship between the sentence and its ending punctuation

def sentence_ending_punctuation(poem):
    punctuation = {}
    for line in poem:
        if len(line) == 0:
            continue
        if line[-1] in punctuation:
            punctuation[line[-1]] += 1
        else:
            punctuation[line[-1]] = 1
    return punctuation

print(sentence_ending_punctuation(poem))

# relationship between the sentence and its length and stanzas and its length

def line_length(poem):
    length = {}
    for line in poem:
        if len(line) == 0:
            continue
        if len(line) in length:
            length[len(line)] += 1
        else:
            length[len(line)] = 1
    return length

print(line_length(poem), 'characters per stanza')

def sentence_length(poem):
    end_terms = ['.', '?', '!' ]
    lengths = []
    sentence_builder = ''
    for line in poem:
        if len(line) == 0:
            continue
        for char in line:
            if char in end_terms:
                if len(sentence_builder) > 0:
                    lengths.append(len(sentence_builder))
                    sentence_builder = ''
            else:
                sentence_builder += char
    return lengths
        
        

print(sentence_length(poem), 'characters per sentence')

def sentence_length_words(poem):
    lengths = []
    for line in poem:
        if len(line) == 0:
            continue
        lengths.append(len(words_in_line(line)))
    return lengths

print(sentence_length_words(poem), 'words per sentence')

# beginning to plot data and start finding relationships

def rhyme_patterns(poem):
    patterns = {}
    for line in poem:
        if len(line) == 0:
            continue
        # last three characters in line
        pattern = filter_line(line)[-3:]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1
    return patterns

print(rhyme_patterns(poem))

def end_word_patterns(poem):
    patterns = {}
    exclude = set('for a of the and to in'.split(' '))
    for line in poem:
        if len(line) == 0:
            continue
        # last word in line
        words = words_in_line(line)
        for word in words:
            pattern = word[-3:]
            if pattern in exclude:
                continue
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1
    return sort_pattern_by_frequency(patterns)

print(end_word_patterns(poem))

# check meter of poem

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def count_syllables(word: str):
    count = 0
    if len(word) == 0:
        return count
    phones = pronouncing.phones_for_word(word)
    if len(phones) > 0:
        count = pronouncing.syllable_count(phones[0])
    return count

def get_syllables_in_line(line):
    syllables = []
    for word in words_in_line(line):
        syllables.append(count_syllables(word))
        
    return syllables

def get_syllables_in_poem(poem):
    syllables = []
    for line in poem:
        if len(line) == 0:
            continue
        syllables.append(get_syllables_in_line(line))
    return syllables

print(get_syllables_in_poem(poem))

print([sum(i) for i in get_syllables_in_poem(poem)])

def get_stressed_syllables_in_poem(poem):
    syllables = []
    for line in poem:
        if len(line) == 0:
            continue
    return syllables

stoplist = set('for a of the and to in'.split(' '))

text = [[word for word in document.lower().split() if word not in stoplist]
        for document in poem]

from collections import defaultdict
frequency = defaultdict(int)
for text in text:
    for token in text:
        frequency[token] += 1

model1 = Word2Vec([poem])

print(model1.wv.most_similar([('snargled!', 'he')]))