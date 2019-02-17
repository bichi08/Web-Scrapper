def fprint(itr):
    if type(itr) == type([]):
        for i in itr:
            print(i)
    elif type(itr) == type({}):
        for k, v in itr.items():
            print("{} : {}".format(k, v))
