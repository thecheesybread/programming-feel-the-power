statements = {}
'''X is y.'''
'''What is x?'''
while True:
    x = raw_input(">")
    if x[-1] == '.':
        x_split = x.split(' is ')
        statements[x_split[0].lower()] = x_split[1][:-1]
    elif x[-1] == '?':
        x_split = x.split(' is ')
        print x_split[1][:-1] + ' was stated to be ' + statements[x_split[1][:-1].lower()] + '.'
    else:
        print 'write a statement or a question.'
        
        
