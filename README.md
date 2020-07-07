# BasicPdfEditor
Short script intended to help anyone that want to add or subtract pages from a PDF file, without using a website that might compromise the confidentiality of the document.

## First
Install PyPDF2 library in 2 steps:
1- In the command prompt go to your python scripts
    cd C:\xxxxx\xxxx\xxxx\Python38\Scripts
2- Install PyPDF2
    pip install PyPDF2

## Now you can use BasiPdfEditor
You only need to modify input.txt
- path:where the file or files to be modify are e.g. 'C:/Users/xxxx/Desktop/xxxx/'
- files: pdf file names separeted by / e.g. f1/f2/f3
- output: name of the new pdf e.g. output='output'
- pages: pages, of each file, to include in the output, this has to be done in order. Page numbers should be in order separated by /, pages of each document are between parentheses, use : to add all pages in an interval (e.g. 2, to 9 is 2:9), the order should fallow the file names order as in the example bellow:
Example: 
Add: page 2 from file f1.pdf, page 1 from file f2.pdf, and pages 1 to 3 from file f3.pdf. All pdfs are in the folder C:/Users/xxx/yy/ is named output1st
Modify input.txt as follows:
path=C:/Users/xxx/yy/
files=[
f1/
f2/
f3]
output=output1st
pages=[
2/
1/
(1:3)]
