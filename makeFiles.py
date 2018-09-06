import os
os.chdir("P")

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
        os.system("touch " + filename)
        os.system("open " + filename)

def EGMO(year):
    num = 6
    if year == 2012:
        num = 8
    for i in range(1,num + 1):
        filename = "EGMO-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def OMO(contest):
    path = "~/Dropbox/OMO/" + contest + "/problems"
    season = "Fall"
    if contest[0] == "S":
        season = "Spring"
    for i in range(1,31):
        problemnum = str(i)
        if len(problemnum) == 1:
            problemnum = "0" + problemnum
        pfile = open("OMO-" + season + "_20" + contest[-2:] + "-" + str(i) + ".tex","w+")
        os.chdir(os.path.expanduser(path))
        orig = open("prob" + problemnum + ".tex","r")
        for line in orig:
            if line[:5] == "\item":
                pass
            elif line[:11] == "\proposedby":
                break
            else:
                pfile.write(line)
        orig.close()
        pfile.close()
        os.chdir(os.path.expanduser("~/Google Drive/Math Stuff/ProblemDatabase/P"))

def SDHMMT(year):
    for i in range(1,11):
        filename = "SDHMMT-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def TARML(year):
    problems = []
    for i in range(1,11):
        problems.append("I" + str(i))
    for i in range(1,3):
        for j in range(1,4):
            problems.append("R" + str(i) + "." + str(j))
    for problem in problems:
        filename = "TARML-" + str(year) + "-" + problem + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def TST(year):
    num = 6
    if year in [2001,2008,2009,2010,2011]:
        num = 9
    if year in [2012,2013]:
        num = 8
    for i in range(1,num + 1):
        filename = "TST-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def TSTST(year):
    num = 9
    if year in range(2014,2018):
        num = 6
    for i in range(1,num + 1):
        filename = "TSTST-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def USAJMO(year):
    for i in range(1,7):
        filename = "USAJMO-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def USAMO(year):
    for i in range(1,7):
        filename = "USAMO-" + str(year) + "-" + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

for year in range(2000,2019):
    TST(year)
