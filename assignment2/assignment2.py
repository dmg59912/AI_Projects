

def main():
    print("Setting up basic maze")

    f = open("smallMaze.lay","r")

    #reading whole file 
    print(f.read())
    f.close()

    print('\n\n')
    #reading in a loop
    f = open("smallMaze.lay","r")

    for x in f:
        print(x,end='')
    f.close()

    #get the lenght of the data 
    f = open("smallMaze.lay","r")
    data = f.read()
    len_char = len(data)
    print(len_char)
    f.close()

    #adding to a matrix 
    #game_board = []
    f = open("smallMaze.lay","r")
    line = f.readline()
    while line:
        for x in line:
            print(x,end='')



  


###############################################
if __name__ == '__main__':
    main()