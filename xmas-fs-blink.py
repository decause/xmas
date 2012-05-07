#!/usr/bin/env python

def xmastree():
    '              ';from\
                random import\
               randint as ri;\
    print '\n'.join([s.center(80) for s in\
    (lambda h:(lambda b:['*'] + sum([b(n) #
    for n in range(1, (h - 1) // 2)], []) +
    b((h - 1) // 2, True) + ['| |'])(lambda
    n, last=False:(lambda o:['/' + "".join(
    [o() for m in range(0, n * 2 -1)])+'\\'
    , '/' + ('_' * (n * 2 + 1) if last else
    "".join([o() for m in range(0, n * 2 -1
    )])) + '\\'])(lambda:"!@#$%^&"[ri(0, 6)
    ] if ri(0, 99) > 80 else ' ')))(20)]) #

def blink():
    while True:
        import time
        print '\n'
        print '\n'
        print '\n'
        print '\n'
        print '\n'
        print '\n'
        print '\n'
        time.sleep(1.8)
        xmastree()

blink()
