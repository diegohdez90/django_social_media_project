from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import (
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    ListView,
                                    DetailView,
                                )
from groups.models import Group,GroupMember

# Create your views here.
class  CreateView(LoginRequiredMixin):
    fields = ('name','description')
    model = Group

class Singlegroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group
