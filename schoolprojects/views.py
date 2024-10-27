from django.shortcuts import render, get_object_or_404
from .models import Project

all_rooms=[{"Geometrical Chart" : "GC",
           "Number Chart" : "NC",
           "Other Chart" : "OC",
           "Pure Construction" : "PC",
           "Applied Construction" : "AC",
           "Still Model" : "SM",
           "Working Model" : "WM",
           "Puzzle" : "PZ",
           "Games" : "GM",
           "Teaching Aid":"TA",
           "Group project": "GP",
           "Single Project": "SP"}]


def project_list(request):
    projects= list(all_rooms.keys())
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail(request, project):
    returntext=all_rooms[project]
    return render(request, 'projects/projects_details.html', {'project': project,'roomname': returntext})