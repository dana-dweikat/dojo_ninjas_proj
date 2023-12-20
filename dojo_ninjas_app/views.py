from django.shortcuts import render , redirect

from dojo_ninjas_app.models import *
# from dojo_ninjas_app.models import Dojos , Ninjas

## Dojos.objects.all() for get (retrive) all dojo   #### Return List
## Dojos.objects.get(id=5) for get one dojo which id = 5 ## Return Object

def root(request):
    # s
    ## Create Vars Used in Index
    context = {'all_dojo':Dojos.objects.all()}
    return render(request,"index.html",context)

def add_dojo(request):
    ## Save From Request Form Post
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        desc = request.POST.get('desc')
        print(name,city,state,desc)
        Dojos.objects.create(
            name= name,
            city=city,
            state=state,
            desc=desc
        )
        print("Created")
        return redirect('home')
    return redirect('home')
    



def add_ninja(request):
    ## For Form (Ninjas)
    ## Linked by action
    if request.method == "POST":
        ## Get Input From Form in Html By (name)
        dojo_id = request.POST.get("dojo_selected") # Catch Value only not Object > Other line to get object by id
        #print(get_dojo_object.city)
        #print(get_dojo_object.name)
        #print(get_dojo_object.ninjas.all())
        get_dojo_object = Dojos.objects.get(id=dojo_id)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Ninjas.objects.create(
            first_name=first_name,
            last_name=last_name,
            dojo_id=get_dojo_object
        )
        print("Created")
    return redirect('home')



