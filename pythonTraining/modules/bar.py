dict = {}


def update_dict(d):
    print("The file that prints this is: " + __name__)
    print("The id of this object is: " + str(id(d)))
    d.update({"ruby dust": 4})
    print(d)
