###########################################
# DON'T TOUCH ANYTHING IN THIS FILE
###########################################
print('Thankyou for using PDFedit')
print('For more of my repositories go to https://github.com/marangoisa')
print('Importing libraries')
import PyPDF2 
import os
import time

#function
def obj(source_cod, pos_ini, start, end):
    pos_ini = source_cod.find(str(pos_ini),0)
    pos_ini = source_cod.find(str(start),pos_ini)
    pos_fini = source_cod.find(str(end), pos_ini)
    output=source_cod[pos_ini+len(start):pos_fini]
    return [output, pos_fini]
print('Reading input.txt')
time.sleep(1)
f = open(os.getcwd()+"\input.txt").read()
path=obj(source_cod=f,pos_ini='#',start="path=",end="#")[0].replace("\n","")
fileslist=obj(source_cod=f,pos_ini='#',start="files=[",end="]")[0].split("/")
output=obj(source_cod=f,pos_ini='#',start="output=",end="#")[0].replace("\n","")
pageslist=obj(source_cod=f,pos_ini='#',start="pages=[",end="]")[0].split('/')
# make pages list
files=[]
for i in fileslist:
    files.append(i.replace("\n",""))
              
pages=[]
for i in pageslist:
    if i.find('(')>-1:
        rng=i.replace('(','').replace(')','').replace("\n","").split(':')
        pgi=[range(int(rng[0]),int(rng[1]))]
    else:
        pgi=[int(i)]
    pages.append(pgi)
           
def rangeok(x1,x2):
    rng=list(range(x1,x2+1))
    return rng
   
for i in range(0,len(pages)):
    if type(pages[i][0]) is range:
        pages[i][0]=rangeok(min(pages[i][0]),(max(pages[i][0])+1))

for i in range(0,len(pages)):
    if type(pages[i][0]) is list:
        for j in range(0,len(pages[i][0])):
            pages[i][0][j]=pages[i][0][j]-1
    else:
        pages[i][0]=pages[i][0]-1
print('Reading PDFs')
time.sleep(1)
pdfs=list()
for i in files:
   pdfs.append(str(path+i+'.pdf'))

print('Merging PDFs')
time.sleep(1)
pdfMerger = PyPDF2.PdfFileWriter()  
for i in range(0,(len(pdfs))): 
    pdfi=PyPDF2.PdfFileReader(open(pdfs[i], 'rb'))
    if type(pages[i][0]) is list:
        for j in pages[i][0]:
            pdfMerger.addPage(pdfi.getPage(j))
    else:
        pdfMerger.addPage(pdfi.getPage(pages[i][0]))     
    
pdfMerger.write(open(path+output+'.pdf','wb'))
print('Done!')
print('PDF saved as:'+path+output+'.pdf')
time.sleep(3)
