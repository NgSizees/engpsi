import csv
import time
from avltrees import BalancingTree
from lab0_utilities import *

class Engsci_Press:
    def __init__(self, author):
        self.author = author
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
                
    def collate_bsts(self):
        self.dictionary_tree = BalancingTree(Node2(self.process_dictionary('projects/dictionary/Dictionary_in_csv/A.csv')))
        dictionary_format = 'projects/dictionary/Dictionary_in_csv/'
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
    def push_tofile(self):
        k = open("slack.txt", "w")
        for i in range(65, 91): 
            z = self.searcher(str(chr(i)))
            n = z.val.inOrder(z.val.root)
            for i in n:
                for p in i:
                    k.write(p.name + ' ' + p.definition)
                k.write('\n')
        k.close()

        

    




if __name__== '__main__':
    dict = Engsci_Press("Vicky")
    x = time.time()
    dict.collate_bsts()
    print(dict.output_definition("Babe"))
    dict.add_word("Strtd", "(n.) Some asshole")
    print(dict.output_definition("Strtd"))
    print(dict.next_word("millet"))
    print(dict.subset_words("push"))
    print(dict.size())
    dict.push_tofile()
    y = time.time()
    print(y-x)

    

