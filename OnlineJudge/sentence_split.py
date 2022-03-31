if __name__ == '__main__':
    word = input().split()
    splitter = input().split()
    i = 0
    while i < len(word):
        if splitter[i] == 'B-LOC':
            print('<LOC>', end='')
            print(word[i], end='')
            if i == len(word)-1 or splitter[i+1] == 'B-LOC' or splitter[i+1] == 'O':
                print('</LOC>', end='')
        elif i == len(word)-1 and splitter[i] == 'I-LOC':
            print(word[i], end='')
            print('</LOC>', end='')
        elif i >= 1 and splitter[i] == 'O' and splitter[i-1] == 'I-LOC':
            print('</LOC>', end='')
            print(word[i], end='')
        elif splitter[i] == 'I-LOC':
            print(word[i], end='')
        else:
            print(word[i], end='')
        i += 1