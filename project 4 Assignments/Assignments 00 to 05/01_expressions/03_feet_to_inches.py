# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


INCHES_IN_FOOT: int = 12
def main():
    feet:int=int(input("Enter the number of feets "))
    inches:int=feet * INCHES_IN_FOOT
    print(f"{feet} feet is {inches} inches")
    
if __name__=="__main__":
 main()