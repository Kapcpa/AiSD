import numpy


# generate arrays with non-repeating numbers in them

def generate_random_array(size):
    return numpy.random.choice(numpy.arange(size * 10), size=size, replace=False)


def generate_increasing_array(size):
    return numpy.arange(size)


sizes = [2**x for x in range(2, 18)]


for size in sizes:
    # Generate arrays
    random_array = generate_random_array(size)
    increasing_array = generate_increasing_array(size)
    
    # Add instance size as the first number and save arrays to files
    numpy.savetxt(f'benchmark/random_array_{size:08d}.txt', random_array, fmt='%d', newline=' ')
    numpy.savetxt(f'benchmark/increasing_array_{size:08d}.txt', increasing_array, fmt='%d', newline=' ')



print("Arrays have been generated and saved to files.")
