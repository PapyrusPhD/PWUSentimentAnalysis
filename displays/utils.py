from textblob import TextBlob
from .models import Average
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def averages(select1, select2, select3, select4, select5, select6, select7, select8, select9, select10,
        select11, select12, select13, select14, select15, select16, select17, select18, select19, select20,
        select21, select22, select23, select24, select25, select26, select27, select28, select29, select30):

        total1 = select1 + select2 + select3 + select4 + select5
        mastery_average = total1 / 5
        total2 = select6 + select7 + select8 + select9 + select10
        planning_average = total2 / 5
        total3 = select11 + select12 + select13 + select14 + select15
        communication_average = total3 / 5
        total4 = select16 + select17 + select18 + select19 + select20
        instructions_average = total4 / 5
        total5 = select21 + select22 + select23 + select24 + select25
        classroom_average = total5 / 5
        total6 = select26 + select27 + select28 + select29 + select30
        personal_average = total6 / 5

        round_mastery = round(mastery_average)
        round_planning = round(planning_average)
        round_communication = round(communication_average)
        round_instructions = round(instructions_average)
        round_classroom = round(classroom_average)
        round_personal = round(personal_average)
        final = round_mastery + round_planning + round_communication + round_instructions +  round_classroom + round_personal
        final_average = final / 6
        finalRoundAverage = round(final_average)
        return round_mastery,  round_planning, round_communication, round_instructions, round_classroom, round_personal,  finalRoundAverage

def SentimentAnalysis(comment):
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity
        sentiment1 = round(sentiment)

        if sentiment1 > 0:
                sentiment1 = 2
                return sentiment1
        elif sentiment1 < 0:
                sentiment1 = 0
                return sentiment1
        else:
                sentiment1 = 1
                return sentiment1
        
def FinalDisplay(User_Picked):
        Mastery = Average.objects.filter(subjectcode = User_Picked).values_list('mastery_average', flat=True)
        Mastery0 = list(Mastery).count(0)
        Mastery1 = list(Mastery).count(1)
        Mastery2 = list(Mastery).count(2)

        Planning = Average.objects.filter(subjectcode = User_Picked).values_list('planning_average', flat=True)
        Planning0 = list(Planning).count(0)
        Planning1 = list(Planning).count(1)
        Planning2 = list(Planning).count(2)

        Communication = Average.objects.filter(subjectcode = User_Picked).values_list('communication_average', flat=True)
        Communication0 = list(Communication).count(0)
        Communication1 = list(Communication).count(1)
        Communication2 = list(Communication).count(2)

        Instructions = Average.objects.filter(subjectcode = User_Picked).values_list('instructions_average', flat=True)
        Instructions0 = list(Instructions).count(0)
        Instructions1 = list(Instructions).count(1)
        Instructions2 = list(Instructions).count(2)

        Classroom = Average.objects.filter(subjectcode = User_Picked).values_list('classroom_average', flat=True)
        Classroom0 = list(Classroom).count(0)
        Classroom1 = list(Classroom).count(1)
        Classroom2 = list(Classroom).count(2) 

        Personal = Average.objects.filter(subjectcode = User_Picked).values_list('personal_average', flat=True)
        Personal0 = list(Personal).count(0)
        Personal1 = list(Personal).count(1)
        Personal2 = list(Personal).count(2) 

        Comment = Average.objects.filter(subjectcode = User_Picked).values_list('comment_average', flat=True)
        Comment0 = list(Comment).count(0)
        Comment1 = list(Comment).count(1)
        Comment2 = list(Comment).count(2)  

        final = Average.objects.filter(subjectcode = User_Picked).values_list('Final_average', flat=True)
        final0 = list(final).count(0) ## negative
        final1 = list(final).count(1) ## neutral
        final2 = list(final).count(2) ## positive

        
        plt.subplot(4, 2, 1)
        plt.bar(['negative', 'neutral', 'positive'], [Mastery0, Mastery1, Mastery2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Mastery', fontsize=10)
        plt.subplot(4, 2, 2)
        plt.bar(['negative', 'neutral', 'positive'], [Planning0, Planning1, Planning2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Planning', fontsize=10)
        plt.subplot(4, 2, 3)
        plt.bar(['negative', 'neutral', 'positive'], [Communication0, Communication1, Communication2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Communications', fontsize=10)
        plt.subplot(4, 2, 4)
        plt.bar(['negative', 'neutral', 'positive'], [Instructions0, Instructions1, Instructions2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Instructions', fontsize=10)
        plt.subplot(4, 2, 5)
        plt.bar(['negative', 'neutral', 'positive'], [Classroom0, Classroom1, Classroom2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Classroom', fontsize=10)
        plt.subplot(4, 2, 6)
        plt.bar(['negative', 'neutral', 'positive'], [Personal0, Personal1, Personal2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Personal', fontsize=10)
        plt.subplot(4, 2, 7)
        plt.bar(['negative', 'neutral', 'positive'], [Comment0, Comment1, Comment2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Comment', fontsize=10)
        plt.subplot(4, 2, 8)
        plt.bar(['negative', 'neutral', 'positive'], [final0, final1, final2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Final Average', fontsize=10)
        fig = plt.gcf()
        fig.set_size_inches(7, 6.3)
        graph = get_graph()
        plt.clf()
        plt.cla()
        plt.close()
        return graph, final0, final1, final2

def AllDisplay(User_Picked):
        Mastery = Average.objects.values_list('mastery_average', flat=True)
        Mastery0 = list(Mastery).count(0)
        Mastery1 = list(Mastery).count(1)
        Mastery2 = list(Mastery).count(2)

        Planning = Average.objects.values_list('planning_average', flat=True)
        Planning0 = list(Planning).count(0)
        Planning1 = list(Planning).count(1)
        Planning2 = list(Planning).count(2)

        Communication = Average.objects.values_list('communication_average', flat=True)
        Communication0 = list(Communication).count(0)
        Communication1 = list(Communication).count(1)
        Communication2 = list(Communication).count(2)

        Instructions = Average.objects.values_list('instructions_average', flat=True)
        Instructions0 = list(Instructions).count(0)
        Instructions1 = list(Instructions).count(1)
        Instructions2 = list(Instructions).count(2)

        Classroom = Average.objects.values_list('classroom_average', flat=True)
        Classroom0 = list(Classroom).count(0)
        Classroom1 = list(Classroom).count(1)
        Classroom2 = list(Classroom).count(2) 

        Personal = Average.objects.values_list('personal_average', flat=True)
        Personal0 = list(Personal).count(0)
        Personal1 = list(Personal).count(1)
        Personal2 = list(Personal).count(2) 

        Comment = Average.objects.values_list('comment_average', flat=True)
        Comment0 = list(Comment).count(0)
        Comment1 = list(Comment).count(1)
        Comment2 = list(Comment).count(2)  
 
        final = Average.objects.values_list('Final_average', flat=True)
        final0 = list(final).count(0) ## negative
        final1 = list(final).count(1) ## neutral
        final2 = list(final).count(2) ## positive

        
        plt.subplot(4, 2, 1)
        plt.bar(['negative', 'neutral', 'positive'], [Mastery0, Mastery1, Mastery2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Mastery', fontsize=10)
        plt.subplot(4, 2, 2)
        plt.bar(['negative', 'neutral', 'positive'], [Planning0, Planning1, Planning2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Planning', fontsize=10)
        plt.subplot(4, 2, 3)
        plt.bar(['negative', 'neutral', 'positive'], [Communication0, Communication1, Communication2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Communications', fontsize=10)
        plt.subplot(4, 2, 4)
        plt.bar(['negative', 'neutral', 'positive'], [Instructions0, Instructions1, Instructions2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Instructions', fontsize=10)
        plt.subplot(4, 2, 5)
        plt.bar(['negative', 'neutral', 'positive'], [Classroom0, Classroom1, Classroom2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Classroom', fontsize=10)
        plt.subplot(4, 2, 6)
        plt.bar(['negative', 'neutral', 'positive'], [Personal0, Personal1, Personal2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Personal', fontsize=10)
        plt.subplot(4, 2, 7)
        plt.bar(['negative', 'neutral', 'positive'], [Comment0, Comment1, Comment2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Comment', fontsize=10)
        plt.subplot(4, 2, 8)
        plt.bar(['negative', 'neutral', 'positive'], [final0, final1, final2], color=['Red', 'Yellow','Green'])
        plt.ylabel('Final Average', fontsize=10)
        fig = plt.gcf()
        fig.set_size_inches(7, 6.3)
        graph = get_graph()
        plt.clf()
        plt.cla()
        plt.close()
        return graph, final0, final1, final2

def get_graph():
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image = buffer.getvalue()
        graph = base64.b64encode(image)
        graph = graph.decode('utf-8')
        buffer.close()
        return graph