from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

#from dal import autocomplete # RSF 11/11/2019

#from django.db.models.functions import Lower    # RSF 10/11/2019

#from django.template.loader import render_to_string

from clients.models import Client, Firm, OKVED
from .forms import InputClientForm

def base(request) :
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputClientForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        #    return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputClientForm()

    return render(request, 'base.html', {'form': form})

def client_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
#        data = model.objects.using('legacy').filter(client__startswith=q).values_list('client', flat=True)
        data = Client.filter(name__startswith=q).values_list('name', flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")

# Функция поиска по Аякс # RSF 10/11/2019

#def index_view(request):
#    ctx = {}
#    url_parameter = request.GET.get("q")
#
#    if url_parameter:
#        clients = Client.objects.filter(name__icontains=url_parameter)
#    else:
#        clients = Client.objects.all()
#
#    ctx["clients"] = clients
#    if request.is_ajax():
#
#        html = render_to_string(
#            template_name="index.html", context={"clients": clients}
#        )
#        data_dict = {"html_from_view": html}
#        return JsonResponse(data=data_dict, safe=False)
#
#    return render(request, "index.html", context=ctx)

#class ClientAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self) :
#        if not self.request.user.is_authenticated(): 
#            return Client.objects.none() 
#        qs = Client.objects.all() 
#        if self.q: 
#            qs = qs.filter(title__istartswith=self.q) 
#        return qs

class ClientListView(generic.ListView):
    model = Client
    paginate_by = 10

class ClientDetailView(generic.DetailView):
    model = Client
    
class FirmListView(generic.ListView):
    model = Firm
    paginate_by = 10

class FirmDetailView(generic.DetailView):
    model = Firm
    
class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = '__all__'

class FirmCreateView(CreateView):
    model = Firm
    template_name = 'firm_new.html'
    fields = '__all__'

