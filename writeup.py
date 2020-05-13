import os
import fnmatch
import datetime
import glob
import sys

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root,name))
    return result

def find_pattern(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name,pattern):
                result.append(os.path.join(root,name))
    return result

"""
def today():
    date = str(datetime.date.today())
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return str(int(date[8:10])) + " " + months[int(date[5:7]) - 1] + " " + date[:4]
"""
def today():
    return input("DATE :: ")

def write(problem):
    PSearch = find_all(problem + ".tex","P")
    SSearch = find_all(problem + ".tex","S")
    LSearch = find_all(problem + ".tex","L")
    WSearch = find_all(problem + ".tex","W")
    P_EXIST = len(PSearch) > 0
    S_EXIST = len(SSearch) > 0
    L_EXIST = len(LSearch) > 0
    W_EXIST = len(WSearch) > 0
    ready = True
    Pready = True
    if not P_EXIST:
        print("Please write problem file.")
        Pready = False
        ready = False
    if not S_EXIST:
        print("Please write solution file.")
        ready = False
    if not L_EXIST:
        print("Please write label file.")
        if Pready:
            os.chdir("L")
            os.system("touch " + problem + ".tex")
            os.system("open " + problem + ".tex")
            os.chdir("..")
        ready = False
    if ready and not W_EXIST:
        os.chdir("L")
        label = open(problem + ".tex","r")
        title = label.readline()
        os.chdir("..")
        # title = input("TITLE :: ")
        os.chdir("W")
        writeup = open(problem + ".tex","w+")
        writeup.write("\\documentclass[letter, 12pt]{article}\n")
        writeup.write("\\usepackage{tssal}\n")
        writeup.write("\n")
        writeup.write("\\title{" + title + "}\n")
        writeup.write("\\author{Dylan Yu}\n")
        writeup.write("\\date{" + today() + "}\n")
        writeup.write("\n")
        writeup.write("\\begin{document}\n")
        writeup.write("\n")
        writeup.write("\\maketitle\n")
        writeup.write("\n")
        writeup.write("\\pdb{" + problem + "}\n")
        writeup.write("\n")
        writeup.write("\\hrulefill\n")
        writeup.write("\n")
        writeup.write("\\begin{solution}\n")
        writeup.write("\\sdb{" + problem + "}\n")
        writeup.write("\\end{solution}\n")
        writeup.write("\n")
        writeup.write("\\end{document}")
        writeup.close()
        os.chdir("..")
    if ready:
        os.chdir("W")
        os.system("pdflatex " + problem + ".tex")
        os.chdir("..")
        asy_files = find_pattern(problem + "*.asy","W")
        if len(asy_files) > 0:
            os.chdir("W")
            for asy_file in asy_files:
                asy_file = asy_file[2:]
                os.system("asy " + asy_file)
            os.system("pdflatex " + problem + ".tex")
            os.chdir("..")
        related_files = find_pattern(problem + "*","W")
        os.chdir("W")
        for file in related_files:
            file = file[2:]
            if file[len(problem)] == "." or file[len(problem)] == "-":
                if file != problem + ".tex" and file != problem + ".pdf":
                    os.system("rm " + file)
        os.system("mv " + problem + ".pdf" + " ../W-PDF")
        os.chdir("../W-PDF")
        os.system("open " + problem + ".pdf")
        os.chdir("..")

# problem = input("PROBLEM :: ")
problem = sys.argv[1]
if " " not in problem:
    write(problem)
