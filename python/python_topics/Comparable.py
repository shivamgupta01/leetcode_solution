def compareTo(self, that):
    return ((self > that) - (self < that))


f1 = compareTo(1,1)
f2 = compareTo(2,2)

f1.compareTo(f2)
compareTo.compare(f1,f2)