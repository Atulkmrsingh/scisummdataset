import glob
import string
import pandas as pd
import csv
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
def convert_data_to_csv():
  path="top1000_complete"
  train_x=[]
  x=0
  y=0
  train_y=[]
  c=glob.glob(path+'/*')
  for i in c:
    p=glob.glob(i+'/Documents_xml/*')
    fp=open(p[0],'r',encoding='utf-8')
    c=str(fp.read())
    text = re.sub('<[^<]+>', "",c)
    text=str(text).strip('\n')
    # startingSent=find_between( text, "\n", "\n" )
    # print(startingSent)
    mystr = text.split(sep='\n')
    heading=mystr[0]
    text =[''.join(mystr[1 : ])][0]
    print(text)
    mx=text.split()
    if(len(mx)>x):
      x=len(mx)
    print("heading is",heading)      
    train_x.append(text)
    fp.close()
    q=glob.glob(i+'/summary/*')
    fq=open(q[0],'r',encoding='utf-8')
    cp=str(fq.read())
    fq.close()
    my=cp.split()
    if(len(my)>y):
      y=len(my)
    train_y.append(cp)
    break
  df = pd.DataFrame({'Paper':train_x, 'Summary':train_y})
  # df.to_csv('data.csv', index=False)
  # with open('data.csv', 'w', newline='',encoding='utf-8') as csvfile:
  #   fieldnames = ['paper', 'summary']
  #   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  #   writer.writeheader()
  #   for i, j in zip(train_x, train_y):
  #       writer.writerow({'paper': i, 'summary': j})
  
  print(len(train_x))
  print(len(train_y))
  return df
convert_data_to_csv()