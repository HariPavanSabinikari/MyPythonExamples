def tower_of_honoi(n, a='1',b='2',c='3'):
    if n >= 1:
        tower_of_honoi(n-1, a, c, b)
        print('Move {} to {}'.format(a,c))
        tower_of_honoi(n-1, b, a, c)
        
tower_of_honoi(3)