# BasicPdfEditor
Short script intended to help anyone that want to add or subtract pages from a PDF file, without using a website that might compromise the confidentiality of the document.
You only need to modify 4 lines:
- line 4: path where the file or files to be modify are e.g. 'C:/Users/xxxx/Desktop/xxxx/'
- line 6: names of the pdf files e.g. 'f1','f2','f3'
- line 8: name modified file e.g. output='output'
- line 10: pages, in order, that must be in the modified document. Page numbers should be in order separated by commas, pages of each document are between brackets, use function range to add all pages in an interval, the order should fallow the file names order as in the example bellow:
Example: 
Add: page 2 from file f1.pdf, page 1 from file f2.pdf, and pages 1 to 3 from file f3.pdf. All pdfs are in the folder C:/Users/xxx/yy/ is named output1st
Modify the lines 4, 6, 8, and 10 as follows:
line 4: path='C:/Users/xxx/yy/'
line 6: files=['f1','f2','f3']
line 8: output='output1st'
line 10: pages=[[2],[1],[range(1,3)]]
