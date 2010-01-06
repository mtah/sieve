
def s(xs):
    return [] if not xs else xs[:1] + s([x for x in xs[1:] if x % xs[0] > 0])
    
if __name__ == '__main__':
    print s(range(2,500))
