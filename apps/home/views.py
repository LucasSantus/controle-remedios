from django.shortcuts import render,redirect
from apps.home.validate import RetornaGrupo
from receitas.models import MedicoPaciente, Receita
from django.contrib.auth.decorators import login_required
from project.settings import GPMedico, GPPaciente

from receitas.models import Agendamento
import datetime

def base(request):
    context = {}
    if request.user.is_authenticated:
        url_path = request.path
        list_path = []
        if len(url_path) == 1:
            list_path.append('/')
        else:
            for url in url_path[1:]:
                if url == '/':
                    break
                else:
                    list_path.append(url)
                
        url_active = "".join(list_path)
    
        date = datetime.datetime.now().date()
        context = {
            'year': date.year,
            'url_active': url_active,
            'idGroup':request.user.idGroup
        }
    return context

@login_required
def ViewHome(request):
    listGroups = [
        {
            'Nome': GPMedico,
            'Url': "ViewDashboardMedico"
        },
        {
            'Nome': GPPaciente,
            'Url': "ViewDashboardPaciente"
        },
    ]

    if request.user.is_authenticated:
        for x in listGroups:
            if RetornaGrupo(request).name == x['Nome']:
                return redirect(x['Url'])

@login_required
def ViewDashboardMedico(request):
    listPacientes = MedicoPaciente.objects.filter(medico = request.user)

    context = {
        "listPacientes": listPacientes,
    }

    return render(request, "home/index.html", context)

@login_required
def ViewDashboardPaciente(request):
    receitas = Receita.objects.filter(medicoPaciente__paciente = request.user).order_by("-pk")
    listReceitas = []
    
    for receita in receitas:
        try:
            agendamento = Agendamento.objects.filter(receita = receita)
        except Agendamento.DoesNotExist:
            agendamento = None
            
        obj = {
            "receita": receita,
            "Agendamento": agendamento,
        }

        listReceitas.append(obj)

    context = {
        "listReceitas": listReceitas,
    }

    return render(request, "home/index.html", context)
