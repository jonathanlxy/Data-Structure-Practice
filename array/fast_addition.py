# Array manipulation - Fast addition
'''
1. Construct an array (1-indexed) of size n with initial value = 0.
2. A method array.add(start, end, x) to add x to each element
    of array from start index to end index (both inclusive).

3. A method array.max() to return the max value in the array.

Test.txt:
    Test file, first row contains the array config and expected output
    (size, number of query, expected output)

    Each of the following rows is a query, contains (start, end, x)
'''

class Array():
    def __init__(self, n):
        self.array = [0] * n

    def add(self, start, end, x):
        self.array[start - 1] += x
        if end < len(self.array): self.array[end] -= x

    def max(self):
        result = 0
        current_sum = 0
        for i in self.array:
            current_sum += i
            if result < current_sum: result = current_sum
        return result

if __name__ == "__main__":
    with open('test.txt', 'rb') as f:
        n, m, test = map(int, f.readline().split(' '))
        arr = Array(n)
        for i in xrange(m):
            a, b, x = map(int, f.readline().split(' '))
            arr.add(a, b, x)
    assert arr.max() == test, \
        'Max value: {}. Test failed. Expected output: {}'.format(
            arr.max(), test)
    print 'Max value: {}. Test passed.'.format(arr.max())

# ### Compare performance (Numpy implementation will be super slow)
# import datetime
# import numpy as np
# results = []
# cur = datetime.datetime.now()
# with open('test.txt', 'rb') as f:
#     n, m, test = map(int, f.readline().split(' '))
#     arr = Array(n)
#     for i in xrange(m):
#         a, b, x = map(int, f.readline().split(' '))
#         arr.add(a, b, x)
# a = arr.max()
# results.append((datetime.datetime.now() - cur))

# cur = datetime.datetime.now()
# with open('test.txt', 'rb') as f:
#     n, m, test = map(int, f.readline().split(' '))
#     arr = np.array([0] * n)
#     for i in xrange(m):
#         a, b, x = map(int, f.readline().split(' '))
#         arr[a-1:b] += x
# a = arr.max()
# results.append((datetime.datetime.now() - cur))

# print results