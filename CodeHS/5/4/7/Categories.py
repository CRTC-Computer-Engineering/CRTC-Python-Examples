thing_list = []

class thing():
    def __init__(self, name, tags):
        self.name = name
        self.tag1, self.tag2, self.tag3 = tags
    def list_info(self):
        print(self.name + ": "+ self.tag1 + " " + self.tag2 + " " + self.tag3)

for i in range(3):
    name = input("Enter a category: ")
    tags = [input("Enter something in that category: "), input("Enter something in that category: "), input("Enter something in that category: ")]
    thing_list.append(thing(name, tags))
    
for m_thing in thing_list:
    m_thing.list_info()