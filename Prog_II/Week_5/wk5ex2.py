#wk5ex2.py

def num_to_base_b(n, b):
    """num_to_base_b neemt int n en int b. en geeft n in grondtal b terug.
    als b 2 is zal dit een binair getal geven, bij b == 10 een 'gewoon'getal en alles daartussen in
    Args:
        n (int): niet negatief getal
        b (int): getal 2 tot 10

    """
    if n < 0:
        return
    if n == 0:
        return ''
    else:
        c = n % b
        n -= c
        return num_to_base_b(n//b, b) + str(int(c))
        
assert num_to_base_b(3116, 9) == '4242'
assert num_to_base_b(141474, 8) == '424242'
assert num_to_base_b(42, 8) == '52'
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(42, 10) == '42'
assert num_to_base_b(42, 2) == '101010'
assert num_to_base_b(4, 2) == '100'
assert num_to_base_b(4, 3) == '11'
assert num_to_base_b(4, 4) == '10'
assert num_to_base_b(0, 4) == ''
assert num_to_base_b(0, 2) == ''
assert num_to_base_b(-10,3) == None


def base_b_to_num(s, b):
    """base_b_to_num neemt string s en base nummer b en geeft grondtal 10 terug

    Args:
        s (string): string met getallen
        b (int): base nummer, tussen 2 en 10

    Returns:
        int: het nummer met grondtal 10
    """
    if s == '':
        return 0
    else:
        last_int = int(s[-1]) 
        return base_b_to_num(s[:-1], b) * b + last_int

 
assert base_b_to_num("5733", 9) == 4242
assert base_b_to_num("1474462", 8) == 424242
assert base_b_to_num("222", 4) == 42
assert base_b_to_num("101010", 2) == 42
assert base_b_to_num("101010", 3) == 273
assert base_b_to_num("101010", 10) == 101010
assert base_b_to_num("11", 2) == 3
assert base_b_to_num("11", 3) == 4
assert base_b_to_num("11", 10) == 11
assert base_b_to_num("", 10) == 0
#return num_to_binary(n/2) + '0'


def base_to_base(b1, b2, s_in_b1):
    """base_to_base neemt string van base b1 en geeft die string terug in base b2

    Args:
        b1 (int): base tussen 2 en 10
        b2 (int): base tussen 2 en 10
        s_in_b1 (string): string in b1
    """
    return num_to_base_b(base_b_to_num(s_in_b1, b1), b2)

assert base_to_base(2, 10, "11") == '3'
assert base_to_base(10, 2, "3") == '11'
assert base_to_base(3, 5, "11") == '4'
assert base_to_base(2, 3, "101010") == '1120'
assert base_to_base(2, 4, "101010") == '222'
assert base_to_base(2, 10, "101010") == '42'
assert base_to_base(5, 2, "4321") == '1001001010'
assert base_to_base(2, 5, "1001001010") == '4321'


def add(s, t):
    """add neemt 2 binaire strings en geeft hun som terug in base 2

    Args:
        s (string): binaire string 1
        t (string): binaire string 2
    """
    return num_to_base_b(base_b_to_num(s, 2) + base_b_to_num(t, 2), 2)

assert add("11", "1") == '100'
assert add("11", "100") == '111'
assert add("110", "11") == '1001'
assert add("11100", "11110") == '111010'
assert add("10101", "10101") == '101010'


def add_b(s, t):
    """add_b neemt 2 binaire strings en geeft de som hiervan terug via een carry


    Args:
        s (string): binaire string 1
        t (string): binaire string 2
    """
    if s == '' and t != '':
        return t 
    elif s != '' and t == '':
        return s
    
    if s[-1] == '1' and t[-1] == '1':
        carry = add_b('1', s[:-1])
        return add_b(carry, t[:-1]) + '0'
    elif s[-1] == '1' or t[-1] == '1':
        return add_b(s[:-1], t[:-1]) + '1'
    else:
        return add_b(s[:-1], t[:-1]) + '0'

assert add_b("11100", "11110") == '111010'
assert add_b("10101", "10101") == '101010'
assert add_b("11", "1") == '100'
assert add_b("11", "100") == '111'
assert add_b("110", "11") == "1001"
assert add_b("1", "1") == "10"
assert add_b("110101010", "11111111") == "1010101001"


def compress(s):
    """compress neemt string s die binaire getallen bevat en geeft een compressie terug

    Args:
        s (string): binaire string
    """
    if len(s) > 64:
        print('string te lang')
        return None
    if s == '':
        return ''
    counter = 0
    for x in s:
        if x == s[0]:
            counter += 1
        else:
            break
    onePart = s[0] * counter
    s = s.replace(onePart, '', 1)
    return splitString(onePart) + compress(s)
    
def splitString(s):
    """splitString functie die delen van compress accepteerd en een compressie teruggeeft

    Args:
        s (string): een deel van de compressie string
    """
    counter = 0
    b = s[0]
    for x in s:
        if x == b:
            counter += 1
        else:
            break
    nullen = 7 - len(num_to_base_b(counter, 2))
    return b + '0' * nullen + num_to_base_b(counter, 2)


def uncompress(s):
    """uncompress neemt een binaire string die geconversed is en maakt dit 'ongedaan'

    Args:
        s (string): de binaire gecompressede string
    """
    if s == '':
        return ''
    else:
        return uncompressHelp(s[0:8]) + uncompress(s[8:])


def uncompressHelp(s):
    """uncompressHelp krijgt een 8 bit string en rekend dit tot een uncompressede string

    Args:
        s (string): string van 8 bits.
    """
    b = s[0]
    s = s.replace(b, '', 1)
    return base_b_to_num(s, 2) * b


assert compress(64 * "0") == '01000000'
assert uncompress("10000101") == '11111'
assert compress("11111") == '10000101'
assert compress("0" * 16 + "1" * 16 + "0" * 16 + "1" * 16) == '00010000100100000001000010010000'
assert uncompress("00010000100100000001000010010000") == '0000000000000000111111111111111100000000000000001111111111111111'