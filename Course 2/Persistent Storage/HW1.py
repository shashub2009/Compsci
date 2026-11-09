import pathlib, pickle
num = [x for x in range(1000)]
file_path= pathlib.Path('data') / 'text'
if file_path.exists():
    print('file exists')
else:
    with open(file_path, 'w') as f: 
        print(num, file=f)

f = open(file_path)
for n in f:
    print(n)
            




