import os
class Simpledb:

    def __init__(self, filename):
        self.filename=filename
        f=open(filename,'a')
        f.close()

    def __repr__(self):
        print ("<" +"Simpledb file="+ self.filename +">")

    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()


    def select_one(self, key):
        f = open(self.filename, 'r')
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                return v[:-1]
        f.close()


    def delete(self, key):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)

            else:
                print('Deleted')

        f.close()
        result.close()
        os.replace('result.txt', self.filename)


    def update(self, key, value):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                result.write(key + '\t' + value + '\n')
                print('Updated')
            else:
                result.write(row)

        f.close()
        result.close()
        os.replace('result.txt', self.filename)
