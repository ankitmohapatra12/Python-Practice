import re as r
# x=10
# if x<100:
#     print(x/0)
# else:
#     print(bool(x/1))

str = "wipro technologiese"
#      012345678.........
#print(str[-1:-18:-1])

#Reverse of string
#print(str[::-1])

# print(r.findall("ca*t","ct cat caat caaat caaaat"))

email = '''1	eric.lopez@gmail.com
2	eric.lund@gmail.com
3	eric.m.boehm@gmail.com
4	eric.mack@gmail.com
5	eric.mason@gmail.com
6	eric.mathews@gmail.com
7	eric.maynard@gmail.com
8	eric.mckinney@gmail.com
9	eric.meredith@gmail.com
10	eric.mintz@gmail.com
11	eric.mistry@gmail.com
12	eric.mittler@gmail.com
13	eric.moeller@gmail.com
14	eric.monica@gmail.com
15	eric.moore@gmail.com
16	eric.murrell@gmail.com
17	eric.nay@gmail.com
18	eric.neilson@gmail.com
19	eric.nelson@gmail.com
20	eric.newcomer@gmail.com
21	eric.nghiem@gmail.com
226t7g6g	eric.nishant@gmail.com
23	eric.noss@gmail.com
24	eric.nyberg@gmail.com
25	eric.o.neil@gmail.com
26	eric.odonnell@gmail.com
27ggtyvty	eric.ogren@gmail.com
28m8uh6tt	eric.olsen@gmail.com
29	eric.oosterhof@wipro3.com
30	eric.pace@gmail.com'''




file = '''
02-11-2020  21:53               182 addingelements.py
23-11-2020  13:30               286 addingTwoMatrices.py
24-11-2020  12:56               208 addSubtractMatrix.py
11-11-2020  20:15               188 anki.py
20-12-2020  21:01               215 avgOFnumbers.py
25-01-2021  23:27               306 bubbleSort.py
23-12-2020  11:54               160 candleheight.py
21-11-2020  15:16               323 checkBinaryString.py
21-11-2020  14:11               245 checkIfStringContainsSpecial.py
20-12-2020  19:39               717 CHECKifTwoMatricesEqual.py
19-11-2020  22:20               134 checksubstringpresentinlist.py
24-11-2020  21:38               220 compareTriplets.py
29-01-2021  08:50               148 countdigitEncode.py
29-01-2021  08:15               139 CounterTest.py
20-11-2020  11:10               284 CountMatchingCharacters.py
17-11-2020  14:11               242 CountOccurencesOfElement.py
23-12-2020  10:39               849 diagonalDiff.py
25-01-2021  23:07               353 distinctElements.py
02-11-2020  22:00                92 extendkeyworduse.py
24-11-2020  20:38               136 factorFun.py
12-11-2020  20:00                93 factorial.py
13-11-2020  19:22                 0 factorialusingforloop.py
19-11-2020  19:44               136 factrescusion.py
17-11-2020  12:30               373 FindNLargestlelement.py
16-11-2020  22:56               149 findsecondlargestelementinlist.py
16-11-2020  21:51                79 findsmallestinlist.py
26-09-2020  21:04                10 first.py
12-11-2020  20:34                43 forlop.py
22-10-2020  23:50                37 keywordlist.py
28-11-2020  19:52                25 ksdls.py
11-11-2020  20:03               240 leapyear.py
20-11-2020  14:15               218 leastFrequentString.py
16-12-2020  22:01               567 matrixdiagonaldifference.py
23-11-2020  19:21               222 matrixProduct.py
24-11-2020  23:00               142 maxAdjacentDifference.py
21-11-2020  14:00               179 maxFrequencyCharacter.py
23-12-2020  11:31               114 mimmaxsum.py
23-11-2020  13:43               338 MultiplyTwoMatrices.py
22-10-2020  23:48                57 myalias.py
29-01-2021  09:34               235 oddevengaamewipro.py
29-11-2020  10:19               100 pattern1.py
29-11-2020  10:32               117 pattern2.py
29-11-2020  11:08               119 pattern3.py
29-11-2020  11:14                94 pattern4.py
29-11-2020  12:25               144 pattern5.py
29-11-2020  12:26               161 pattern6.py
20-12-2020  18:55               231 positionInterchange.py
14-11-2020  21:21               377 primenumsum.py
19-11-2020  22:49               133 PrintevenlengthString.py
12-11-2020  20:17                46 printpatternwith1while.py
14-11-2020  22:26               134 printpythonseries.py
17-11-2020  14:26               246 programtodeleteDuplicates.py
16-11-2020  21:49               122 programtoexchangefirstandlastelement.py
21-11-2020  15:55               237 programToFindUncommonWords.py
21-11-2020  11:57             1,181 randomnumgenerator.py
26-11-2020  12:07               282 randomsample.py
20-11-2020  13:54               242 removingduplicatesfromstring.py
19-11-2020  22:09               129 removingithcharacterfromstring.py
29-01-2021  08:22               199 repeatingdigitsfreq.py
22-10-2020  23:16                74 Returnnothingfunctionnone.py
19-11-2020  21:52               114 reversewordsingivenstring.py
23-11-2020  13:04                87 rotateString.py
23-12-2020  11:20               107 sample.py
16-11-2020  21:29               216 SortByFrequency.py
16-11-2020  19:07                 0 sortingalgoSet1.py
21-11-2020  12:14               159 SplitStringJoin.py
19-11-2020  23:19               297 StringContainingVowels.py
19-11-2020  21:43               115 stringreversecheck.py
29-01-2021  09:14               352 sumadjacentdistance.py
29-01-2021  21:28               447 sumlarsmallprimenum.py
12-11-2020  20:03                96 sumofdigits.py
12-11-2020  19:57               114 sumofseries.py
11-02-2022  21:17             3,492 trainingWiproPython.py
24-11-2020  12:09               199 transposeOfMatrix.py
21-11-2020  14:25               216 wordsGreaterThanKlength.py'''

line =r.findall("[0-9-]+\s+[0-9:]+\s+([0-9,]+)+\s+([a-zA-Z._()]+)",file)

for sen in line:
    print(sen)

# print(r.findall("\w+[.]+\w+[@]+[a-zA-Z0-9]+[.]+com",email))
#lowercase
#print(str.lower())

#uppercase
#print(str.upper())


#print(str.title())



#count of a character
#print(str.count(' '))



#finding index of substring mentioned
# print(str.find('technologies'))
# 
# print(str.find('e'))




#print(str.rfind('e'))


# print(str.split(' '))




l = ["aaa","sdsrt","sddfdf"]

def descFun(val):
    return val[-1]

l.sort(key=descFun)
l.sort(key=len)

#incase of a tie in length original order is maintained

# print(l)







para = '''Paragraphs are the building blocks of papers.
        Many students define paragraphs in terms of length:
        a paragraph is a group of at least five sentences,
        a paragraph is half a page long, etc. In reality,
        though, the unity and coherence of ideas among sentences is what constitutes a paragraph.
        A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116).
        Length and appearance do not determine whether a section in a paper is a paragraph.
        For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long.
        Ultimately, a paragraph is a sentence or group of sentences that support one main idea.
        In this handout, we will refer to this as the “controlling idea,”
        because it controls what happens in the rest of the paragraph.'''


l = para.split()
dic = {}

for word in l:
    if word not in dic.keys():
        dic[word]=1
    else:
        dic[word]+=1
        
        
loi = list(dic.items()) 
def customSort(val):
    return val[-1]
            
loi.sort(key=customSort,reverse=True)
# print(loi[0:9])


# x = int(input())
# print(type(x))


# candidates = {"ankit":24,"ajay":36,"Alexa":55}
# print(candidates)
# 
# d = {k:"senior" if v>=30 else "junior" for k,v in candidates.items()}
# print(d)


pal= lambda word : "palindrone" if word==word[::-1] else "not palindrone"

low = ["kasak","boom","blb","dssdd"]
# 
# for word in low:
#     #print(word,":",pal(word))
    


# print({x:pal(x) for x in low})

# dic1={x:list(map(pal,low)) for x in low }
# print(dic1)

# 
# f =list(filter(lambda word:word==word[::-1],low))
# print(f)


print(dir(__builtins__))
    