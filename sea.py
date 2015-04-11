
b=open('fd.txt','r')
c=str(b.read())
d=raw_input('enter word what do u want to search')
if c.find(d):
    print "location" 
      
else:
    print ' no word in file'
      
      

