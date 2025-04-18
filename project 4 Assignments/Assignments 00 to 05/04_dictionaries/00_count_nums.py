# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.




def get_nums():
    nums=[]
    while True:
        num_input=input("Enter a number: ")
        if num_input=="":
            break
        nums.append(int(num_input))
    return nums

def count_nums(nums_list):
    num_dict={}
    for num in nums_list:
        if num in nums_list:
            num_dict[num]=1
        else:
            num_dict[num]+=1
    return num_dict
def print_nums(num_dict):
    for num in num_dict:
        print(str(num) +" appears " + str(num_dict[num]) + " times ")
def main():
    nums=get_nums()
    num_dict=count_nums(nums)
    print_nums(num_dict)
if __name__=="__main__":
    main()




   
        
