from django.shortcuts import render, get_object_or_404
from .models import Project
import json

science_fair=[
         
         
         
         {"name":"Programme Office",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Judges Room",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Invigilators Room",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Working Model Hs",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Working Model HS&HSS",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Working Model Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Improvised Experiments Hs",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":" Improvised Experiments Hs&Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Improvised Experiment Hss",  "short": "GC","image":"OneToNine.PNG","roomNum":"5","block":""},
         {"name":"Still Model Hs",  "short": "GC","image":"10to12.PNG","roomNum":"5","block":""},
         {"name":"Still Model Hs &Hss",  "short": "GC","image":"10to12.PNG","roomNum":"5","block":""},
         {"name":"Still Model Hss",  "short": "GC","image":"10to12.PNG","roomNum":"5","block":""},
         {"name":"Green Room (Science Drama)",  "short": "GC","image":"131415.PNG","roomNum":"5","block":""},
         {"name":"Rest Room (Science Drama)",  "short": "GC","image":"131415.PNG","roomNum":"5","block":""},
         {"name":"Talent Search Exam",  "short": "GC","image":"131415.PNG","roomNum":"5","block":""},
         {"name":"Presentation Room (Research Type Project)",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         {"name":"Rest Room Hs (Research Type Project) ",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         {"name":"Rest Room Hss (Reasearch Type Project)",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         {"name":"Teacher Project Presentation &Teaching aid",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         {"name":"Rest Room (Teacher Project)",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         {"name":"Rest roomTeaching Aid",  "short": "GC","image":"16To21.PNG","roomNum":"5","block":""},
         ]
         
         


def project_list(request):
    projects= list(science_fair)
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail(request, name):
    identified_post = next(post for post in science_fair if post["name"] == name)
    
    return render(request, "projects/projects_details.html", {"project": identified_post})



