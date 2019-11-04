import os

def count_and_print(path, level=0, printable=True, threshold=0):
    count = 0
    files = os.listdir(path)
    for i in files:
        file = os.path.join(path, i)
        if os.path.isfile(file):
            count += 1
        elif os.path.isdir(file):
            count += count_and_print(file, level+1, printable=printable, threshold=threshold)
    if printable and count > threshold:
        print('\t' * (level + 1) + path + '\t' + str(count))
    return count

if __name__ == '__main__':
    path = input('Input your path name:')
    if not path:
        path = '.'
    count_and_print(path, threshold=0)
