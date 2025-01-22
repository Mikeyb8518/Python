# write a program that asks the userfor the name of the file they want to open
# program should only displat the first 5 lines of the file if less display the entire file

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    count = 0
    while count <= 4:
        if line == '' :
            count += 5
        else:
            print(line)
            line = object_file.readline()
            line = line.rstrip('\n')
            count += 1
    object_file.close()
def main():
    read()

main()