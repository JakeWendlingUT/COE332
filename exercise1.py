import names

with open('words', 'r') as infile:
        words = infile.read().splitlines()
count = 0
for word in words:
        if len(word.strip(' ')) == 8 and count < 5:
                print(word)
                count += 1

for x in range(5):
        name = names.get_full_name()
        length = len(name.replace(" ", ""))
        print(f'{name} {length}')
