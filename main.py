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

def py_interface_branch_create():
    print("What would you like the name of the branch to be?: ")
    branchNameCre = str(input())
    print("Is", branchNameCre, "correct? : y or n")
    isCorrectNameCre = str(input())
    if isCorrectNameCre == "y":
        branchNameCre = "git branch " + branchNameCre
        os.system(branchNameCre)
        py_interface_branch()
    else:
        py_interface_branch()

def py_interface_branch_delete():
    print("What branch would you like to delete?: ")
    branchNameDel = str(input())
    print("is", branchNameDel, "correct? : y or n")
    isCorrectNameDel = str(input())
    if isCorrectNameDel == "y":
        branchNameDel = "git branch -d " + branchNameDel
        os.system(branchNameDel)
        py_interface_branch()
    else:
        py_interface_branch()

def py_interface_branch_checkout():
    print("What branch would you like to go into?: ")
    checkoutBranch = str(input())
    checkoutBranch = "git checkout " + checkoutBranch
    os.system(checkoutBranch)
    py_interface_branch()

def py_interface_branch_status():
    os.system("git status")
    py_interface_branch()

def py_interface_branch_add():
    os.system("git status")
    print("What would you like to add?: ")
    gitAdd = str(input())
    gitAdd = "git add " + gitAdd
    os.system(gitAdd)
    py_interface_branch()


def py_interface_branch_commit():
    print("Please add a comment to your commit: ")
    commitComment = str(input())
    commitComment = "git commit -m " + commitComment
    os.system(commitComment)
    py_interface_branch()

def py_interface_branch_push():
    print("Please enter the branch name: ")
    branchName = str(input())
    branchName = "git push origin " + branchName
    os.system(branchName)
    py_interface_branch()

def py_interface_clone():
    print("Please enter the http address for the repository you would like to clone: ")
    repoHttp = str(input())
    print("Is", repoHttp, "The correct address? : y or n")
    isCorrectAddress = str(input())
    if isCorrectAddress == "y":
        repoHttp = "git clone " + repoHttp
        os.system(repoHttp)
    else:
        py_interface_start()

def py_interface_start():
    print("What would you like to do?  1:Clone Repository 2:Branch Maintenance 3:Quit")
    commandOptionOne = None
    try:
        commandOptionOne = int(input())
    except ValueError:
        commandOptionOne = 4
    if commandOptionOne == 1:
        py_interface_clone()
    elif commandOptionOne == 2:
        py_interface_branch()
    elif commandOptionOne == 3:
        quit()
    elif commandOptionOne == 4:
        py_interface_start()
    else:
        py_interface_start()

def py_interface_branch():
    print("What do you want to do?  1:Create 2:Delete 3:Checkout 4:Status 5:Add 6:Commit 7:Push 8:Go Back")
    commandOptionTwo = None
    try:
        commandOptionTwo = int(input())
    except ValueError:
        commandOptionTwo = 9
    if commandOptionTwo == 1:
        py_interface_branch_create()
    elif commandOptionTwo == 2:
        py_interface_branch_delete()
    elif commandOptionTwo == 3:
        py_interface_branch_checkout()
    elif commandOptionTwo == 4:
        py_interface_branch_status()
    elif commandOptionTwo == 5:
        py_interface_branch_add()
    elif commandOptionTwo == 6:
        py_interface_branch_commit()
    elif commandOptionTwo == 7:
        py_interface_branch_push()
    elif commandOptionTwo == 8:
        py_interface_start()
    elif commandOptionTwo == 9:
        py_interface_branch()
    else:
        py_interface_branch()

print("Please run this program in the directory you need to run git in.")

py_interface_start()
