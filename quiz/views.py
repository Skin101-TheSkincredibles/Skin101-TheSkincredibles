from django.shortcuts import render
from productdisplay.models import SkinCareItem,Tags

# Create your views here.

class Quiz:
    
    def __init__(self):
        # sementara dummy dulu
        self.list_of_moisturizer = [] # culik dari database
        self.list_of_sunscreen = [] # culik dari database
        self.list_of_serum = [] # culik dari database
        self.list_of_facewash = [] # culik dari database
        self.list_of_toner = [] # culik dari database
        self.list_of_misc = [] # culik dari database
        self.list_of_tags = [] # culik dari database

    # untuk testing
    def set_toner(self,list):
        self.list_of_toner = list

    # NOTE : ARTINYA ASSIGN TAG HARUS BERURUTAN!!

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
    
    def question_session(self,request):

        tags = []

        type = request.POST.get('type')

        oily = request.POST.get('oily')
        if oily == 'yes':
            tags.append('oily')

        sensitive = request.POST.get('sensitive')
        if sensitive == 'yes':
            tags.append('sensitive')

        acne = request.POST.get('acne')
        if acne == 'yes':
            tags.append('acne')

        dry = request.POST.get('dry')
        if dry == 'yes':
            tags.append('dry')

        # tags is empthy
        if len(tags) == 0:
            tags.append('normal')

        return (type,tags)

           

quiz = Quiz()

def start_session(request):
    #gatau ahszhxbw
    return render(request,'quiz_session.html')

def generate_recommendation(request):
    client_answer = quiz.question_session(request)
    client_recommendation = quiz.generate_recommendation(client_answer[0],client_answer[1])
    response = {'products': client_recommendation}
    return render(request,'quiz_result.html',response)


#def generate_reccomendation(tags):



    

