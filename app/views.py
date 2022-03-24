from re import search
from django.shortcuts import redirect, render
from app.forms import CadastroForm
from app.models import Cadastro
from django.core.paginator import Paginator


    #def de configuração da ferramenta de busca

def home(request):
    data = {}                              
    search = request.GET.get('search')
    if search:
        data ['db'] = Cadastro.objects.filter(nome__icontains= search)
    else:
        data['db'] = Cadastro.objects.all()
    return render(request,'index.html', data)


    #Paginação do formulario (desativado por contrapor a ferramenta de busca, futura melhoria)
    
'''def home(request):
    data = {}  
    all = Cadastro.objects.all()            
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request,'index.html', data)'''

def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request,'form.html', data)

    #def de criação e savamento de dados cadastrais 

def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    #def de vizualição de dados

def view(request, pk):
    data = {}
    data ['db'] = Cadastro.objects.get(pk=pk) 
    return render (request, 'view.html', data)

    #def de edição de dados

def edit(request, pk):
    data = {}
    data ['db'] = Cadastro.objects.get(pk=pk) 
    data ['form'] = CadastroForm(instance=data['db'])
    return render (request,'form.html', data)

    #atualização e salvamento de novos dados cadastrais

def update (request, pk):
    data = {}
    data ['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

    #def de exclusao de dados

def delete (request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')




