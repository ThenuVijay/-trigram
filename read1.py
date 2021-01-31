import nltk
from nltk.util import ngrams
from collections import Counter
import re
import csv
import bs4 as bs
import urllib.request

def fileread(file):
    content = bs.BeautifulSoup(file, 'lxml')
    paragraphs = content.find_all('p')
    text= ''
    for para in paragraphs:
        text += para.text
    return text


def SpecialCharacterRemoval(content):
   
    result =  re.sub(r"[”“’‘•``[['(',')'—@\'?\'-.:*//!/;$%=–]", " ", content)
    result1 = re.sub(r"[0-9A-Za-z_]"," ",result)
    result1 = result1.replace(']',r"")
    return(result1)
    


def writefile(num,Out):
    res="result"+str(num)+"."+"csv"
    print(res)
    with open(res, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        data3=''
        for i in Out:
            (data1,data2)=i
            for j in range(0,num):
               file.write(str(data1[j])+'\t')          
            file.write(str(data2))
            file.write('\n')
    file.close()            


    
def Findgrams(file,num):
    d=SpecialCharacterRemoval(file)
    token = nltk.word_tokenize(d)
    Ngrams= ngrams(token,num)
    Out=Counter(Ngrams)
    Max_Out=Out.most_common(500)
    return Max_Out
    
    
    
def Findgrams1(file,num):
    d=Findgrams(file,num)
    writefile(num,d)
        
