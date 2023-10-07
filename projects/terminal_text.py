'''
name: Sebastian Plunkett
date: 9/22/2023
sources: ChatGPT for events.
reflection: This project was really fun, and I was able to really put my energy into something that I love. I wish I could spend more time on it, and I will probably
Work on it more after the submission date. The decider for if there should be a death event was fun but uncompleted to an extent.
Honor Code: I have not given nor received any unauthorized aid on this assignment. -Sebastian Plunkett
'''

import math, random, time
import numpy as np



insults = [
    'You are a smelly pirate hooker.',
    'You are a cotton-headed ninny muggins.',
    'You are a fart factory, slug-slimed sack of rat guts in cat vomit.',
    'You are a festering, rotting, fly-covered pile of dog crap.',
    'You are a spineless little worm deserving nothing but the profoundest contempt.',
    'You are a degenerate, no-talent, idiotic, pathetic, white trash ball of failure.',
    'I fart in your general direction.',
    'I could walk in a field of cow poop, and you would still be the ugliest thing in sight.',
]

bribe = [
    'A little birdie told me you were looking for some money.',
    'I have a proposition for you.',
    'I will give you $100,000 if you do me a favor.',
    'Everyone needs a little extra liquidity.',
    'I have a little extra cash lying around.',
    'I have a little extra cash lying around.',
]

mug = [
    'Give me your stuff!',
    'Hand over your wallet.',
    'I need your money.',
    'Stick \'em up!',
]

welcome = [
    'Welcome to Mob Boss.',
    'You are a newly appointed mob boss in the city of New York.',
    'Your goal is to survive and become the most powerful mob boss in the city',
    'You will have to make decisions that will affect your reputation, your influence, and your money.',
    'Good luck.',
]

intro = [
    'You are a newly appointed mob boss in the city of New York.',
    'Your goal is to survive and become the most powerful mob boss in the city',
    'You will have to make decisions that will affect your reputation, your influence, and your money.',
]

new_day = [
    'A new day has begun.',
    'You have woken up in your bed.',
    'What will you do today?',
]

new_day_decisions = [
    'Grow your empire.',
    'Party with the elite.',
    'Go to bed.',
]

end_day = [
    'You have decided to go to bed.',
    'good night.',
]

event_box = {
    'grow_your_empire.': [
        {
            "description": ["Your gang spots a rival gang member walking down the street."],
            "decisions": ["Kill him.", "Mug him.", "Bribe him.", "Ignore him."],
            "results": [
                {
                    "influence": -1,
                    "money": 0,
                    "cruelty": 1,
                    "response": ["You have killed the rival gang member.", "He will not bother you again."]
                },
                {
                    "influence": 0,
                    "money": 1,
                    "cruelty": 0,
                    "response": ["You have mugged the rival gang member.", "You have gained $100,000."]
                },
                {
                    "influence": 1,
                    "money": -1,
                    "cruelty": 0,
                    "response": ["You have bribed the rival gang member.", "He has joined your gang.", "You have lost $100,000."]
                },
                {
                    "influence": -1,
                    "money": 0,
                    "cruelty": 0,
                    "response": ["You have ignored the rival gang member.", "Your gang has lost respect for you."]
                }
            ]
        },
        {
            "description": ["You have the ability to expand your territory with a new building."],
            "decisions": ["Expand your territory.", "Do not expand your territory."],
            "results": [
                {
                    "influence": 1,
                    "money": -1,
                    "cruelty": 0,
                    "response": ["You have expanded your territory.", "You have lost $100,000."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 0,
                    "response": ["You have not expanded your territory."]
                }
            ]
        },
        {
            "description": ["A single mother is struggling to pay the loan shark, and asking you to forgive the debt"],
            "decisions": ["Forgive the debt.", "Do not forgive the debt."],
            "results": [
                {
                    "influence": 1,
                    "money": -1,
                    "cruelty": -1,
                    "response": ["You have forgiven the debt.", "You have lost $100,000."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 1,
                    "response": ["You have not forgiven the debt."]
                }
            ]
        },
        {
            "description": ["You run into a member of a rival gang on your territory."],
            "decisions": ["Negotiate a truce.", "Attack the rival member."],
            "results": [
                {
                    "influence": 1,
                    "money": 0,
                    "cruelty": -1,
                    "response": ["You successfully negotiate a truce with the rival gang member.", "Your influence in the area has increased."]
                },
                {
                    "influence": -1,
                    "money": -5,
                    "cruelty": 2,
                    "response": ["You choose to attack the rival member.", "You've lost money and increased your cruelty."]
                }
            ]
        },
        {
            "description": ["A local business owner is being extorted by a small-time thug."],
            "decisions": ["Offer protection for a fee.", "Intimidate the thug and protect the business for free."],
            "results": [
                {
                    "influence": 1,
                    "money": 1,
                    "cruelty": -1,
                    "response": ["You offer protection for a fee, gaining money and influence.", "The business owner is grateful."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 2,
                    "response": ["You intimidate the thug and protect the business for free.", "Your cruelty increases, but the business owner is safe."]
                }
            ]
        },
        {
            "description": ["One of your underlings is suspected of disloyalty."],
            "decisions": ["Conduct a thorough investigation.", "Deal with the suspected traitor immediately."],
            "results": [
                {
                    "influence": 2,
                    "money": -.05,
                    "cruelty": -1,
                    "response": ["You conduct a thorough investigation, clearing the underling's name.", "Your influence remains strong, but it costs money."]
                },
                {
                    "influence": -2,
                    "money": 0,
                    "cruelty": 3,
                    "response": ["You decide to deal with the suspected traitor immediately.", "Your cruelty increases, and you lose influence."]
                }
            ]
        },
        {
            "description": ["A rival mob boss offers a partnership in a lucrative candy trade."],
            "decisions": ["Accept the partnership.", "Refuse the offer."],
            "results": [
                {
                    "influence": 3,
                    "money": 2,
                    "cruelty": 1,
                    "response": ["You accept the partnership and enter a lucrative candy trade.", "Your influence and wealth increase."]
                },
                {
                    "influence": -2,
                    "money": 0,
                    "cruelty": -1,
                    "response": ["You refuse the offer, maintaining your independence.", "Your influence remains unchanged."]
                }
            ]
        },
        {
            "description": ["A police detective approaches you with an offer to provide information in exchange for a bribe."],
            "decisions": ["Pay the bribe and get the information.", "Refuse the offer and risk exposure."],
            "results": [
                {
                    "influence": 1,
                    "money": -1,
                    "cruelty": 0,
                    "response": ["You pay the bribe and receive valuable information.", "Your influence decreases, but you gain useful knowledge."]
                },
                {
                    "influence": -3,
                    "money": 0,
                    "cruelty": 0,
                    "response": ["You refuse the offer, not willing to compromise.", "Your influence takes a hit, but your integrity remains intact."]
                }
            ]
        },
        {
            "description": ["A rival mob boss challenges your leadership and demands a duel."],
            "decisions": ["Accept the duel.", "Ignore the challenge."],
            "results": [
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 2,
                    "response": ["You accept the duel, displaying your strength.", "Your influence remains unchanged, but your cruelty increases."]
                },
                {
                    "influence": -2,
                    "money": 0,
                    "cruelty": -1,
                    "response": ["You ignore the challenge, dismissing the rival's attempt.", "Your influence decreases slightly, but you avoid conflict."]
                }
            ]
        },
        {
            "description": ["A rival mob boss offers to share valuable stolen goods with you."],
            "decisions": ["Accept the stolen goods.", "Report the offer to the authorities."],
            "results": [
                {
                    "influence": 1,
                    "money": 2,
                    "cruelty": 0,
                    "response": ["You accept the stolen goods and profit from the arrangement.", "Your influence and wealth increase."]
                },
                {
                    "influence": -3,
                    "money": -1,
                    "cruelty": 0,
                    "response": ["You report the offer to the authorities, maintaining your integrity.", "Your influence decreases, but you uphold the law."]
                }
            ]
        },
        {
            "description": ["A member of your crew is caught stealing from your organization."],
            "decisions": ["Punish the thief.", "Forgive the thief but keep a close watch."],
            "results": [
                {
                    "influence": 1,
                    "money": 0,
                    "cruelty": 1,
                    "response": ["You punish the thief, sending a message about loyalty.", "Your influence remains strong, but it costs you money."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": -1,
                    "response": ["You forgive the thief but maintain a close watch on them.", "Your influence remains unchanged."]
                }
            ]
        },
        {
            "description": ["A prominent politician offers to pass laws that benefit your operations in exchange for financial support."],
            "decisions": ["Provide financial support to the politician.", "Decline the offer and maintain your independence."],
            "results": [
                {
                    "influence": 2,
                    "money": -7.5,
                    "cruelty": 0,
                    "response": ["You provide financial support to the politician, gaining political influence.", "Your wealth decreases, but your political power grows."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 0,
                    "response": ["You decline the offer, choosing to remain independent.", "Your influence remains unchanged."]
                }
            ]
        },
        {
            "description": ["A rival mob boss offers a truce and suggests a joint venture for a profitable casino."],
            "decisions": ["Accept the truce and partnership.", "Reject the truce."],
            "results": [
                {
                    "influence": 2,
                    "money": 2,
                    "cruelty": 0,
                    "response": ["You accept the truce and partnership, entering a lucrative casino business.", "Your influence and wealth increase."]
                },
                {
                    "influence": 0,
                    "money": 0,
                    "cruelty": 0,
                    "response": ["You reject the truce, maintaining your independence.", "Your influence remains unchanged."]
                }
            ]
        }
    ],
    'party_with_the_elite.': [
        {
            "description": ['You see a rival mob boss at the party.', 'He is alone.'],
            "decisions": ['Kill him.', 'Mug him.', 'Invite him to your table.', 'Ignore him.'],
            "results": [
                {'influence': -1, 'money': 0, 'cruelty': 2, 'response': ['You have killed the rival mob boss.','He will not bother you again.']},
                {'influence': 0, 'money': 3, 'cruelty': 0, 'response': ['You have mugged the rival mob boss.','You have gained $300,000.']},
                {'influence': 1, 'money': 0, 'cruelty': -1, 'response': ['you have invited the mob boss to your table.', 'You have become friends with the mob boss.']},
                {'influence': -1, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the rival mob boss.', 'Your gang has lost respect for you.']}
            ]
        },
        {
            "description": ['You see a rival mob boss at the party.', 'He is with his bodyguards.'],
            "decisions": ['Kill him.', 'Mug him.', 'Invite him to your table.', 'Ignore him.'],
            "results": [
                {'influence': -1, 'money': 0, 'cruelty': 0, 'response': ['You have attempted to kill the rival mob boss.', 'You have been killed by his bodyguards.']},
                {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have attempted to mug the rival mob boss.', 'You have been killed by his bodyguards.']},
                {'influence': 0, 'money': -1, 'cruelty': -1, 'response': ['You have invited the mob boss to your table.', 'You have become friends with the mob boss.', 'You have lost $100,000.']},
                {'influence': -1, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the rival mob boss.', 'Your gang has lost respect for you.']}
            ],
            'death': [
                True,
                True,
                False,
                False
            ]
        },
        {
            "description": ['You find out that one of the waiters is an undercover cop.'],
            "decisions": ['Kill him.', 'Bribe him.', 'Ignore him.'],
            "results": [
                {'influence': -1, 'money': 0, 'cruelty': 1, 'response': ['You have killed the undercover cop.','He will not bother you again.']},
                {'influence': 4, 'money': -4, 'cruelty': 0, 'response': ['You have bribed the undercover cop.','He has joined your gang.', 'You have lost $400,000.']},
                {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the undercover cop.']}
            ]
        },
        {
            "description": ['You see a drunk passerby exiting the party.'],
            "decisions": ['kill him.', 'mug him.', 'ignore him.'],
            "results": [
                {'influence': -1, 'money': 0, 'cruelty': 2, 'response': ['You have killed the drunk passerby in cold blood.', 'He was secretly a part of the FBI.', "You are known amongst the FBI"]},
                {'influence': 0, 'money': 1, 'cruelty': 0, 'response': ['You have mugged the drunk passerby.', 'You have gained $100,000.']},
                {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the drunk passerby.']}
            ]
        }
    ],
    'encounter': {
        'takeover': [
                {
                "description": ['Another mob boss has started to take over your territory.'],
                "decisions": ['Fight back.', 'Run away.'],
                "results": [
                    {'influence': -1, 'money': 0, 'cruelty': 0, 'response': ['You have fought back.', 'You have lost some of your territory.']},
                    {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have run away.', 'You have lost all of your territory.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed in hiding.']}
                ],
                'death': [
                    False,
                    True
                ]
            }, {
                'description': ['A rival mob boss is extorting you.'],
                'decisions': ['Pay him.', 'Fight him.'],
                'results': [
                    {'influence': 0, 'money': -100, 'cruelty': 0, 'response': ['You have paid him.', 'You have lost $10,000,000.']},
                    {'influence': -1, 'money': 0, 'cruelty': 0, 'response': ['You have fought him.', 'You have lost some of your territory.']}
                ],
            }
            ],
        'fbi': [
                {
                "description": ['An FBI agent has started to investigate you.'],
                "decisions": ['Bribe the FBI.', 'Kill the FBI.'],
                "results": [
                    {'influence': 1, 'money': -100, 'cruelty': 0, 'response': ['You have bribed the FBI.', 'The FBI has stopped investigating you.', 'You have lost $10,000,000.']},
                    {'influence': -1, 'money': 0, 'cruelty': 2, 'response': ['You have killed the FBI agent.', 'The FBI has put a hit on you.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed in hiding.']}
                ],
                'death': [
                    False,
                    True
                ]
            }, 
                {
                    "description": ['You have found an FBI agent hiding in your territory.'],
                    "decisions": ['Kill him.', 'Ignore him.'],
                    "results": [
                        {'influence': 1, 'money': -5, 'cruelty': 1, 'response': ['You have killed the FBI agent', 'You spent a lot of money to cover it up.', 'You have lost $500,000.']},
                        {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the FBI agent.', 'He has found out about you.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed in hiding.']}
                    ],
                    'death': [
                        False,
                        True
                    ]
                },
                {
                    'description': ['A member of your gang has been arrested by the FBI.'],
                    'decisions': ['Bail him out.', 'Ignore him.'],
                    'results': [
                        {'influence': 1, 'money': -4, 'cruelty': 0, 'response': ['You have bailed him out.', 'You have lost $400,000.']},
                        {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored him.', 'He spilled the beans on you.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed in hiding.']}
                        
                    ],
                    'death': [
                        False,
                        True
                    ]
                }
            ],
        'betrayal': [
                {
                "description": ['One of your underlings has betrayed you.'],
                "decisions": ['Kill him.', 'Ignore him.'],
                "results": [
                    {'influence': 1, 'money': 0, 'cruelty': 2, 'response': ['You have killed the traitor.', 'Your gang has gained respect for you.']},
                    {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the traitor.', 'Your gang has lost respect for you.', 'The traitor has started an uprising.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed fighting the uprising.']}
                ],
                'death': [
                    False,
                    True
                ]
            },
            {
                'description': ['A member of your gang has been funded by another mob boss.'],
                'decisions': ['Kill him.', 'Ignore him.'],
                'results': [
                    {'influence': 1, 'money': 0, 'cruelty': 2, 'response': ['You have killed the traitor.', 'Your gang has gained respect for you.']},
                    {'influence': 0, 'money': 0, 'cruelty': 0, 'response': ['You have ignored the traitor.', 'Your gang has lost respect for you.', 'The traitor has started an uprising.', 'You have lost all of your money.', 'You have lost all of your influence.', 'You have lost all of your respect.', 'You were killed fighting the uprising.']}
                ],
                'death': [
                    False,
                    True
                ]
            }
        ]
    }
}

def random_list_element(array: list):
    '''
    Returns a random element from a list.
    :param list: The list to choose from.
    :return: A random element from the list.
    '''
    return array[random.randint(0, len(array) - 1)]

def random_array(width, height, min, max):
    '''
    Generates a 2D array of random numbers.
    :param width: The width of the array.
    :param height: The height of the array.
    :param min: The minimum number to generate.
    :param max: The maximum number to generate.
    :return: The generated array.
    '''
    array = []
    for y in range(height):
        array.append([])
        for x in range(width):
            array[y].append(random.randint(min, max))
    return array

def random_array_2d(width, height, min, max):
    '''
    Generates a 2D array of random numbers.
    :param width: The width of the array.
    :param height: The height of the array.
    :param min: The minimum number to generate.
    :param max: The maximum number to generate.
    :return: The generated array.
    '''
    array = []
    for y in range(height):
        array.append([])
        for x in range(width):
            array[y].append(random.randint(min, max))
    return array

def ask(str):
    '''
    Asks the user for input with a prompt.
    :param str: The prompt to ask the user.
    :return: The user's input.
    '''
    try:
        return input(str + '\n>>> ')
    except ValueError:
        print('Please enter a valid input. (string)')
        return ask(str)

def print_sequence(sequence: list, delay: float):
    '''
    Prints a list of strings.
    :param sequence: The list of strings to print.
    :param delay: The delay between each print.
    '''
    for i in sequence:
        print(i)
        time.sleep(delay)

def ask_int(question:str):
    '''
    Asks the user for input with a prompt.
    :param int: The prompt to ask the user.
    :return: The user's input as an integer.'''
    try:
        return int(ask(question))
    except ValueError:
        print('Please enter a valid input. (int)')
        return ask_int(question)

def str_has(str: str, contains: str):
    '''
    if the string contains the substring
    :param str: the string to search
    :param contains: the substring to search for
    :return: true if the substring is in the string
    '''
    return contains in str.lower()

def str_has_all(str: str, contains: list):
    '''
    if the string contains all of the substrings
    :param str: the string to search
    :param contains: the substrings to search for
    :return: true if the substrings are in the string'''
    for contain in contains:
        if not str_has(str, contain):
            return False
    return True

def str_has_any(str: str, contains: list):
    '''
    if the string contains any of the substrings
    :param str: the string to search
    :param contains: the substrings to search for
    :return: true if any of the substrings are in the string
    '''
    for contain in contains:
        if str_has(str, contain):
            return True
    return False

# def decision(question: str or int, answers: list):

cruelty:int = 0
influence:int = 0
money:int = 0
name:str = ''

class Decision():
    
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers
        
    def ask(self):
        
        answers = ''
        
        for i in range(len(self.answers)):
            answers = answers  + " " + (f'{i + 1}: {self.answers[i]}')
        res = ask_int(self.question + ' (' + answers + ")")
        if res > len(self.answers):
            print('Please enter a valid input.')
            return self.ask()
        return [res - 1, self.answers[res - 1]]
    
    
class Event():
    
    def __init__(self, name: str, obj: object):
        # print(obj)
        self.name = name
        self.description = obj['description']
        self.decisions = Decision('What will you do?', obj['decisions'])
        self.results = obj['results']
        try:
            self.death = obj['death']
        except:
            self.death = False
        
    def start(self):
        print_sequence(self.description, 1.5)
        res = self.decisions.ask()
        return res
    
    def result(self, res: list):
        consequences = self.results[res[0]]
        print_sequence(consequences['response'], 1.5)
        
        globals()['cruelty'] += consequences['cruelty']
        globals()['influence'] += consequences['influence']
        globals()['money'] += consequences['money']
        
        if self.death:
            if self.death[res[0]]:
                return 'death'
        # return Player('Player', influence, money, cruelty)
    
    def run(self):
        res = self.start()
        return self.result(res)
            


class Day():
    
    def __init__(self, events: list):
        self.events = []
        # print(self.events)
        
    def encounter_death(self):
        cruelty = globals()['cruelty'] 
        influence = globals()['influence']
        money = globals()['money']
        
        # if the money is high, but the influence is low, you are a target for a takeover
        if money > 5 and influence < 5:
            return 'takeover'
        # if the influence is high, but the cruelty is low, you are a target for a takeover
        if influence > 5 and cruelty < 5:
            return 'takeover'
        # if the cruelty is high, bu the money is low, you are a target for the fbi
        if cruelty > 5 and money < 5:
            return 'fbi'
        # if the cruelty is high, but the influence is low, you are a target for the fbi
        if cruelty > 5 and influence < 5:
            return 'fbi'
        # if the money is high, but the cruelty is low, you are a target for a takeover
        if money > 5 and cruelty < 5:
            return 'takeover'
        # if influence is low and money is low, you are a target for a betrayal
        if influence < 5 and money < 5:
            return 'betrayal'
        # if influence is low and cruelty is low, you are a target for a betrayal
        if influence < 5 and cruelty < 1:
            return 'betrayal'
        # if money is low and cruelty is low, you are a target for a betrayal
        if money < 5 and cruelty < 5:
            return 'betrayal'
        return False
        
        
    def start(self):
        print_sequence(new_day, .5)
        decision = Decision('', new_day_decisions)
        i, a = decision.ask()
        if a == 'Go to bed.'.lower():
            return
        event_amt = random.randint(1,3)
        if event_amt == 0:
            print_sequence(end_day, .5)
            return
        for i in range(event_amt):
            if self.encounter_death() and random.randint(0, 10) == 1:
                ev = event_box['encounter'][self.encounter_death()]
            else:
                ev = event_box[a.lower().replace(' ', '_')]

            self.events.append(Event(a, random_list_element(ev)))
            res = self.events[i].run()
            if res == 'death':
                return 'death'
            
    def end(self):
                
        print_sequence(end_day, .5)
        # current player status:
        print('Your current status: \n')
        print(Player(influence, money, cruelty))
        print('\n')
        return
    
    def run(self):
        res = self.start()
        if res == 'death':
            print_sequence(['You have died.', '', random_list_element(insults), '', 'Final Score', '', Player(influence, money, cruelty)], 1)
            return 'death'
        else:
            self.end()
        

class Game():
    
    def __init__(self, array: list):
        # print(array)
        self.days = []
        for day in array:
            self.days.append(Day(day))
        
    def start(self):
        print_sequence(intro, .5)
        name = ask('What is your name?')
        globals()['name'] = name
        print(f'Hello {name}. Please enjoy staying alive.') 
        print('\n')
        print('Your current status: \n')
        print(Player(influence, money, cruelty))
        print('\n')
        for day in self.days:
            res = day.run()
            if res == 'death':
                return 'death'
            
    
            

class Player():
    
    def __init__(self, influence: int, money: int, cruelty: int):
        self.name = globals()['name']
        self.influence = influence
        self.money = money
        self.cruelty = cruelty
        
    def __str__(self):
        extra = ''
        if self.money < 0:
            extra = '\n \nYou are broke.'
        if self.cruelty > 10:
            extra += '\n \nYou are a monster.'
        if self.influence > 10:
            extra += '\n \nYou are the most powerful mob boss in the city.'
        if self.influence < 0:
            extra += '\n \nYou have a bad reputation.'
        if self.cruelty < 0:
            extra += '\n \nYou are a nice mob boss.'
        return f'Name: {self.name}\nInfluence: {self.influence * 10}\nMoney: {self.money * 100000}\nCruelty: {self.cruelty}' + extra
    
    def __repr__(self):
        return self.__str__()
    
    def __dict__(self):
        return {
            'Boss': self.name,
            'influence': self.influence,
            'money': self.money * 100000,
            'cruelty': self.cruelty,
        }
    
    def __eq__(self, other):
        return self.__dict__() == other.__dict__()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.__dict__() < other.__dict__()
    
    def __gt__(self, other):
        return self.__dict__() > other.__dict__()
    
    def __le__(self, other):
        return self.__dict__() <= other.__dict__()
    
    def __ge__(self, other):
        return self.__dict__() >= other.__dict__()
    
    def __add__(self, other):
        return Player(
            self.name,
            self.influence + other.influence,
            self.money + other.money,
            self.cruelty + other.cruelty,
        )
    
    def __sub__(self, other):
        return Player(
            self.name,
            self.influence - other.influence,
            self.money - other.money,
            self.cruelty - other.cruelty,
        )
    
    def __mul__(self, other):
        return Player(
            self.name,
            self.influence * other.influence,
            self.money * other.money,
            self.cruelty * other.cruelty,
        )
    
    def __truediv__(self, other):
        return Player(
            self.name,
            self.influence / other.influence,
            self.money / other.money,
            self.cruelty / other.cruelty,
        )
    
    def __floordiv__(self, other):
        return Player(
            self.name,
            self.influence // other.influence,
            self.money // other.money,
            self.cruelty // other.cruelty,
        )
        

def main():
    
    # print_sequence(welcome, .5)
    
    game = Game(random_array_2d(3, 10, 0, 10))
    
    game.start()
    
    


if __name__ == '__main__':
    main()