# print triangle using nested loop
# Output - 
# *
# * *
# * * *
# * * * *

def DisplayPattern():
    i = 1
    while i <= 4:
        print()
        for no in range(i):
            print("*", end=" ")
        i = i + 1

def main():
    DisplayPattern()
    
if __name__ == "__main__":
    main()