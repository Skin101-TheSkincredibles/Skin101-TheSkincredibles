from django.shortcuts import render
from .forms import QuizSession

# Create your views here.


def start_session(request):
    # inisiasi tags harusnya
    tags = question_session(request) #gatau ahszhxbw
    return render(request,'quiz_session.html')


def question_session(request):

    tags = []

    type = request.POST.get('type')
#    if type == 'Pembersih/Cleanser':
#        tags.append('cleanser')

#    elif type == 'Pelembab/Moisturizer':
#        tags.append('moisturizer')
    
#    elif type == 'Tabir Surya/Sunscreen':
#        tags.append('sunscreen')

#    elif type == 'Produk tambahan':
#        tags.append('misc')


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

    return type,tags


#def generate_reccomendation(tags):

class Quiz:

    list_of_moisturizer = [] # culik dari database
    list_of_sunscreen = [] # culik dari database
    list_of_serum = [] # culik dari database
    list_of_facewash = [] # culik dari database
    list_of_toner = [] # culik dari database
    list_of_misc = [] # culik dari database
    list_of_tags = [] # culik dari database
     
    def generate_recomendation(tags,type):
        
        products = []
        if type == 'Pembersih/Cleanser':
            products = []

        elif type == 'Pelembab/Moisturizer':
            tags.append('moisturizer')
        
        elif type == 'Tabir Surya/Sunscreen':
            tags.append('sunscreen')

        elif type == 'Produk tambahan':
            tags.append('misc')

    

