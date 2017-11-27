import os
import tempfile

class File():
    def __init__(self, path):
        self.path = path
        
    def write(self, text):
        write_mode = 'w'
        if os.path.isfile(self.path):
            write_mode = 'a'
        with open(self.path, write_mode) as file:
            file.write(text)
    
    def __iter__(self):
        return open(self.path, 'r')
    
    def __add__(self, other):
        path = os.path.join(tempfile.gettempdir(), "2.txt")
        with open(path, 'a') as tmp_file:
            with open(self.path, 'r') as one_file:
                tmp_file.write(one_file.read())
            with open(other.path, 'r') as two_file:
                tmp_file.write(two_file.read())
        return File(path)
    
    def __str__(self):
        return self.path
    
    def read(self):
        text = ''
        with open(self.path, 'r') as file:
            text = file.read()
        return text
    
obj = File('file.txt')
obj.write('line')
obj.write('line2')
first = File('1.txt')
first.write('1.txt')
second = File('2.txt')
second.write('2.txt')

new_obj = first + second
print (new_obj)
print (new_obj.read())

for line in obj:
    print (line)