##########################################
# ONLY MODIFY THIS!!!!
#path to the folder with files
path='C:/Users/maran/Desktop/expPDF/'
# name of input files
files=['f1','f2','f3']
# Name of the output files
output='output'
# Pages of input files
pages=[[2],[1],[range(1,3)]]

###########################################
# DON'T TOUCH ANYTHING BELLOW THIS LINE
###########################################
import PyPDF2 

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

pdfs=list()
for i in files:
   pdfs.append(str(path+i+'.pdf'))
    
pdfMerger = PyPDF2.PdfFileWriter()  
for i in range(0,(len(pdfs))): 
    pdfi=PyPDF2.PdfFileReader(open(pdfs[i], 'rb'))
    if type(pages[i][0]) is list:
        for j in pages[i][0]:
            pdfMerger.addPage(pdfi.getPage(j))
    else:
        pdfMerger.addPage(pdfi.getPage(pages[i][0]))     
        
pdfMerger.write(open(path+output+'.pdf','wb'))
