
import pandas as pd



def name_to_numbers(letters, alf):
    letters = letters.lower()
    numbers = []

    for letter in letters:
        if alf == 'latin':
            number = ord(letter) - 96
        elif alf == 'russian':
            number = ord(letter) - 1071
        elif alf == 'bulgarian':
            number = ord(letter) - 975
        else:
            number = ord(letter) - 96
        numbers.append(number)

    return numbers


def mod9(number=int):
    return number%9



def name_quality(numbers=list):
    uniqueNums = set(numbers)
    quality = len(list(uniqueNums))
    return quality

def perfect_name(numbers=list):
    perfect = False
    if len(numbers) >= 9:
        quality = name_quality(numbers)
        if quality == 9:
            perfect=True
    return perfect

def get_quality(name, alf):
    numbers = name_to_numbers(name, alf)
    number9name = [mod9(n) for n in numbers]
    quality = name_quality(number9name)
    print(name, numbers, quality)
    return quality


# English names
'''
path = '/Users/kivanov/Downloads/baby-names.csv'

namedf = pd.read_csv(path)
namedf['quality']= namedf['name'].apply(get_quality)
namedf = namedf.sort_values(by = ['quality'])

print(namedf)
'''



'''
path = '/Users/kivanov/Downloads/russian_names.csv'
namedf = pd.read_csv(path, sep=';')
males = namedf.loc[namedf['Sex']=='М']
males['quality'] = males['Name'].apply(lambda x: get_quality(x, alf='russian'))
print(males)
males = males.sort_values(by = ['quality'])


print(males)
'''

path = '/Users/kivanov/Downloads/all_text.csv'
namedf = pd.read_csv(path, sep=';')

