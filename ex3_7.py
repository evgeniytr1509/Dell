def first(size, *arg):
    resalt = size + len (arg)
    print (resalt)
first(5, "first", "second", "third")

def second(size, **arg):
    resalt = size + len (arg)
    print (resalt)
second(3, comment_one="first", comment_two="second", comment_third="third")