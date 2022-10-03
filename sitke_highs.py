import csv




filename='data/simple.csv'

def read_in_chunks (file_object, chunksize=100):
    while True:
        data= file_object.read(chunksize)
        if not data:
            break
        yield data


with open(filename) as f:
    for piece in read_in_chunks(f):
        print(piece)