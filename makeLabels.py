import os
os.chdir("L")

def CCAMB(year):
    problems = []
    for i in range(1,16):
        problems.append("I" + str(i))
    for i in range(1,11):
        problems.append("T" + str(i))
    for i in range(1,6):
        for j in range(1,5):
            problems.append("L" + str(i) + "." + str(j))
    for i in range(1,5):
        problems.append("TB" + str(i))

    for problem in problems:
        filename = "CCAMB-" + str(year) + "-" + problem + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " CCAMB " + problem)
        lfile.close()

def EGMO(year):
    num = 6
    if year == 2012:
        num = 8
    for i in range(1,num + 1):
        filename = "EGMO-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " EGMO \#" + str(i))
        lfile.close()

def OMO(contest):
    season = "Fall"
    if contest[0] == "S":
        season = "Spring"
    for i in range(1,31):
        lfile = open("OMO-" + season + "_20" + contest[-2:] + "-" + str(i) + ".tex","w+")
        lfile.write("OMO " + season + " 20" + contest[-2:] + " " + "\#" + str(i))
        lfile.close()

def SDHMMT(year):
    for i in range(1,11):
        filename = "SDHMMT-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " SDHMMT \#" + str(i))
        lfile.close()

def TARML(year):
    problems = []
    for i in range(1,11):
        problems.append("I" + str(i))
    for i in range(1,3):
        for j in range(1,4):
            problems.append("R" + str(i) + "." + str(j))
    for problem in problems:
        filename = "TARML-" + str(year) + "-" + problem + ".tex"
        lfile = open(filename,"w+")
        if problem[0] == "R":
            problem = problem[:2] + "-" + problem[-1]
        lfile.write(str(year) + " TARML " + problem)
        lfile.close()

def TST(year):
    num = 6
    if year in [2001,2008,2009,2010,2011]:
        num = 9
    if year in [2012,2013]:
        num = 8
    for i in range(1,num + 1):
        filename = "TST-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " TST \#" + str(i))
        lfile.close()

def TSTST(year):
    num = 9
    if year in range(2014,2018):
        num = 6
    for i in range(1,num + 1):
        filename = "TSTST-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " TSTST \#" + str(i))
        lfile.close()

def USAJMO(year):
    for i in range(1,7):
        filename = "USAJMO-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " USAJMO \#" + str(i))
        lfile.close()

def USAMO(year):
    for i in range(1,7):
        filename = "USAMO-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " USAMO \#" + str(i))
        lfile.close()

for year in range(2000,2019):
    TST(year)