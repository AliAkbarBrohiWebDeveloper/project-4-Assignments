# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def main():
    num=int(input("Enter a number: "))
    result=subtract_seven(num)
    print(f"The result is {result}")

def subtract_seven(num:int)->int:
    return num-7

if __name__=="__main__":
    main()
    



