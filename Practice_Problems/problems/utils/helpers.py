import re
import os
import json
from pathlib import Path

UTILS_PATH = Path(__file__).parent

def clear_screen():
    # For Unix/Linux
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

def check_input(pattern, prompt,reject_prompt):
    no_match = True
    inp = ""
    while(no_match):
        inp = input(prompt).upper().lstrip(" ")
        no_match = not re.search(pattern, inp)
        
        if(no_match):
            clear_screen()
            input(f"{reject_prompt}\nPress enter to continue.\n")
            clear_screen()
    return inp


def sort_dict(d:dict) -> dict:
    sorted_keys = sorted(d)

    return {key: d[key] for key in sorted_keys}

def read_json(file: str = UTILS_PATH / "progress.json") -> dict:
    with open(file, "r") as file:
        data = json.load(file)

    return data
    

def write_json(file: str = UTILS_PATH / "progress.json", data: dict = None) -> None:
    with open(file, 'w') as file:
        json.dump(data, file)


def get_file_names(folder: Path = Path(__file__).parent.parent) -> dict:
    path = folder
    
    return [f.name for f in path.iterdir() if f.is_file()]


def update_report():
    try:
        report = read_json(UTILS_PATH / "progress.json")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        report = {"progress":{}}
        

    try:
        progress = report["progress"]
    except KeyError as e:
        report["progress"] = {}
        progress = report["progress"]


    files = get_file_names(Path(__file__).parent.parent)

    for f in files:
        if f not in progress:
            progress[f] = "\u274C Not Yet Passed"

    report["progress"] = sort_dict(report["progress"])
    write_json(UTILS_PATH / "progress.json", report)
    write_report()


def show_report(write: bool = False) -> None:
    update_report()

    with open(Path(__file__).parent.parent.parent / "progress_report.txt", "rb") as f:
        print(f.read().decode("utf-8"))



def clear_report(file: Path = UTILS_PATH / "progress.json"):
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
    
    update_report()


def write_report(path: Path = Path(__file__).parent.parent.parent / "progress_report.txt"):

    report = read_json()
    
    lines = []
    num_passed = 0 
    num_of_problems = len(report["progress"])

    for key, value in report["progress"].items():
        if "\u2705 Passed" in value:
            num_passed += 1

        line = f"{value}  ".ljust(18," ") + f":  {key}\n"
        lines.append(line)

    summary = [
        f"\nTotal Number of Problems : {num_of_problems}\n",
        f"Total Problems Completed : {num_passed}\n",
        f"Percent Completed : {round(num_passed / num_of_problems*100)}%\n"
    ]

    lines += summary

    with open(path, "wb") as f:
        f.writelines(to_bytes(lines))

def to_bytes(lst) -> list[bytes]:
    bytes_list = []
    for e in lst:
        bytes_list.append(bytes(e.encode("utf-8")))

    return bytes_list

if __name__ == "__main__":
    clear_report()

    
