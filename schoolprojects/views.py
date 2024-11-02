from django.shortcuts import render, get_object_or_404
from .models import Project
import json

science_fair=[
         
         
         
         {"name":"Programme Office",  "short": "GC","image":"OneToNine.PNG","roomNum":"1","block":""},
         {"name":"Judges Room",  "short": "GC","image":"OneToNine.PNG","roomNum":"2","block":""},
         {"name":"Invigilators Room",  "short": "GC","image":"OneToNine.PNG","roomNum":"3","block":""},
         {"name":"Working Model Hs",  "short": "GC","image":"OneToNine.PNG","roomNum":"4","block":""},
         {"name":"Working Model HS&HSS",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Working Model Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"6","block":""},
         {"name":"Improvised Experiments Hs",  "short": "GC","image":"OneToNine.PNG","roomNum":"7","block":""},
         {"name":" Improvised Experiments Hs&Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"8","block":""},
         {"name":"Improvised Experiment Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"9","block":""},
         {"name":"Still Model Hs",  "short": "GC","image":"10to12.PNG","roomNum":"10","block":""},
         {"name":"Still Model Hs &Hss",  "short": "GC","image":"10to12.PNG","roomNum":"11","block":""},
         {"name":"Still Model Hss",  "short": "GC","image":"10to12.PNG","roomNum":"12","block":""},
         {"name":"Green Room (Science Drama)",  "short": "GC","image":"131415.PNG","roomNum":"13","block":""},
         {"name":"Rest Room (Science Drama)",  "short": "GC","image":"131415.PNG","roomNum":"14","block":""},
         {"name":"Talent Search Exam",  "short": "GC","image":"131415.PNG","roomNum":"15","block":""},
         {"name":"Presentation Room (Research Type Project)",  "short": "GC","image":"16To21.PNG","roomNum":"16","block":""},
         {"name":"Rest Room Hs (Research Type Project) ",  "short": "GC","image":"16To21.PNG","roomNum":"17","block":""},
         {"name":"Rest Room Hss (Reasearch Type Project)",  "short": "GC","image":"16To21.PNG","roomNum":"18","block":""},
         {"name":"Teacher Project Presentation &Teaching aid",  "short": "GC","image":"16To21.PNG","roomNum":"19","block":""},
         {"name":"Rest Room (Teacher Project)",  "short": "GC","image":"16To21.PNG","roomNum":"20","block":""},
         {"name":"Rest room Teaching Aid",  "short": "GC","image":"16To21.PNG","roomNum":"21","block":""},
         
         
         {"name":"Elocution HS & HSS",  "short": "GC","image":"social.jpg","roomNum":"","block":""},
         {"name":"Working Model HS & HSS",  "short": "GC","image":"social.jpg","roomNum":"","block":""},
         { "name":"Still Model HS & HSS",  "short": "GC","image":"social.jpg","roomNum":"","block":""},
         {"name":"Local History",  "short": "GC","image":"social.jpg","roomNum":"","block":""},
         ]
         
         


def project_list(request):
    projects= list(science_fair)
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail(request, name):
    identified_post = next(post for post in science_fair if post["name"] == name)
    
    return render(request, "projects/projects_details.html", {"project": identified_post})



