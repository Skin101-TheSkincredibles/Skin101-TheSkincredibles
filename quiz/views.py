from django.shortcuts import render
from productdisplay.models import SkinCareItem,Tags

from .forms import CHOICES
from .forms import QuizSession
from django.http import HttpResponseRedirect
# Create your views here.

class Quiz:
    
    def __init__(self):
        # sementara dummy dulu
        self.list_of_moisturizer = [] # culik dari database --> .objects.all()
        self.list_of_sunscreen = [] # culik dari database
        self.list_of_serum = [] # culik dari database
        self.list_of_facewash = [] # culik dari database
        self.list_of_toner = [] # culik dari database
        self.list_of_misc = [] # culik dari database
        self.list_of_tags = [] # culik dari database

        skincare = SkinCareItem.objects.all()
        self.sort_items(skincare)
        

    # untuk testing
    def set_toner(self,list):
        self.list_of_toner = list

    # sementara, nunggu Display
    def sort_items(self,skincare):

        for item in skincare:

            if item.type == 'cleanser':
                self.list_of_facewash.append(item)

            elif item.type == 'moisturizer':
                self.list_of_moisturizer.append(item)
            
            elif item.type == 'sunscreen':
                self.list_of_sunscreen.append(item)

            elif item.type == 'toner':
                self.list_of_toner.append(item)
            
            elif item.type == 'serum':
                self.list_of_serum.append(item)

            elif item.type == 'misc':
                self.list_of_misc.append(item)


    # self reminder : ASSIGN TAG HARUS BERURUTAN!!
    def generate_recommendation(self,type,tags):
        
        products = []
        if type == 'cleanser':
            products = self.list_of_facewash

        elif type == 'moisturizer':
            products = self.list_of_moisturizer
        
        elif type == 'sunscreen':
            products = self.list_of_sunscreen

        elif type == 'toner':
            products = self.list_of_toner
        
        elif type == 'serum':
            products = self.list_of_serum

        elif type == 'misc':
            products = self.list_of_misc
        
        current_tag = 0

        # The tags must match perfectly
        for tag in tags:

            for product in products:
                if product[current_tag] != tag:
                    products.remove(product)
            
            current_tag = current_tag + 1
        
        return products
    
    # NOTE : Nunggu user
    def add_to_favorite(self,client,product):
        # fave_list = client.users_favorite
        # fave_list.append(product)
        x = 1
    


           

quiz = Quiz()

def start_session(request):
#     #gatau ahszhxbw
    if request.method == 'POST':

        form = QuizSession(request.POST)
        print('form is accepted')

        if form.is_valid():

            print('form is valid')

            tags = []

            print(form.cleaned_data.get('type'))
            iterate = ['oily','sensitive','acne','dry']
            for tag in iterate:
                selected = form.cleaned_data.get(tag)
                print(selected)

                if(selected == 'True'):
                    tags.append(Tags.objects.filter(name=tag))
            
            for item in tags:
                print(item)
            
            if len(tags) == 0:
                tags.append(Tags.objects.filter(name='normal'))
                print(tags[0])
            
            
            print(len(tags))
            
            return HttpResponseRedirect('/quiz/tes')

    else:
        form = QuizSession()

    return render(request,'quiz_session.html',{'form': form})

def generate_recommendation(request):
    client_answer = quiz.question_session(request)
    client_recommendation = quiz.generate_recommendation(client_answer[0],client_answer[1])
    response = {'products': client_recommendation, 'user':request.user}
    return render(request,'quiz_result.html',response)

def test(request):
        #a = ' is this ok'
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CHOICES(request.POST)
        print('its post')
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            selected = form.cleaned_data.get("NOMS")
            print(selected)

            return HttpResponseRedirect('/quiz')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CHOICES()
        

    return render(request, 'tes.html', {'form': form})

def next_session(request):
    #gatau ahszhxbw
    return render(request,'quiz_session.html')

#def generate_reccomendation(tags):



    

