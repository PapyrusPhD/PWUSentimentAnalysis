from os import F_OK
from re import T
from django.http import HttpResponse
from django.shortcuts import render
from numpy import positive
from .utils import AllDisplay, averages, SentimentAnalysis, FinalDisplay
from .models import Evaluation, Average

# Create your views here.
def index(request):
    return render(request, "index.html")

def getStarted(request):
    SectionCodeList = Evaluation.objects.values('subjectcode').distinct()
    return render(request, "page2.html", {'SectionCodeList': SectionCodeList})
        
def results(request):
    contents = {}
    User_Picked = request.GET['select']
    if User_Picked == "All":
        graph, negative, neutral, positive = AllDisplay(User_Picked)
        contents['picked'] = User_Picked
        contents['tables'] = graph
        contents['Pos'] = positive
        contents['Neg'] = negative
        contents['Neu'] = neutral
        return render(request, "page3.html", contents) 
    else:
        graph, negative, neutral, positive = FinalDisplay(User_Picked)
        contents['picked'] = User_Picked
        contents['tables'] = graph
        contents['Pos'] = positive
        contents['Neg'] = negative
        contents['Neu'] = neutral
        return render(request, "page3.html", contents)

def evaluation(request):
    return render(request, "evaluate.html")

def confirmation(request):
    if request.method == 'POST':
        flname = request.POST['flname']
        flname = flname.upper()
        subjectcode = request.POST['Section']
        subjectcode = subjectcode.upper()
        name = Evaluation.objects.filter(subjectcode = subjectcode).values_list('flname', flat=True)
        nameList = list(name).count(flname)
        comment = request.POST['comment']
        prof = request.POST['Prof']
        if nameList < 1:
            sem = request.POST['sem']
            year = request.POST['Year']

            select1 = int(request.POST['select1'])
            select2 = int(request.POST['select2'])
            select3 = int(request.POST['select3'])
            select4 = int(request.POST['select4'])
            select5 = int(request.POST['select5'])
            select6 = int(request.POST['select6'])
            select7 = int(request.POST['select7'])
            select8 = int(request.POST['select8'])
            select9 = int(request.POST['select9'])
            select10 = int(request.POST['select10'])
            select11 = int(request.POST['select11'])
            select12 = int(request.POST['select12'])
            select13 = int(request.POST['select13'])
            select14 = int(request.POST['select14'])
            select15 = int(request.POST['select15'])
            select16 = int(request.POST['select16'])
            select17 = int(request.POST['select17'])
            select18 = int(request.POST['select18'])
            select19 = int(request.POST['select19'])
            select20 = int(request.POST['select20'])
            select21 = int(request.POST['select21'])
            select22 = int(request.POST['select22'])
            select23 = int(request.POST['select23'])
            select24 = int(request.POST['select24'])
            select25 = int(request.POST['select25'])
            select26 = int(request.POST['select26'])
            select27 = int(request.POST['select27'])
            select28 = int(request.POST['select28'])
            select29 = int(request.POST['select29'])
            select30 = int(request.POST['select30'])


            round_mastery, round_planning, round_communication, round_instructions, round_classroom, round_personal, finalRoundAverage = averages(select1, select2, select3, select4, select5, select6, select7, select8, select9, select10,
            select11, select12, select13, select14, select15, select16, select17, select18, select19, select20,
            select21, select22, select23, select24, select25, select26, select27, select28, select29, select30)

            comment_average = SentimentAnalysis(comment)

            inputed_average = Average(prof = prof, subjectcode = subjectcode, mastery_average = round_mastery, planning_average = round_planning, communication_average = round_communication, 
                            instructions_average = round_instructions, classroom_average = round_classroom, personal_average = round_personal, 
                            Final_average = finalRoundAverage, comment_average= comment_average)


            inputed_evaluation = Evaluation(flname = flname, 
                        prof = prof, sem = sem,year = year, subjectcode = subjectcode, mastery1 = select1,
                        mastery2 = select2, mastery3 = select3, mastery4 = select4, mastery5 = select5,
                        planning1 = select6, planning2 = select7, planning3 = select8, planning4 = select9, planning5 = select10,
                        communication1 = select11, communication2 = select12, communication3 = select13, communication4 = select14, communication5 = select15,
                        instructional1 = select16, instructional2 = select17, instructional3 = select18, instructional4 = select19, instructional5 = select20,
                        classroom1 = select21, classroom2 = select22, classroom3 = select23, classroom4 = select24, classroom5 = select25,
                        personal1 = select26, personal2 = select27, personal3 = select28, personal4 = select29, personal5 = select30, comments = comment)
            inputed_evaluation.save()
            inputed_average.save()
            return render(request, "confirmation.html")
        else:
            return render(request, "repeating.html")
