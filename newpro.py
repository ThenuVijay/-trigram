import read1 as re

file=open(r'C:\\Users\\User\\Desktop\\python practice\\result.txt',encoding="utf-8") 
content = file.read()
file.close()


#re.Findgrams1(content,1)
re.Findgrams1(content,2)
re.Findgrams1(content,3)



