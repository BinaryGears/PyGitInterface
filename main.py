import os


print("*----------------------------------------------------------------*")
print("Please run this program in the directory you need to run git in.")

print("What would you like to do?  1:Clone 2:Branch 3:Status 4:Checkout")

commandOptionOne = int(input())

if commandOptionOne == 1:
    print("Please enter the http address for the repository you would like to clone: ")
    repoHttp = str(input())
    print("Is", repoHttp, "The correct address? : Y or N")
    isCorrectAddress = str(input())
    if isCorrectAddress == "Y":
        repoHttp = "git clone " + repoHttp
        os.system(repoHttp)
    else:
        exit()

elif commandOptionOne == 2:
    print("What do you want to do?  1:Create 2:Delete 3:Commit 4:Switch")
    commandOptionTwo = int(input())
    if commandOptionTwo == 1:
        print("What would you like the name of the branch to be?: ")
        branchName = str(input())
        print("Is", branchName, "correct? : Y or N")
        isCorrectName = str(input())
        if isCorrectName == "Y":
            branchName = "git branch " + branchName
            os.system(branchName)
        else:
            exit()
