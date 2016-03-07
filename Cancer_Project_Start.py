###############################################################################
import pdb
import sys
###############################################################################
# Tasks
# 1 - Create a training set
# 2 - Train a 'dumb' rule-based classifier
# 3 - Create a test set
# 4 - Apply rule-based classifier to test set
# 5 - Report accuracy of classifier
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and sums
# DONE - Do not modify.
###############################################################################
attributeList = []
attributeList.append("ID")
attributeList.append("radius")
attributeList.append("texture")
attributeList.append("perimeter")
attributeList.append("area")
attributeList.append("smoothness")
attributeList.append("compactness")
attributeList.append("concavity")
attributeList.append("concave")
attributeList.append("symmetry")
attributeList.append("fractal")
attributeList.append("class")



###############################################################################
# 1. Create a training set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
# makeTrainingSet
# parameters: 
#     - filename: name of the data file containing the training data records
#
# returns: trainingSet: a list of training records (each record is a dict,
#                       that contains attribute values for that record.)
###############################################################################
def makeTrainingSet(filename):
    # DONE - Do not modify.
    trainingSet = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        # Create a dictionary for the line
        # ( assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys )
        record = {}
        for i in range(len(attributeList)):
              if(i==11): #class label is a character, not a float
                  record[attributeList[i]] = linelist[31].strip() 
              else:
                  record[attributeList[i]] = float(linelist[i])
        # Add the dictionary to a list
        trainingSet.append(record)        

    return trainingSet

###############################################################################
# 2. Train 'Dumb' Classifier
# trainClassifier
# parameters:
#     - trainingSet: a list of training records (each record is a dict,
#                     that contains attribute values for that record.)
#
# returns: a dictionary of midpoints between the averages of each attribute's
#           values for benign and malignant tumors
###############################################################################
def trainClassifier(trainingSet):
    # TODO
    
    # A. initialize dictionaries for sums of attribute values
    #    and initialize record counts
    attributeSumsBenign = dict.fromkeys(attributeList)
    for i in range(len(attributeList)):
        if i == 11:
            attributeSumsBenign[attributeList[i]] = 'B'
        else: 
            attributeSumsBenign[attributeList[i]] = 0

    attributeSumsMalign = dict.fromkeys(attributeList)
    for i in range(len(attributeList)):
        if i == 11:
            attributeSumsMalign[attributeList[i]] = 'M'
        else:
            attributeSumsMalign[attributeList[i]] = 0        
    
    # B. process each record in the training set
    #    calculating sums and counts as we go
    nBenignCount = 0
    nMalignCount = 0
    for value in trainingSet:
        if value['class'] == 'B':
            for i in range(len(attributeList) - 1):
                if attributeList[i] == 'ID':
                    attributeSumsBenign[attributeList[i]] = value[attributeList[i]]
                else:
                    attributeSumsBenign[attributeList[i]] = attributeSumsBenign[attributeList[i]] + float(value[attributeList[i]])
            nBenignCount += 1
        elif value['class'] == 'M':
            for i in range(len(attributeList) - 1):
                if attributeList[i] == 'ID':
                    attributeSumsMalign[attributeList[i]] = value[attributeList[i]]
                else:
                    attributeSumsMalign[attributeList[i]] = attributeSumsMalign[attributeList[i]] + float(value[attributeList[i]])
            nMalignCount += 1
            
    # C. calculate averages 
    for i in range(len(attributeList) - 1):
        attributeSumsBenign[attributeList[i]] = attributeSumsBenign[attributeList[i]] / nBenignCount
        attributeSumsMalign[attributeList[i]] = attributeSumsMalign[attributeList[i]] / nMalignCount
        #print i, attributeList[i], attributeSumsBenign[attributeList[i]]
        #print i, attributeList[i], attributeSumsMalign[attributeList[i]]
        
    # D. calcualte midpoints for our classifier
    midPoint = dict.fromkeys(attributeList)
    for i in range(len(attributeList) - 1):
        midPoint[attributeList[i]] = 0;
        
    for i in range(len(attributeList) - 1):
        if attributeList[i] != 'ID':
            midPoint[attributeList[i]] = (attributeSumsBenign[attributeList[i]] + attributeSumsMalign[attributeList[i]]) / 2;  

    #    return classifier
    return midPoint, attributeSumsBenign, attributeSumsMalign

2

###############################################################################
# 3. Create a test set
# - Read in file
# - Create a dictionary for each line
# - Initialize each record's predicted class to '0'
# - Add this dictionary to a list
#
# makeTestSet
# parameters: 
#     - filename: name of the data file containing the test data records
#
# returns: testSet: a list of test records (each record is a dict,
#                       that contains attribute values for that record
#                       and where the predicted class is set to 0. 
###############################################################################
def makeTestSet(filename):

    # DONE - Do not modify.
    testset = makeTrainingSet(filename)

    for record in testset:
        record["predicted"] = 0

    return testset


###############################################################################
# 4. Classify test set
#
# classifyTestRecords
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#      - classifier: a dictionary of midpoint values for each attribute
#
# returns: testSet with the predicted class set to either 2 (benign) or 4 (malignant)
#
# for each record, if the majority of attributes are greater than midpoint
# then predict the record as malignant
###############################################################################
def classifyTestRecords(testSet, classifier):
    #pass
    # TODO
    
    # For each record in testset

        # initialize malignant and benign votes to zero

        # for each attribute of the record
            # if attribute value is greater than midpoint then
            # add one to malignant vote. Otherwise, add one to benign vote

        # if malignant vote greater than or equal to benign vote then
        # predicted class of record is malignant (set predicted class value)
        # otherwise, the predicted class is benign
            
#    return testSet 
    for record in testSet:
        nVoteCountMalign = 0
        nVoteCountBenign = 0
        #pdb.set_trace()
        #print record
        for attribute in attributeList:
            if record[attribute] > classifier[attribute]:  #The supplement says we are to check >= but when we do that we get acccuracy as 204/231
                nVoteCountMalign = nVoteCountMalign + 1
            else:
                nVoteCountBenign = nVoteCountBenign + 1
        
        if nVoteCountMalign > nVoteCountBenign:
            record['predicted'] = '4'
        else:
            record['predicted'] = '2'
            
    return testSet


###############################################################################
# 5. Report Accuracy
# reportAccuracy
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#                 and both the predicted and actual class values are set
#
# returns: None
#
# prints out the number correct / total and accuracy as a percentage
###############################################################################
def reportAccuracy(testSet):
    #pass
    # TODO

    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class ("predicted") to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.
    nCorrectCount = 0
    nTotalCount = 0
    for record in testSet:
        if ((record['class'] == 'B' and record['predicted'] == '2') or (record['class'] == 'M' and record['predicted'] == '4')):
            nCorrectCount = nCorrectCount + 1
        else:        
            print record
        nTotalCount = nTotalCount + 1
        
    print "The classifier correctly predicted the class (malignent/benign) of ", nCorrectCount, "records out of ", nTotalCount, " records"
    accuracy =  (float(nCorrectCount)/nTotalCount) * 100
    print "The accuracy of the model is ", accuracy 
    return None
###############################################################################
def dumpStats(classifier,benignAverages,malignantAverages):
    
# TODO
# print out the averages and classifier cutoff for each of the 9 categories
# write to a file named "cancer_stats.dat" the printed averages and classifier      
#   cutoff for each of the 9 categories
# use the following format string to reproduce the table in the demo is
# print '%28s %12.3f %12.3f %12.3f'%(key,malignanAvg[key],classifier[key],benignAvg[key])
# write this same table to the "cancer_stats.dat"  as well. 
    f = open("cancer.dat","w") 
    print "Classifier, benign and malignant stats"
    print "============================================================================="
    print "Key  Malignant  Classifier  Benign"
    print '%70s'%'Key  Malignant  Classifier  Benign'
    for key in attributeList:
        if key != 'class' and key != 'ID':
            #print key
            #print malignantAverages[key],classifier[key],benignAverages[key]
            print '%28s %12.3f %12.3f %12.3f'%(key,malignantAverages[key],classifier[key],benignAverages[key])
            string = str(key)+ str(malignantAverages[key])+ str(classifier[key]) + str(benignAverages[key]) + str("\n")
            f.write(string)
    f.close() 
    
    return None

def checkSomePatients(testDataRecordsList, classifier):
    #pass
# TODO
# starts a prompting loop. Prompts for a patient ID
# for each value, prints out the patient's value, the classifier cutoff and the diagnosis
# prints out the final diagnosis
    while (1):
        userInput = raw_input("Type an ID to check a patient ('quit' to stop)")
        if userInput == 'quit':
               sys.exit(0)
        else:
            nPatientID = int(userInput)
            print "Checking ID:", nPatientID,"'s classification"
            print '%70s'%'Key  Patients Value  Classifier Value  Class'
            for record in testDataRecordsList:  
                patientInfo = {}
                tempClass = ""
                tempCount = 0
                #pdb.set_trace()
                if record['ID'] == nPatientID:
                    for i in range(len(attributeList)):
                        #pdb.set_trace()
                        if attributeList[i] != 'ID' and attributeList[i] != 'class':
                            patientInfo[attributeList[i]] = record[attributeList[i]]
                            if patientInfo[attributeList[i]] >= classifier[attributeList[i]]:
                                tempClass = "Malignent"
                                tempCount = tempCount + 1
                            else:
                                tempClass = "Benign"
                       
                            print '%28s %12.3f %12.3f %12s'%(attributeList[i], patientInfo[attributeList[i]],classifier[attributeList[i]],tempClass)
            
                    if tempCount >= 5:
                        tempClass = "Malignent"
                    else:
                        tempClass = "Benign"
                    print "Overall diagnosis for patient", nPatientID, ": ", tempClass
    
    return None            
    
###############################################################################
# main - starts the program
###############################################################################
def main():
    # TODO
    print "Reading in training data..."
    trainingSet = []
    trainingFile = "cancerTrainingData.txt"
    
    trainingSet = makeTrainingSet(trainingFile)
    print "Done reading training data.\n"

    print "Training classifier..."    
    # add call to appropriate function
    trainedClassifier = trainClassifier(trainingSet)
    #print trainedClassifier[0]
    #print trainedClassifier[1]
    #print trainedClassifier[2]
    #pdb.set_trace()
    print "Done training classifier.\n"

    print "Present Classifier Stats"
    # add call to appropriate function
    dumpStats(trainedClassifier[0], trainedClassifier[1], trainedClassifier[2]) 

    print "Reading in test data..."
    testFile = "cancerTestingData.txt"
    testSet = makeTestSet(testFile)
    print "Done reading test data.\n"

    print "Classifying records..."
    # add call to appropriate function
    classifiedTestSet = classifyTestRecords(testSet, trainedClassifier[0])

    print "Done classifying.\n"
    # add call to appropriate function
    reportAccuracy(classifiedTestSet)

    print "Check some Patients"
    # add call to appropriate function
    checkSomePatients(classifiedTestSet, trainedClassifier[0])    

    print "Program finished."
    
main()
