#files_io

#open for reading
myfile = open("/tmp/hello.txt", mode="r")

#print myfile.read()

#looping over file object
for line in myfile:
    print line

#open for appending
# myfile = open("/tmp/hello.txt", mode="a")
# myfile.write("hello world")
#
# myfile.close()
