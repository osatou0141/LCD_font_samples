class :
    def flavor(self):
        print("delicious")
    def shape(self):
        print("long and narrow")

class b(a):
    def shape(self):
        print("")

test1 = banana()
test1.flavor()

test2 = apple()
test2.flavor()