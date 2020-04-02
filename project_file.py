import csv
import time
from avltrees import BalancingTree
from lab0_utilities import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from google_trans import Translator
from google_trans import LANGCODES
# restart the terminal every time i compile:
# sleep  function
# how to improve ui
# input like press 1 and stuff
# scroll function with previous_word and next_word
# make sure delete works (how to integrate with new code)


def lev(len_a, len_b, str1, str2):
    if (min(len_a, len_b) == 0):
        return max(len_a, len_b)  
    else:
        f = lev(len_a-1, len_b, str1, str2) + 1
        g = lev(len_a, len_b-1, str1, str2) + 1
        z = 1 if str1[len_a-1] != str2[len_b-1] else 0
        h = lev(len_a-1, len_b-1, str1, str2) + z   
        return min(f, g, h)

def collect_string(a, b):
    return lev(len(a), len(b), a, b)



class Engsci_Press:
    def __init__(self, author):
        self.author = author
        self.dictionary_tree = None
        
    def process_dictionary(self, filename):
        with open(filename, 'r') as f:       
            t = f.readline()
            t = t[1:]
            t.replace('\n', '')
            t_1 = t.split(' (')
            tree = BalancingTree(Node(Word(t_1[0], '('+t_1[1])))
            csv_row = csv.reader(f)
            for row in csv_row:
                if(row != []):
                    row = ''.join(row)
                    n = row.split(' (')
                    if(len(n) == 2):
                        n[1] = '(' + n[1]
                        tree.balanced_insert(Node(Word(n[0], n[1])))
            return tree 
                
    def collate_bsts(self, filenam):
        self.dictionary_tree = BalancingTree(Node2(self.process_dictionary(filenam + '/A.csv')))
        dictionary_format = 'Dictionary_in_csv/'
        for i in range(66, 91):
            filename = dictionary_format + str(chr(i)) + '.csv' 
            self.dictionary_tree.balanced_insert(Node2(self.process_dictionary(filename)))
        return self.dictionary_tree
    
    def search(self, root, key):
        while root and not root._val == key:
            if key < root._val:
                root = root.left
            else:
                root = root.right
        return root
    
    def searcher(self, key):
        peek = self.dictionary_tree.root
        peet = self.search(peek, key)
        return peet
    
    def searchier(self, root, key):
        fleek = root
        p = self.search(fleek, key)
        return p
    
    def output_definition(self, phrase):
        phrase = phrase.capitalize()
        z = self.searcher(phrase[0])
        if(z):
            p = self.searchier(z.val.root, phrase)
            x = []
            for i in p.val:
                x.append(i.definition)
                x.append('\n')
            del x[-1]
            return ''.join(x) 
        else:
            return 'Not found'
        
    def subset_words(self, phrase):
        phrase = phrase.capitalize()
        z = self.searcher(phrase[0])
        answer =[]
        if(z):
            p = self.searchier(z.val.root, phrase)
            next = z.val.successor(p)
            answer.append(p._val)
            while(next._val[:len(phrase)] == phrase):
                answer.append(next._val)
                next = z.val.successor(next)
        return answer
    
    def findName(self, node, language_name):
        if node is None:
            return False
        if language_name in node._val:
            return node.val.definition
        elif language_name < node._val:
            return self.findName(node.left, language_name)
        else:
            return self.findName(node.right, language_name)

    def add_word(self, word, definition):
        word = word.capitalize()
        z = self.searcher(word[0])
        z.val.balanced_insert(Node(Word(word, definition)))

    def previous_word(self, word):
        word = word.capitalize()
        z = self.searcher(word[0])
        if(z):
            p = self.searchier(z.val.root, word)
            t = z.val.predecessor(p)
            return t._val, [a.definition for a in t.val]
        else:
            return None
        
    def next_word(self, word):
        word = word.capitalize()
        z = self.searcher(word[0])
        if(z):
            p = self.searchier(z.val.root, word)
            t = z.val.successor(p)
            return t._val, [a.definition for a in t.val]
        else:
            return None
        
    def size(self):
        size = 0
        #n = z.val.preOrder(z.val.root)
        '''
        k = open("slack.txt", "w")
        for i in n:
            k.write(i + " " )
        k.close()
        '''
        for i in range(65, 91): 
            z = self.searcher(str(chr(i)))
            size += z.val.preorder_count(z.val.root)
        return size
    
    def push_tofile(self, filename):
        k = open(filename, "w")
        for i in range(65, 91): 
            z = self.searcher(str(chr(i)))
            n = z.val.inOrder(z.val.root)
            for i in n:
                for p in i:
                    k.write(p.name + ' ' + p.definition)
                k.write('\n')
        k.close()
        
    def suggest_word(self, word, threshold = None):
        word = word.capitalize()
        #answer = 15
        #suggested_word = ''
        n = []
        for i in range(65, 91): 
            z = self.searcher(str(chr(i)))
            n += z.val.preOrder(z.val.root)
            
            '''
            for i in n:
                lent = collect_string(word, i) 
                if(lent < answer):
                    answer = lent
                    suggested_word = i
                if (answer == 0):
                    return suggested_word
            '''
        z = process.extractOne(word, n) 
        if(threshold):
            if(z[1] >= threshold):
                return z[0]
            else:
                return "No suggestions"
        else:
            return z[0] 

    def reference_word(self, word: str, subset_size):
        word = word.capitalize()
        z = self.searcher(word[0])
        answer = []
        if(z):
            p = self.searchier(z.val.root, word)
            count = 0
            next = p
            previous = p
            while(count < subset_size):
                next =  z.val.successor(next)
                answer.append(next._val)
                count+=1
                if (count < subset_size):
                    previous = z.val.predecessor(previous)
                    answer.insert(0, previous._val)
                    count += 1
        return answer
    
    def translate_word(self, word, destination = None, source = None):
        translator = Translator()
        if(destination):
            destination = LANGCODES[destination.lower()]
            if(source):
                source = LANGCODES[source.lower()]
                result = translator.translate(word, dest= destination, src=source)
                return result.text.capitalize()
            else:
                result = translator.translate(word, dest= destination)
                return result.text.capitalize()
        else:
            if(source):
                source = LANGCODES[source.lower()]
                result = translator.translate(word, src=source)
                return result.text.capitalize()
            else:
                result = translator.translate(word)
                return result.text.capitalize()
            
    def scroll (self, word, num_words, direction = 0):
        if direction != 0 or direction!=1:
            print("Wrong direction! Specify the direction, please.")
            print("0 for a previous word, 1 for a next word.")
            return 
        for i in range(num_words):
            if direction == 0:
                word = self.previous_word(word)
                if not word:
                    print("That's the end of the dictionary, sorry.")
                    break
                print("The previous word is: ", word)
                return 
            if direction == 1:
                word = self.next_word(word)
                if not word:
                    print("That's the end of the dictionary, sorry.")
                    break
                print("The next word is: ", word)
            return 
    







 
if __name__== '__main__':
    dictionary_format = 'Dictionary_in_csv'
    dict = Engsci_Press("Vicky")
    x = time.time()
    dict.collate_bsts(dictionary_format)
    print(dict.output_definition("Banality"))
    dict.add_word("Strtd", "(n.) Some asshole")
    print(dict.output_definition("Strtd"))
    print(dict.next_word("millet"))
    print(dict.subset_words("push"))
    print(dict.size())
    print(dict.reference_word("lambaste", 3))
    dict.push_tofile("slack.txt")
    print(dict.suggest_word("Slaek", 80))
    print(dict.translate_word("buenos dias", source="spanish", destination='russian'))
    y = time.time()
    print(y-x)

    

