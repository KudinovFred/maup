"""

1. Чтение строки с отфильтровыванием символов, которые не цифры

готово  2. Разбиение строки на группы по 3
например    "123456789"  = "123 456 789"
3. Из строки УРЛ адрес  извлечь  имя файла
напимер https://web.telegram.org/#  =   web.telegram.org
готово  4. Поиск самого длинного слова в предложении
готово  5. Авто генератор пароля из 8 символов (буква, цифра, знак)

"""

def trinity(number, sep=" "):
    """
    """
    result = list(str(number))

    x = len(str(number))%3

    for i in range(x,len(result),3):
        result[i]=sep+result[i]

    return  "".join(result).lstrip(sep)



print(trinity(1))
print(trinity(12))
print(trinity(123))
print(trinity(1234))
print(trinity(12345))
print(trinity(123456))
print(trinity(1234567))
print(trinity(12345678))
print(trinity(123456789))
print(trinity(1234567890))



def get_url(url):
    return url.split("/")[2]

print(get_url("https://web.telegram.org/#"))




def get_longest(text, max = True):
    text= list(text.split(" "))
    x = dict((word,len(word)) for word in text if len(word))

    f = sorted(x, reverse=max)
    print (f)
    return (f[0])


get_longest("one two three four five six seven eight eleven 123456789", max=False)
get_longest("one two three four five six seven eight eleven 123456789", max=True)

def password(length=8):
    import string
    import random

    result = []
    for i in range(length):
        result.append(random.choice(string.ascii_lowercase+string.digits))
    return "".join(result)



print(password(length=10))
print(password(length=12))
print(password(length=14))
print(password(length=16))
print(password(length=18))
print(password(length=20))

def non_leter_string(text):

    result = list(letter for letter in list(text) if letter in "1234567890")
    return "".join(result)

print(non_leter_string("lkjhdsflk hhd9f8u398ur rfohjf309r 9009rf xjjnk"))
