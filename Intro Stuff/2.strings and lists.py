#Strings and Lists

string01 = "Hello World"
string02 = 'I <3 Python'

#Accessing Values

print "string01[0]: ", string01[0]
print "string02[7:13]: ", string02[5:13]
print "string02 length: ", len(string02)
print "string02[-7:] = ", string02[-7:]

#replace values
string03 = string02.replace("I", "1")
print string03

#Lists

list01 = ['pt1', 'pt2', 'pt3', 'pt4']
print list01[2]
print list01[1:3]

print list01[-1]
 
 
#add to list

list01.append('pt5')

print list01


#remove from list

del list01[2]
print list01


#list length
print len(list01)

#iterate
for x in list01:
    print x

#membership test
print 'pt2' in list01
print 'pt3' in list01

