from bar import dict

dict.update({"sadlkfsaklfja": 2})

def printdict1(d):
    printdict(d)
    d.update({"sadlkfsaklfja": 2})
    print("The file that prints this is: " + __name__)
    print("The id of this object is: " + str(id(d)))
    print(d)
