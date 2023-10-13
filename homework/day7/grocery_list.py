'''
name: Sebastian Plunkett
date: 10/1/2023
sources: None.
reflection: This was a good use of lists, and I was able to stretch my mind in more ways to use a list. This code can definitely be simpler, but for some
reason I like writing it this way.
Honor Code: I have not given nor received any unauthorized aid on this assignment. -Sebastian Plunkett
'''


import math, time

def ask(str):
    return input(str + '\n>>> ')

def intro():
    intro = [
        'Welcome to the grocery list app!',
        'Please enter the items you wish to add to your grocery list.',
        'If you want to add an item, type "add"'
        'If you want to remove an item, type "remove" ',
        'If you want to clear your list, type "clear"',
        'If you want to update an item, type "update"',
        'If you want to sort your list, type "sort"'
        'If you want to see your list, type "show"',
        'If you want to save your list, type "save"'
        'If you are done, type "done"',
        'If you need help, type "help"',
        'You can also type "help" to see this message again.'
        ]
    for line in intro:
        print(line)
        time.sleep(.75)
    

    
class GroceryList:
    
    def __init__(self):
        self.list = []
        self.done = False
        
    def commands(self):
        return '(add, remove, help, show, done, clear, update, sort, save)'
    
    def add(self):
        item = ask('What item would you like to add?')
        self.list.append(item)
        print('Added ' + item + ' to your list.')
        
    def remove(self):
        if len(self.list) == 0: return print('Your list is empty.')
        item = ask('What item would you like to remove?')
        try:
            self.list.remove(item)
            print('Removed ' + item + ' from your list.')
        except ValueError:
            print('That item is not in your list.')
            return self.getInput()
        
    def show(self, numbered = False):
        print('Your grocery list:')
        for i, item in enumerate(self.list):
            if numbered:
                print(str(i + 1) + ' - ' + item)
            else:
                print(" - "+item)
        if len(self.list) == 0:
            print('Your list is empty.')
            
    def update(self):
        if len(self.list) == 0: return print('Your list is empty.')
        self.show(True)
        item = ask('What item number would you like to update?')
        try:
            num = int(item)
            if num > len(self.list) or num < 1:
                raise ValueError
            print('Updating item ' + str(num) + '...')
            self.list[num - 1] = ask('What would you like to replace it with?')
            print('Updated item ' + str(num) + ' to ' + self.list[num - 1])
            print('Your list is now:')
            self.show(True)
        except ValueError:
            print('That item is not in your list.')
            return self.getInput()
    
    def save(self):
        if len(self.list) == 0: return print('Your list is empty.')
        print('Saving your list...')  
        try:
            with open('grocery_list.txt', 'w') as f:
                f.write('Your grocery list: ' + time.strftime('%m-%d-%y %I:%M %p') + '\n')
                for i, item in enumerate(self.list):
                    f.write(str(i + 1) + ' - ' + item + '\n')
            print('Saved your list to grocery_list.txt')
        except:
            print('There was an error saving your list.')
            
    def sort(self):
        if len(self.list) < 1: return print('Your list is empty.')
        res = ask('Would you like to sort your list alphabetically or reverse alphabetically? (a/r)').lower()
        try:
            if res == 'a':
                self.list.sort()
                print('Your list has been sorted alphabetically.')
            elif res == 'r':
                self.list.sort(reverse=True)
                print('Your list has been sorted reverse alphabetically.')
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid command (a/n)')
            return self.sort()
    
    def getInput(self):
        res = ask('What would you like to do? ' + self.commands()).lower()
        
        if res == 'add':
            return self.add()
        elif res == 'remove':
            return self.remove()
        elif res == 'help':
            intro()
            return self.getInput()
        elif res == 'show':
            return self.show()
        elif res == 'done':
            self.done = True
            self.show()
            print('Goodbye!')
        elif res == 'update':
            return self.update()
        elif res == 'clear':
            self.list = []
            print('Your list has been cleared.')
        elif res == 'save':
            self.save()
        elif res == 'sort':
            self.sort()
        else:
            print('Please enter a valid command ' + self.commands())

def main():
    
    intro()
    list = GroceryList()
    while not list.done:
        list.getInput()

if __name__ == '__main__':
    main()