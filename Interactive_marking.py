import json
import os
import time
import sys
from colorama import Fore, Back, Style

def loop_menu(data):
    os.system('cls')
    print("Do you want to :")
    print("1) Mark all data")
    print("2) Mark only unmarked data")
    print("3) Save the marked data")
    print("4) Exit without saving")
    print("5) Get percentage of completion")
    action = input("Your choice (1 to 5): ")
    if action not in ["1", "2", "3", "4", "5"]:
        print("The selected action is not recognized")
        print("restarting menu")
        time.sleep(2)
        loop_menu(data)
    elif action=="1":
        return mark_all(data)
    elif action=="2":
        return mark_unmarked(data)
    elif action=="3":
        return save(data)
    elif action=="4":
        return exit()
    elif action=="5":
        return completion(data)


def mark_all(data):
    mark_data(data,True)
    loop_menu(data)

def mark_unmarked(data):
    mark_data(data, False)
    loop_menu(data)

def save(data):
    with open("dataset_marked.json", "wt") as f:
        json.dump(data_set, f, indent=2)
    loop_menu(data)

def exit():
    sys.exit()

def mark_data(data,all_element):
    for item in data:
        if (not item["Reviewed"]) or all_element:
            for att in item['attributes']:
                os.system('cls')
                print(item["original_text"])
                print("_________________________________________________________")
                print("Full attribute:", end=" ")
                print(att[0][0],":",", ".join([string[0] for string in att[1:]]))
                print("_________________________________________________________")
                for a in att:
                    answer=""
                    while answer not in ["f","t","s"]:
                        answer = input(f"{a[0]}\t. Is it a correct description ? Press t for True, f for False, s to stop the process: ")
                        if answer=="s":
                            return
                        elif answer=="t":
                            a[1] = True
                        elif answer=="f":
                            a[1] = False
        item["Reviewed"] = True

def completion(data):
    answers = [item['Reviewed'] for item in data]
    os.system('cls')

    print(f"There are {len(answers)} items in the data and {sum(answers)} were reviewed. Completion rate: {100*sum(answers)/len(answers):.2f}%")
    input("Press any key to continue")
    loop_menu(data)





if __name__=="__main__":
    with open("dataset.json", "rt") as f:
        data_set = json.load(f)
    loop_menu(data_set)
