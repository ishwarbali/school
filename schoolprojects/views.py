from django.shortcuts import render, get_object_or_404
from .models import Project
import json

science_fair=[{"name":"Geometrical Chart", "short": "GC","image":"img63.PNG","roomNum":"122","block":"RAMANUJAN"},
         {"name":"Number Chart",  "short": "NC","image":"img63.PNG","roomNum":"1","block":"RAMANUJAN"},
         {"name":"Other Chart",  "short": "OC","image":"img63.PNG","roomNum":"2","block":"RAMANUJAN"},
         {"name":"Pure Construction",  "short": "PC","image":"img64.PNG","roomNum":"4","block":"MADAME CURIE"},
         {"name":"Applied Construction",  "short": "AC","image":"img64.PNG","roomNum":"444","block":"MADAME CURIE"},
         {"name":"Still Model Chart",  "short": "SM","image":"img65.PNG","roomNum":"433","block":"GALILEO"},
         {"name":"Working Model",  "short": "WM","image":"img61.PNG","roomNum":"43","block":"EDISON"},
         {"name":"Puzzle",  "short": "PZ","image":"img61.PNG","roomNum":"87","block":"EDISON"},
         {"name":"Games",  "short": "GC","image":"img64.PNG","roomNum":"8","block":"MADAME CURIE"},
         {"name":"Teaching Aid",  "short": "TA","image":"","roomNum":"76","block":"GALILEO"},
         {"name":"Group project",  "short": "GP","image":"img65.PNG","roomNum":"56","block":"GALILEO"},
         {"name":"Single Project",  "short": "SM","image":"img65.PNG","roomNum":"5","block":"GALILEO"},
         
        
         {"name":"AGARBATHI MAKING ",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"ADAM SMITH"},
         {"name":"BAMBOO PRODUCTS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"JAMES WATT"},
         {"name":"BEADS WORK",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"1","block":"BABBAGE"},
         {"name":"BOOK BINDNG",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"2","block":"BABBAGE"},
         {"name":"BUDDING & LAYERING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"4","block":"PANTHAL"},
         {"name":"COCONUT SHELL WORK",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"444","block":"BABBAGE"},
         {"name":"COIR DOOR MAT",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"433","block":"ADAM SMITH"},
         {"name":"DOLL MAKING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"43","block":"ADAM SMITH"},
         {"name":"ECONOMIC NUTRITIOUS FOOD",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"87","block":"JAMES WATT"},
         {"name":"ELECTRIC WIRING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"8","block":"EDISON"},
         {"name":"ELECTRONICS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"76","block":"NEWTON"},
         {"name":"EMBROIDARY",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"56","block":"ADAM SMITH"},
         {"name":"FABRIC PAINTING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"ADAM SMITH"},
         {"name":"VEGETABLE PRINTING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"EDISON"},
         {"name":"NATURAL FIBRE WORK",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"MENDELEEV"},
         {"name":"GARMENT MAKING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"ADAM SMITH"},
         {"name":"METAL ENGRAVING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"FARADAY"},
         {"name":"CLAY MODELING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"MENDELEEV"},
         {"name":"NET MAKING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"PANTHAL"},
         {"name":"PAPER CRAFT",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":" PLASTER OF PARIS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"JAMES WATT"},
         {"name":"THREAD PATTERN",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":"PALM LEAVE PRODUCTS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"ADAM SMITH"},
         {"name":"CARD CHARTCARD",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":"REXIN CANVAS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"MENDELEEV"},
         {"name":"SCREWINE LEAVE",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"FARADAY"},
         {"name":"WASTE MATERIAL",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"FARADAY"},
         {"name":"PUPPETRY",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"FARADAY"},
         {"name":"SHEET METAL WORK",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"JAMES WATT"},
         {"name":"STUFFED TOYS",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":"UMBRELLA",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":"WOOD CARVING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"BABBAGE"},
         {"name":"WOOD WORK",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"JAMES WATT"},
         {"name":"CHALK MAKING",  "short": "GC","image":"newIMG_6168.PNG","roomNum":"5","block":"JAMES WATT"},
         
         ]
         
         


def project_list(request):
    projects= list(science_fair)
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail(request, name):
    identified_post = next(post for post in science_fair if post["name"] == name)
    
    return render(request, "projects/projects_details.html", {"project": identified_post})



