from django.shortcuts import render
from productdisplay.models import Tags

from .forms import QuizSession
from django.http import HttpResponseRedirect


def start_session(request):

    if request.method == 'POST':

        form = QuizSession(request.POST)

        if form.is_valid():

            tags = []

            # - - testing validity -- #
            # NOTE : kalau udah puas ngetes, printnya apus ajaa      

            type = form.cleaned_data.get('type')
            print(type)

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
            
            # NOTE : masih ngasilin error nes sessionnya :[
            #request.session['type'] = type
            #request.session['tags'] = tags
            return HttpResponseRedirect('/display')

    else:
        form = QuizSession()

    return render(request,'quiz_session.html',{'form': form})




    

