from chatapp.models import Sharks
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from  django.contrib.auth.mixins import LoginRequiredMixin
from chatapp.forms import AddSharkForm,UpdateSharkForm
class SharkCreateView(CreateView,LoginRequiredMixin):
    template_name="chatbox/add_shark.html"
    form=AddSharkForm
    success_url = '/login1'
    model=Sharks
    fields='__all__'
class SharkUpdateView(UpdateView,LoginRequiredMixin):
    template_name="chatbox/update_shark.html"
    form=UpdateSharkForm
    success_url='/login1'
    model=Sharks
    fields='__all__'
