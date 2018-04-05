def log(x):
    print(x);

letter = "hello";
log(letter[::-1]);




def createNewLetter(new,old):
    return new+old;


new = "P";
old = letter[1:]

newWord = createNewLetter(new,old).upper()

log(f"this is a new word {newWord}")

newList = [1,2,3,4,5,6,7,8,9,9];
a = newList.pop()
newList.append(10)
log(a)
log(newList)


west = [3,4,5,2,1,3,4]
west.sort();
log(west)



dictianire = {
    "key1":"value",
    "key2":"value",
    "key3":"value"
    }

log(dictianire.keys())
log(dictianire.values())
socks = dictianire.items()

def Value(list):
    return [x for x in list.values()]

log(Value(dictianire))


t = (1,1,11,2,2,3,4,5);
log(t.index(1))
log(t.count(2))


newSet = set();
newSet.add(1)
newSet = set([1,1,1,1,1,2,2,2,2,4,4,4])
log(newSet)



myList = [(1,3),(2,3),(4,5)]
for a,b in myList:
    print(a)

myList = [x+2 for x in range(1,20)]

log(myList)


word = 'hello'
for index,letter in enumerate(word):
    print(index)
    print(letter)


myList = [1,2,3];
myList2=["a","b","c"]

myNewList = list(zip(myList,myList2))

log(myNewList)


west = [
    {
        "name":"sung",
        "age":22,
        "job":"developer"
    },
    {
        "name":"yonna",
        "age":21,
        "job":"designer"
    }
];

again = [v['name'] for v in west];

log(again)



def required():
    print("argument is requred")


def name_function(name =required()):
    print(f"Hello world {name}")
    return True




result = name_function("Sungmin Yi");


if(result):
    log("sup")


def dogCheck(string):
    return "dog" in string.lower();



import operator
def dogCheck2(mystring):
    return operator.contains(mystring.lower(),"dog");


log(dogCheck2("Dogis here"))
log(dogCheck("dogis here"))



def catCheck(str):
    return operator.contains(str.lower(),str);

def catCheck2(str):
    return "cat" in str.lower();

log(catCheck("cat is here"))

def isRequired():
    return None;


def pigLatin(str):
    vowel ='aieou'
    loweredStr = str.lower();
    first_letter = loweredStr[0]
    rest_letters = loweredStr[1:]
    if operator.contains(vowel,first_letter):
         str = ("{r}ay").format(r=loweredStr);
    else:
        str= ("{r}{a}ay").format(r =rest_letters,a=first_letter)
    return str;


log(pigLatin("apple"))



def myFunc(*args):
    #returns 5% of the sum of A and B
    return sum(args) * 0.05;

log(
    myFunc(20,50)
)

def myFunc2(**kwargs):
    if "fruit" in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not see anything")


myFunc2(fruit="apple",veggie="lettuce")



def myFunc3(*args,**kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myFunc3(10,20,30,50,fruit='orange', food='egg')




def firstAndForth(str):
    firstHalf = str[:3].capitalize();
    secondHalf = str[3:].capitalize();
    return firstHalf+secondHalf




log(
    firstAndForth("macdonald")
)

def reverse(text):
    reversedArray = text.split()[::-1]
    return " ".join(reversedArray)


log(
    reverse("I am home")
)


def AmlostThere(num):
    return (abs(100-num) <=10) or (abs(200-num) <=10);


log(
    AmlostThere(104)
)


def getThreeFunc(index,item):
    return index * item;


print("=======")


def has_33(nums):
    for i in range(0,(len(nums)-1)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True;
    return False;





log(
    has_33([1,2,3,3])
)





def parseDoll(str):
    result = ""
    for char in str:
        result += char * 3;
    return result


log(
    parseDoll("Hello")
)


def blackJack(*args):
    result = sum(args);
    if result <=21:
        return result;
    elif 11 in args and result <=31:
        return result - 10;
    else:
        return "BUST"


log(
    blackJack(9,9,9)
)


def summer_69(arr):
    if not 6 in arr:
        return sum(arr);
    elif 6 in arr and 9 in arr:
        index1 = arr.index(6);
        index2 = arr.index(9);
        return sum(arr[0:index1]) + sum(arr[index2 +1:])



log(
    summer_69([2,1,6,9,11])
)


def spyGame(arr):
    codeList = [];
    for num in arr:
        if num == 0:
            codeList.append(num);
        elif num == 7:
            codeList.append(num);
    return  sum(codeList) == 7 and sum(codeList[0:2]) == 0;

log(
    spyGame([1,2,4,0,0,7,5])
)



def count_prime(num):
    numList = [];
    for i in range(0,num):
        if i < 2:
            continue;
        elif i % 2 == 0:
            print(i)
            numList.append(i);
        else:
            continue;
    return len(numList);


log(
    count_prime(100)
)


def square(num):
    return num **2;

newList = list(map(square,[1,2,3,4,5]));

log(
    newList
)



def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "Even";
    else:
        return mystring[0];


log(
    list(map(splicer,["Andy","Eve","Sally"]))
)


def checkEven(num):
    return num % 2 ==0;

log(
    list(filter(checkEven,[1,2,3,4,5,6,7]))
)


square = lambda num : num**2;



log(
    list(map(lambda str : str[0],["Andy","Sandy"]))
)

# lambda num : num **2
name = "This is A GlobalString"
getData = 'ss'


def greet():
    return lambda name: 'Hello {a} {b}'.format(a=name, b= getData);

log(
    greet()('Sung')
);


x= 50;
def func():
    print(f"x is {x}")
    x= "New Value";
    print(f"x is {x}")




from functools import partial

def add(*args):
    return sum(args);

add_10 = partial(add,10)
add_20 = partial(add,20)

log(
    add_20(1,2,3)
)


from inspect import signature
from functools import reduce



newList = [1,2,3,4,5]

def compose(*fns):
    def inner(x):
        return reduce(
            lambda acc,fn : fn(acc),
            fns,
            x
        )
    return inner;

def square(list):
    return map(lambda num: num**2, list)
def checkEven(list):
    return filter(lambda num: num % 2== 0, list)
def addNumber(list):
    return map(lambda num: num+4, list)

result = list(compose(
 square,
 checkEven,
 addNumber
)(newList))

log(
    result
)

def range_check(num):
    def inner(low,high):
        if num in range(low,high):
            print(f"{num} is in the raunge");
        else:
            print(f'{num} is not in the range');
    return inner;

w = range_check(5)
w(1,10)
