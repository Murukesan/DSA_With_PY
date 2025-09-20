my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]
def hash_function(value):
    sum_of_chars=0
    for char in value:
        sum_of_chars+=ord(char)
    return sum_of_chars%10
def contains(name):
    index=hash_function(name)
    print(my_hash_set[index])
    if name in my_hash_set[index]:
        return True
    return False
def add(name):
    index=hash_function(name)
    bucket=my_hash_set[index]
    if name not in bucket:
        bucket.append(name)
add('Stuart')
print(my_hash_set)
print('contains stuart:',contains('Stuart'))