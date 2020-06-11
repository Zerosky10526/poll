from django.shortcuts import render
from .models import Poll
from django.views.generic import Listview

# Create your views here.
class POllCreate(Createview):
    model = Poll 
    fields = ["desc",'subject']
    success_url = '/poll/'

class PollList(Listview)
    model = Poll
    fields = ["subject",'desc']
    success_url = '/poll/'

   
class OptionCreate(Createview)
     model  = Option 
     fields = [title]



class PollList(Detalview)
    model = Poll

class PollList




