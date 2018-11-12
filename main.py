"""  Copyright 2018 BinaryGears

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. """

import os


print("*----------------------------------------------------------------*")
print("Please run this program in the directory you need to run git in.")

print("What would you like to do?  1:Clone 2:Branch 3:Status 4:Checkout")

commandOptionOne = int(input())

if commandOptionOne == 1:
    print("Please enter the http address for the repository you would like to clone: ")
    repoHttp = str(input())
    print("Is", repoHttp, "The correct address? : y or n")
    isCorrectAddress = str(input())
    if isCorrectAddress == "y":
        repoHttp = "git clone " + repoHttp
        os.system(repoHttp)
    else:
        exit()

elif commandOptionOne == 2:
    print("What do you want to do?  1:Create 2:Delete 3:Commit 4:Switch")
    commandOptionTwo = int(input())
    if commandOptionTwo == 1:
        print("What would you like the name of the branch to be?: ")
        branchNameCre = str(input())
        print("Is", branchNameCre, "correct? : y or n")
        isCorrectNameCre = str(input())
        if isCorrectNameCre == "y":
            branchNameCre = "git branch " + branchNameCre
            os.system(branchNameCre)
        else:
            exit()
    elif commandOptionTwo == 2:
        print("What branch would you like to delete?: ")
        branchNameDel = str(input())
        print("is", branchNameDel, "correct? : y or n")
        isCorrectNameDel = str(input())
        if isCorrectNameDel == "y":
            branchNameDel = "git branch -d " + branchNameDel
            os.system(branchNameDel)
        else:
            exit()
