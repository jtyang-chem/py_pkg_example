import sys
sys.path.append("./somewhere/")

def test1():
    import my_pkg.m1 as m2
    m2.fun()

def test2():
    import my_pkg
    my_pkg.fun()

test1()
test2()
