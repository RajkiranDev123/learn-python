import os
# types of files

#  text files : .txt , .csv
#  binary files : .pdf , .mp3 , .png , .jpg , .mp4 etc


print("read and write operation")

# read

fil = open("./f1.txt", "r")

content = fil.read()
print(content)
fil.close()


# write
fil2 = open("./f2.txt", "w")
content2 = "5552"
fil2.write(content2)
print(content2)
fil2.close()


# with : no need to close manually

with open("./f3.txt","w") as file:
    cont="30"
    file.write(cont)

# append mode

with open("./f3.txt","a") as file2:
    cont2=" 31"
    file2.write(cont2)

    

