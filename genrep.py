import itertools

n = int(input('Desired length: '))

#generate combinations of length n made up of only digits
with open(f'numerical{n}.txt', 'w') as outfile:
    for i in [v for v in itertools.product(range(10), repeat=n)]:
        outfile.write(''.join(map(str, i))+'\n')
