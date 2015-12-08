import numpy as np
import random
import csv
import xlrd
import pprint

globalObj = {}
pp = pprint.PrettyPrinter(indent=4)

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    # print(oldmu, mu)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def init_board(columnArr):
    mycsv = csv.reader(open("/home/bhavya/Downloads/CAX_Data_Aging.csv"))
    mycsv = list(mycsv)
   # print(mycsv[1][17])
    # read a cell
    counter = 1
    # j = 0
    cell = []
   # print(int(mycsv[1][int(columnArr[0])]))
    # print(len(columnArr))   
    while (counter < 12959):
        eachrow = []
        #eachrow has information of each col selected of a particular patient
        j = 0
        while(j < len(columnArr)):
            row = counter
            col = int(columnArr[j])
            # print(row)
            # print(col)    
            if (mycsv[row][col] == ''):
                mycsv[row][col] = -1
            eachrow.append(float(mycsv[row][col]))
            # print(eachrow[j])
            j += 1
        eachrow = tuple(eachrow) #making tuple as algo accepts tuple
        cell.append(eachrow) #cell array has all the tuples
        globalObj[eachrow] = counter #associating the tuple with its patient id
        counter += 1
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(cell)
    X = np.array([i for i in cell])
    return find_centers(list(X), 8)


# select random 1/3 of similar columns and pass it to init

def data_dictionary():
    book = xlrd.open_workbook('/home/bhavya/Downloads/CAX_Data_Dictionary.xlsx')

    # print number of sheets
    # print(book.nsheets)

    # print(sheet names
    # print(book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    # print(first_sheet.row_values(0))
    pp = pprint.PrettyPrinter(indent=4)
    # read a cell
    finalObj = {}
    counter = 4
    prev = first_sheet.cell(counter,2)
    # print(str(prev))
    count = 1
    arrayCounter = 0
    counter += 1
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        if (str(cell) == str(prev)):
            count += 1
        else:
            # try:
            #     abc = finalObj[str(cell)]
            #     finalObj[str(cell)] = abc + count
            # except:
            finalObj[arrayCounter] = count
            count = 1
            prev = cell
            arrayCounter += 1

        counter += 1
    finalObj[arrayCounter] = count   
    # pp.pprint(finalObj) 
    # print(finalObj[text:'Residence'])
    columnArr = []
    counter = 4
    arrayCounter = 0
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        abc = finalObj[arrayCounter]
        finalPoint = counter + abc
        times = int(abc / 3)
        newSet = set()
        if (times == 0):
            columnArr.append(counter)
        else:
            while (1):
                x = random.randint(counter, finalPoint - 1)
                newSet.add(x)
 #               print(x, counter, finalPoint)
                if(len(newSet) == times):
                    break
            temp = list(newSet)
            for t in temp:
                columnArr.append(t)
        counter = finalPoint
        arrayCounter += 1
    # pp.pprint(columnArr)
    return init_board(columnArr)


# function for sending all columns to init_board

def send_all():
    columnArr = []
    colCount = 4
    while (colCount <= 268):
        columnArr.append(colCount)
        colCount += 1

    return init_board(columnArr)

# send one third of columns that are similar
def send_one_third():
    book = xlrd.open_workbook('/home/bhavya/Downloads/CAX_Data_Dictionary.xlsx')

    # print number of sheets
    # print(book.nsheets)

    # print(sheet names
    # print(book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    # print(first_sheet.row_values(0))
    pp = pprint.PrettyPrinter(indent=4)
    # read a cell
    finalObj = {}
    counter = 4
    prev = first_sheet.cell(counter,2)
    # print(str(prev))
    count = 1
    arrayCounter = 0
    counter += 1
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        if (str(cell) == str(prev)):
            count += 1
        else:
            # try:
            #     abc = finalObj[str(cell)]
            #     finalObj[str(cell)] = abc + count
            # except:
            finalObj[arrayCounter] = count
            count = 1
            prev = cell
            arrayCounter += 1

        counter += 1
    finalObj[arrayCounter] = count   
    # pp.pprint(finalObj) 
    # print(finalObj[text:'Residence'])
    columnArr = []
    counter = 4
    arrayCounter = 0
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        abc = finalObj[arrayCounter]
        finalPoint = counter + abc
        times = int(abc / 3)
        newSet = set()
        if (times == 0):
            columnArr.append(counter)
        else:
            while (1):
                # x = random.randint(counter, finalPoint - 1)
                x = counter
                newSet.add(x)
                counter += 1
 #               print(x, counter, finalPoint)
                if(len(newSet) == times):
                    break
            temp = list(newSet)
            for t in temp:
                columnArr.append(t)
        counter = finalPoint
        arrayCounter += 1
    # pp.pprint(columnArr)
    return init_board(columnArr)

# send second one third of columns that are similar
def send_one_third_second():
    book = xlrd.open_workbook('/home/bhavya/Downloads/CAX_Data_Dictionary.xlsx')

    # print number of sheets
    # print(book.nsheets)

    # print(sheet names
    # print(book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    # print(first_sheet.row_values(0))
    pp = pprint.PrettyPrinter(indent=4)
    # read a cell
    finalObj = {}
    counter = 4
    prev = first_sheet.cell(counter,2)
    # print(str(prev))
    count = 1
    arrayCounter = 0
    counter += 1
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        if (str(cell) == str(prev)):
            count += 1
        else:
            # try:
            #     abc = finalObj[str(cell)]
            #     finalObj[str(cell)] = abc + count
            # except:
            finalObj[arrayCounter] = count
            count = 1
            prev = cell
            arrayCounter += 1

        counter += 1
    finalObj[arrayCounter] = count   
    # pp.pprint(finalObj) 
    # print(finalObj[text:'Residence'])
    columnArr = []
    counter = 4
    arrayCounter = 0
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        abc = finalObj[arrayCounter]
        finalPoint = counter + abc
        times = int(abc / 3)
        newSet = set()
        if (times == 0):
            columnArr.append(counter)
        else:
            while (1):
                # x = random.randint(counter, finalPoint - 1)
                x = counter + times
                newSet.add(x)
                counter += 1
 #               print(x, counter, finalPoint)
                if(len(newSet) == times):
                    break
            temp = list(newSet)
            for t in temp:
                columnArr.append(t)
        counter = finalPoint
        arrayCounter += 1
    # pp.pprint(columnArr)
    return init_board(columnArr)


# send last one third of columns that are similar
def send_one_third_last():
    book = xlrd.open_workbook('/home/bhavya/Downloads/CAX_Data_Dictionary.xlsx')

    # print number of sheets
    # print(book.nsheets)

    # print(sheet names
    # print(book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    # print(first_sheet.row_values(0))
    pp = pprint.PrettyPrinter(indent=4)
    # read a cell
    finalObj = {}
    counter = 4
    prev = first_sheet.cell(counter,2)
    # print(str(prev))
    count = 1
    arrayCounter = 0
    counter += 1
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        if (str(cell) == str(prev)):
            count += 1
        else:
            # try:
            #     abc = finalObj[str(cell)]
            #     finalObj[str(cell)] = abc + count
            # except:
            finalObj[arrayCounter] = count
            count = 1
            prev = cell
            arrayCounter += 1

        counter += 1
    finalObj[arrayCounter] = count   
    # pp.pprint(finalObj) 
    # print(finalObj[text:'Residence'])
    columnArr = []
    counter = 4
    arrayCounter = 0
    while (counter <= 268):
        cell = first_sheet.cell(counter,2)
        # print(str(cell), str(prev), count)
        abc = finalObj[arrayCounter]
        # print("abc" + str(abc))
        finalPoint = counter + abc
        times = int(abc / 3)
        newSet = set()
        if (times == 0):
            columnArr.append(counter)
        else:
            while (1):
                # x = random.randint(counter, finalPoint - 1)
                x = counter + times * 2
                newSet.add(x)
                counter += 1
                # print(x, counter, finalPoint)
                if(x + 1 == finalPoint):
                    break
            temp = list(newSet)
            for t in temp:
                columnArr.append(t)
        counter = finalPoint
        # print("counter" + str(counter))
        arrayCounter += 1
    # pp.pprint(columnArr)
    return init_board(columnArr)


def accuracy(clusNew) :
    clusCount = 0
    accu = {}
    mycsv = csv.reader(open("/home/bhavya/Downloads/CAX_Data_Aging.csv"))
    mycsv = list(mycsv)

    while(clusCount<8) :
        disease = {}
        for c in clusNew[clusCount]:
            ar = mycsv[c][1]
            an = mycsv[c][2]
            cl = mycsv[c][3]
            try:
                if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
                    try:
                        disease[0] += 1
                    except:
                        disease[0] = 1
                elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
                    try:
                        disease[1] += 1
                    except:
                        disease[1] = 1
                elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
                    try:
                        disease[2] += 1
                    except:
                        disease[2] = 1
                elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
                    try:
                        disease[3] += 1
                    except:
                        disease[3] = 1
                elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
                    try:
                        disease[4] += 1
                    except:
                        disease[4] = 1
                elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
                    try:
                        disease[5] += 1
                    except:
                        disease[5] = 1
                elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
                    try:
                        disease[6] += 1
                    except:
                        disease[6] = 1
                elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
                    try:
                        disease[7] += 1
                    except:
                        disease[7] = 1
            except:
                pass
        diseaseCount = 0
        sumTotal = 0
        maxCount = 0
        print(disease)
        while (diseaseCount < 8):
            try:
                sumTotal += disease[diseaseCount]
                if (disease[diseaseCount] > maxCount):
                    maxCount = disease[diseaseCount]
            except:
                pass
            diseaseCount += 1
        accu[clusCount] = float(maxCount / sumTotal) * 100
        clusCount += 1
    pp.pprint(accu)
    return accu    
    
# from kmeans import *  
# >>> x=init_board()


def seg (y):
    clus = y[1] #selecting clusters
    #pp.pprint(clus)
    clusCount = 0
    clusNew = {} #saves patients id corresponding to a cluster as we get the whole tuple as result
    while (clusCount < 8):
        try:
            finalclus = clus[clusCount]
            # print(finalclus)
            clusNew[clusCount] = []
            for f in finalclus:
                abc = tuple(f)
                clusNew[clusCount].append(globalObj[abc])
            clusCount += 1
        except:
            pass
    #pp.pprint (clusNew)
    return accuracy(clusNew)


def startFun():
    y = data_dictionary() #if data dictionary then randomly one third
    print ("Accuracy of randomly calculated one third is : ")
    return seg(y)

def startFun1():

    #takes all
    y = send_all()
    print ("Accuracy of all columns calculated is : ")
    return seg(y)

def startFun2():

    #takes one third not randomly

    y = send_one_third()
    print ("Accuracy of first one third is : ")
    return seg(y)

def startFun3():

    # takes second one third not randomly

    y = send_one_third_second()
    print ("Accuracy of second one third is : ")
    return seg(y)

def startFun4():

    # takes last one third not randomly

    y = send_one_third_last()
    print ("Accuracy of last remaining is : ")
    return seg(y)