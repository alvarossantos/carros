from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


#ENCAPSULAMENTO PARA VERIFICAR SE O USUARIO ESTA LOGADO, PARA FUNCIONAR
@method_decorator(login_required(login_url='/login/'), name='dispatch')#DISPATCH VERIFICA O METODO DE REQUISIÇÃO
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):#SELF É A INSTANCIA DO OBJETO
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    #RETORNA O DETALHES DO CARRO, COM O PK(ID) DO CARRO

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

