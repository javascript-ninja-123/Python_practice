
def log(x):
    print(x)

def isogram(str):
    a = list(map(lambda a:a.lower(), str.split()))
    b = [];
    for ele in a:
        for x in ele:
            b.append(x);
    return len(b) == len(set(b))


log(
    isogram("Algorism")
)
log(
    isogram("PasSword")
)

log(
    isogram("Consecutive")
)


# one word = 4 letters
# two words  = 2 letters from each
# three words = first letter from 2 and first 2 letters from the last
# four wrods = first letters from each of them


def letterLoop(str,num):
    b="";
    for x in str:
        b+=x[:num]
    return b;


def birdCodes(str):
    str = str.split();
    result ='';
    if len(str) == 1:result = str[0][:4]
    if len(str) == 2:result = str[0][:2] + str[1][:2]
    if len(str) == 3:result = str[0][:1] + str[1][:1] + str[2][:2]
    if len(str) == 4:result = str[0][:1] + str[1][:1] + str[2][:1]
    return ["".join(result).upper()];

log(
    birdCodes("American White Pelicam")
)

def cumulativeListSum(arr):
    array = [];
    for i in range(0,len(arr)):
        if i == 0: array.append(arr[i])
        else:array.append(sum(arr[:i +1]))
    return array;

log(
    cumulativeListSum([3,3,-2,408,3,3])
)


def wordCount(text):
    return len(text.split())

log(
    wordCount("This is a test")
)



student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]


from operator import itemgetter, attrgetter, methodcaller

log(
    sorted(student_tuples, key=itemgetter(2), reverse=True)
)




def findingMissingNumber(List):
    for n in range(1,11):
        if not n in List:
            return n

log(
    findingMissingNumber([7, 2, 3, 6, 5, 9, 1, 4, 8])
)



def findTheFirstNonRepeatedCharacter(txt):
    array = [];
    final = None;
    if txt == '': return False;
    if len(txt) == 1: return txt;
    else:
        for string in txt:
            for letter in string:
                array.append(letter);
        for a in array:
            if array.count(a) == 1:
                final= a;
                break;
    return final;



log(
    findTheFirstNonRepeatedCharacter('the quick brown fox jumps then quickly blows air')
)


def pracitceFunc(txt):
    txt = txt.replace(' ','')
    for i in range(len(txt)):
        if txt.count(txt[i]) == 1: return txt[i];
    else:
        return False;



log(
    pracitceFunc("the quick brown fox jumps then quickly blows air")
)

import operator
def SecondAndFirst(List):
    newList = list(map(lambda x:x.lower(), List));
    firstSet = sorted(newList[0])
    secondSet =sorted(newList[1])
    for letter in secondSet:
        if not operator.contains(firstSet, letter):return False;
    else: return True;


log(
    SecondAndFirst(["trances", "nectar"])
)

print("======")

def phoneNumber(txt):
    txt = txt.replace(' ','');
    num = '1234567890'
    if not txt[0] == "(" and txt[4] == ")": return False;
    if not operator.contains(num,txt[1:4]): return False;
    if not operator.contains(num,txt[5:8]): return False;
    if not txt[8] == '-': return False;
    if not operator.contains(num,txt[9:]): return False;
    else: return True;
    return True;


log(
    phoneNumber("1111)555 2345")
)


"(111)555-2345"

def phoneNumber(string):
    string = string.replace(' ','');
    braket = string[0] + string[4];
    digit1 = string[1:4];
    digit2 = string[5:8];
    tag = string[8];
    digit3 = string[9:];
    numbers = digit1 + digit2 + digit3;
    if not numbers.isdigit(): return False;
    if not braket == '()': return False;
    if not tag == '-': return False;
    else: return True;


log(
    phoneNumber("(111)555-2345")
)
