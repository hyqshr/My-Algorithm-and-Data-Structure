#implement djb2
import re
import random
from collections import Counter
class ListNode:
    def __init__(self,count,string):
        self.val = count
        self.key = string
        self.next = None
        self.prev = None

class Hashmap():
    def __init__(self,size = 10000):
        self.HashTable = [[] for _ in range(size)]
        self.collision = 0

    def hashing(self,string):
        hash = 33
        for num,char in enumerate(string):
            hash = ord(char)*num*hash + hash
            hash = hash >> len(string)
        return hash

    # def hash_djb2(s):
    #     hash = 5381
    #     for x in s:
    #         hash = ((hash << 5) + hash) + ord(x)
    #     return hash & 0xFFFFFFFF

    def insert(self,string):
        hash_key = self.hashing(string)
        if self.HashTable[hash_key]:
            head = self.HashTable[hash_key]

            #check if input string match the first node
            while head:
                if head.key == string:
                    head.val += 1
                    return None
                elif head.next:
                    head = head.next
                else:
                    self.collision += 1
                    head.next = ListNode(1, string)
                    cur = head.next
                    cur.prev = head


        else:
            self.HashTable[hash_key] = ListNode(1, string)


    def find(self,string):
        '''

        :param key:
        :return: the object according to the key
        '''
        key = self.hashing(string)
        head = self.HashTable[key]
        if not head:
            print('string not found in the hash table!')
            return None

        while head and head.key != string:
            head = head.next
        return head

    def delete(self,string):
        key = self.hashing(string)
        head = self.find(string)

        if not head:
            print('{} is not found'.format(string))
            return

        #find the string in chaining
        while head:
            if head.key == string:
                break
            else:
                head = head.next
        #if head is not the first node
        if head.prev:
            head.prev.next = head.next
        #else
        else:
            self.HashTable[key] = head.next

        if head.next:
            head.next.prev = head.prev

    def increase(self,string,num):
        if self.find(string):
            self.find(string).val += num

    # Function to display hashtable
    def display_hash(self):
        for i in range(len(self.HashTable)):
            if self.HashTable[i]:
                head = self.HashTable[i]
                while head:
                    print("-->", end=" ")
                    print(head.key, head.val, end=" ")
                    head = head.next
                print('')

    def check(self):
        used_slot = 0
        for i in range(len(self.HashTable)):
            if self.HashTable[i]:
                used_slot += 1
        print('{} of 10000 slot are used'.format(used_slot))
        print('{} collisions happens'.format(self.collision))


def read_file_to_string_list(file_path):
    with open(file_path,encoding='cp1252') as f:
        corpus = f.read()
        corpus = corpus.split()
        string_list = []
        for word in corpus:
            word = re.sub('\W','',word)
            word = word.strip()
            if word and word != ' ':
                string_list.append(word)
    return string_list

def find_unique_word_number(corpus):
    '''
    :param corpus:
    :return # of unique word in a give corpus
    '''
    table = Counter(corpus)
    return len(table)

if __name__ == '__main__':
    # Creating Hashtable
    hashmap = Hashmap()

    #read corpus
    file_path = 'alice_in_wonderland.txt'
    corpus = read_file_to_string_list(file_path)

    #insert word from corpus into hashtable
    for i in corpus:
        hashmap.insert(i)
    hashmap.display_hash()
    hashmap.check()

    print('\n\n------------Report of corpus------------\n\n')
    print('There are {} word in the corpus'.format(len(corpus)))
    print('There are {} unique word in the corpus'.format(find_unique_word_number(corpus)))

    #Test find function
    print('\n\n------------Test function------------\n\n')
    print('Try find word:\'just\'',hashmap.find('just').key)
    print('Try find Non-exist word: asd456',hashmap.find('asd456'))


    #Test delete function
    print('\n\n------------Test delete function------------\n\n')
    hashmap.delete('just')
    print('Delete word:just',hashmap.find('just'))
    print('Try find non-exist word:a9ds8',hashmap.find('a9ds8'))


    print('\n\n------------Test increase function------------\n\n')
    #Test increase function
    print('count of word:\'the\' is: ',hashmap.find('the').val)
    hashmap.increase('the',10)
    print('count of word:\'the\' after increase is: ',hashmap.find('the').val)

# \begin{minted}{python}
# \end{minted}