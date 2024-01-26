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

def filter_stanza(stanza: str):
    #filter any punctuation and numbers
    return ''.join([c for c in stanza if c.isalpha() or c == ' ']).lower()

def words_in_line(stanza: str):
    # split the line into words
    return filter_stanza(stanza).split()

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

def stanza_length(poem):
    length = {}
    for line in poem:
        if len(line) == 0:
            continue
        if len(line) in length:
            length[len(line)] += 1
        else:
            length[len(line)] = 1
    return length

def sentence_length(poem):
    end_terms = ['.', '?', '!']
    length = {}
    sentence_builder = ''
    for line in poem:
        if len(line) == 0:
            continue
        for char in line:
            if char in end_terms:
                if len(sentence_builder) in length:
                    length[len(sentence_builder)] += 1
                else:
                    length[len(sentence_builder)] = 1
                sentence_builder = ''
            else:
                sentence_builder += char
    return length
        
        
print(stanza_length(poem), 'characters per stanza')

print(sentence_length(poem), 'characters per sentence')

# beginning to plot data and start finding relationships

def rhyme_patterns(poem):
    patterns = {}
    for line in poem:
        if len(line) == 0:
            continue
        # last three characters in line
        pattern = filter_stanza(line)[-3:]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1
    return patterns

print(rhyme_patterns(poem))

def end_word_patterns(poem):
    patterns = {}
    for line in poem:
        if len(line) == 0:
            continue
        # last word in line
        words = words_in_line(line)
        for word in words:
            pattern = word[-3:]
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1
    return sort_pattern_by_frequency(patterns)

print(end_word_patterns(poem))
