print('hello world');
print('what is up');

firstNumber = 50+50;
print(firstNumber);

a = 5;
print(a);

a = 10;
print(a);


print(type(a));
a = 'yes';
print(type(a));


a = [1,2,3,4,5];
print(type(a));

b = "hello";
c = "this is also a string";

print(c);
print(len(c));


mystring = 'abcdefghijk';
print(mystring[2:]);
print(mystring[:3]);
print(mystring[3:6]);
print(mystring[1:3]);
print(mystring[1::2])
print(mystring[2:7:2]);
print(mystring[::-1]);



name = "Sam";

print(name);

last_letter = name[1:];
newName = "P" + last_letter;
print(newName)





x = 'Hello world';
x = x.upper();
print(x);
newX = x.lower().split();
print(newX);

print("This is a string {}".format("INSERTED"))



print("The {0} {1} {0}".format("yes","horray"))


print("Yes {a} {b} {c}".format(a = 'yes', b="ss", c ="waa"))


result = 100/7;
print("The result was {r:1.3f}".format(r = result))
print("The result was {r:1.2f}".format(r = result))
name = 'yes';
# print(f"hello my name is {name}");



myList = [1,2,3,4];
anotherList = ["String",1,2];

print(myList[::-1])


hey = myList + anotherList;
print(hey);
hey[0] = "ONe ALl CAPS";

print(hey);
hey.append("six");
print(hey);
hey.pop();
print(hey);

poppedItem = hey.pop();
print(poppedItem);
hey.pop(0);

print(hey);
a = [1,2,3,4,5,6,7,0,34,2];
b = ["a","b","c","d","e"];

a.sort();
print(a);


mydic = {"key":"value","key2":"vlaue2","key3":["a","b"]};
print(mydic["key3"][0].upper())



price_lookup = {"apple":2.99, "orange":1.99, "milk":5.80};
print(price_lookup["apple"])

price_lookup2 = {"k1":123, "k2":[0,1,2],"k3":{"insideKey":100}};
price_lookup2["k3"]["insideKey"] = 400;
print(price_lookup2.keys())
print(price_lookup2.values())
print(price_lookup2.items())
print(price_lookup2.items())


t = (1,2,3,2,2);
myList = [1,2,3];


print(type(t))
print(type(myList))
print(t[0])
print(t[1:])
print(t.index(1))
print(t.count(2));
name = 'aas'
print(f"my name is {name}");


myset = set();

myset.add(1);
myset.add(2);
myset.add(3);
mylist = [1,2,3,4,5,5,5];

myset = set(mylist);


print(myset);



mylist = [1,2,3,4,5,6,6,7,7,7,7,7,7];
myset = set(mylist);
print(myset);

print(True);
print(False);

print(1 == 1);
b = None;
print(b);

# myfile= open('/Users/Sung/desktop/python/file.txt')
# contents= myfile.read()
# print (contents)
# myfile.seek(0);
# contents= myfile.readlines()
# print (contents)
# myfile.close();


# yesss
# with open('file.txt') as myFile:
#     contents = myFile.read();
#
#
# with open("file.txt",mode="a") as f:
#     f.write("\nFour on Fourth")
#
# with open('file.txt') as myFile:
#     contents = myFile.read();
#
# with open('adsfads.txt', mode="w") as f:
#     f.write("I created this file")

with open('adsfads.txt', mode="r") as f:
    contents = f.readlines();
    print(contents)



print(2 == 2);
print("hello" == "hello");
print("2" == 2);
print(2.0 == 2);



print(1 < 2 or False);
print("h" == "h" and "v" == "v");

print(not 1 == 1);



if not True:
    print("it is true");
else:
    print("it is not true")

loc = 'Bank';

if loc == 'Autoshop':
    print("Cars are cool");
elif loc == 'Bank':
    print("money is cool");
else:
    print("I will not go anywhere");


myList = [1,2,3,4,5,6,7,8,9];
for num in myList:
    print(num + 1);


for jelly in myList:
    if(jelly % 2 == 0):
        print(jelly);
    else:
        print(f"odd {jelly}");


list_sum = 0;

for num in myList:
    list_sum += num;

print(list_sum);

for _ in "helloWorld":
    print("Cool")

tup = (1,2,3,4,5);

for ele in tup:
    print(ele);


myList = [(1,2),(3,4),(5,6)];
print(len(myList));

for a,b in myList:
    print(a)
    print(b)

d = {"k1":1,"k2":2,"k3":3};
c = {};
for key,value in d.items():
    value = value + 2;
    c[key] = value;

print(c);


x = 0;
while x < 5:
    print(f'the current value of x is {x}')
    x +=1;
else:
    print("X is not less then 5")


x = [1,2,3];

for item in x:
    if item == 2:
        break;
    else:
        print("it is odd");



for num in range(1,10,2):
    print(num);

# list = list(range(1,10))

#
# list = list(range(1,20))

print(list)


index_count = 0;
word = 'abcde'
for _ in word:
    print(f'At index {index_count} the letter is {word[index_count]}');
    index_count +=1;


for index,letter in enumerate(word):
    print(index)
    print(letter)


myList1 = [1,2,3,4];
myList2 = ["a","b","c","d"];

for item in zip(myList1,myList2):
    print(item);

a = list(zip(myList1,myList2))

print(a)


print("x" in [1,2,3])

d = {"mykey":5};
print(d.values())
print(5 in d.values())

print(min(myList1))
print(max(myList1))

from random import shuffle
from random import randint
myList = [3,4,5,6,7,8,9]
shuffle(myList)
print(myList)
print(randint(0,100))




myString = 'hello';

myList = [letter for letter in myString];
print(myList);


myList =[x for x in 'words']
print(myList)


myList = [num**2 for num in range(1,19)]

print(myList)


myList = [num for num in range(0,11) if num % 2 == 0]
print(myList)



celcius = [0,10,20,34,5]

fahrenhet= [((9/5)*temp + 32) for temp in celcius];
print(fahrenhet)


fahrenhet = [];

for temp in celcius:
    fahrenhet.append((9/5)*temp +32)

def log(x):
        print(x);


log(fahrenhet);


myList = []
for x in [1,2,3,4]:
    for y in [200,300,400,500]:
        myList.append(x *y)

log(myList)


list = [1,2,3,4,5,6,7];
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

again = [{name:v['name']} for v in west];

log(again)



doit = [v["age"] for v in west]

log(doit)
