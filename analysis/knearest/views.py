from django.shortcuts import render
from knearest.kmeans import *
import json
from django.http import HttpResponse,Http404,HttpResponseRedirect
from knearest.models import *
import csv


# Create your views here.

def home (request):
	return render(request,'home.html')

def getKmeans (request):
	finalObj = {}
	# abc = startFun()
	temp = []
	# print (abc)
	print ("aa")
	# temp.append(abc[0])
	# temp.append(abc[1])

	# temp.append(abc[2])

	# temp.append(abc[3])

	# temp.append(abc[4])

	# temp.append(abc[5])
	# temp.append(abc[6])
	# temp.append(abc[7])

	# finalObj['random one third'] = temp
	finalObj['random one third'] = [68.02773497688752, 67.19413353917406, 66.41566265060241, 67.77910210568136, 57.89473684210527, 65.56473829201101, 68.51967520299813, 76.92307692307693]
	
	# abc = startFun1()
	temp = []
	# print (abc)
	# temp.append(abc[0])
	# temp.append(abc[1])

	# temp.append(abc[2])

	# temp.append(abc[3])

	# temp.append(abc[4])

	# temp.append(abc[5])
	# temp.append(abc[6])
	# temp.append(abc[7])


	# finalObj['all col'] = temp
	finalObj['all col'] = [68.646408839779, 62.65060240963856, 67.19339952454202, 80.0, 65.30898876404494, 68.75,
	69.17599186164801,
	100.0]

	
	# abc = startFun2()
	temp = []
	# print (abc)
	# temp.append(abc[0])
	# temp.append(abc[1])

	# temp.append(abc[2])

	# temp.append(abc[3])

	# temp.append(abc[4])

	# temp.append(abc[5])
	# temp.append(abc[6])
	# temp.append(abc[7])


	# finalObj['first one third'] = temp
	finalObj['first one third'] = [63.0275974025974,
	87.1313672922252,
	67.91208791208791,
	71.62162162162163,
	55.88235294117647,
	74.55470737913485,
	67.96589524969549,
	65.3459972862958]

	# abc = startFun3()
	temp = []
	# print (abc)
	# temp.append(abc[0])
	# temp.append(abc[1])

	# temp.append(abc[2])

	# temp.append(abc[3])

	# temp.append(abc[4])

	# temp.append(abc[5])
	# temp.append(abc[6])
	# temp.append(abc[7])


	# finalObj['second one third'] = temp
	finalObj['second one third'] = [67.80185758513932,
	68.05671392827357,
	60.16559337626495,
	71.68103448275862,
	68.91604675876727,
	63.297872340425535,
	75.0,
	59.91561181434599]

	# abc = startFun4()
	temp = []
	# print (abc)
	# temp.append(abc[0])
	# temp.append(abc[1])

	# temp.append(abc[2])

	# temp.append(abc[3])

	# temp.append(abc[4])

	# temp.append(abc[5])
	# temp.append(abc[6])
	# temp.append(abc[7])

	# finalObj['last remaining'] = temp
	finalObj['last remaining'] = [69.17599186164801,
	65.30898876404494,
	62.65060240963856,
	80.0,
	67.20257234726688,
	100.0,
	68.75,
	68.646408839779]
	print (finalObj)
	return HttpResponse(json.dumps(finalObj), content_type='application/json')

def predictPatient(request):
	pId = int(request.GET.get('patientId'))
	type1 = int(request.GET.get('type'))
	prediction = ''

	mycsv = csv.reader(open("/home/bhavya/Downloads/CAX_Data_Aging.csv"))
	mycsv = list(mycsv)

	ar = mycsv[pId][1]
	an = mycsv[pId][2]
	cl = mycsv[pId][3]
	try:
		if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
			prediction = 'No Disease Found'
		elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
			prediction = 'Patient has Chronic Lung'
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
			prediction = 'Patient has Angina'    	
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
			prediction = 'Patient has both Angina and Chronic Lung'
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
			prediction = 'Patient has Arthritis'
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
			prediction = 'Patient has both Arthritis and Chronic Lung'
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
			prediction = 'Patient has both Arthritis and Angina'
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
			prediction = 'Patient has all Arthritis, Angina and Chronic Lung'
	except:
		pass

	if (type1 == 1):
		value = predictallcol.objects.filter(x = pId)
		if (len(value) != 0):
			pre = value[0].prediction
			if (pre == 0):
				prediction = 'No Disease Found'
			elif (pre == 1):
				prediction = 'Patient has Chronic Lung'
			elif (pre == 2):
				prediction = 'Patient has Angina'    	
			elif (pre == 3):
				prediction = 'Patient has both Angina and Chronic Lung'
			elif (pre == 4):
				prediction = 'Patient has Arthritis'
			elif (pre == 5):
				prediction = 'Patient has both Arthritis and Chronic Lung'
			elif (pre == 6):
				prediction = 'Patient has both Arthritis and Angina'
			elif (pre == 7):
				prediction = 'Patient has all Arthritis, Angina and Chronic Lung'

	if (type1 == 2):
		value = predictonlybig.objects.filter(x = pId)
		if (len(value) != 0):
			pre = value[0].prediction
			if (pre == 0):
				prediction = 'No Disease Found'
			elif (pre == 1):
				prediction = 'Patient has Chronic Lung'
			elif (pre == 2):
				prediction = 'Patient has Angina'    	
			elif (pre == 3):
				prediction = 'Patient has both Angina and Chronic Lung'
			elif (pre == 4):
				prediction = 'Patient has Arthritis'
			elif (pre == 5):
				prediction = 'Patient has both Arthritis and Chronic Lung'
			elif (pre == 6):
				prediction = 'Patient has both Arthritis and Angina'
			elif (pre == 7):
				prediction = 'Patient has all Arthritis, Angina and Chronic Lung'

	if (type1 == 3):
		value = predictexceptbig.objects.filter(x = pId)
		if (len(value) != 0):
			pre = value[0].prediction
			if (pre == 0):
				prediction = 'No Disease Found'
			elif (pre == 1):
				prediction = 'Patient has Chronic Lung'
			elif (pre == 2):
				prediction = 'Patient has Angina'    	
			elif (pre == 3):
				prediction = 'Patient has both Angina and Chronic Lung'
			elif (pre == 4):
				prediction = 'Patient has Arthritis'
			elif (pre == 5):
				prediction = 'Patient has both Arthritis and Chronic Lung'
			elif (pre == 6):
				prediction = 'Patient has both Arthritis and Angina'
			elif (pre == 7):
				prediction = 'Patient has all Arthritis, Angina and Chronic Lung'

	return HttpResponse(json.dumps({'data': prediction}), content_type='application/json')

