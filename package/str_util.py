

def str_reverse(string):
    return string[::-1]

def substr(string, x, y):
    return string[x:y+1]

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("123456789", 1, 2))