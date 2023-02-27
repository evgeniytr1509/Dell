
fh = open('d:\\test_file.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('d:\\test_file.txt', 'r')
while True:
    symbol = fh.read(1)
    
    print(symbol)

fh.close()



