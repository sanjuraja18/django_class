from django.shortcuts import render

def home(requred):
    return render(requred, 'home.html')

def about(requred):
    return render(requred, 'about.html')

def contact(requred):
    return render(requred, 'contact.html')

def search(requred):
    return render(requred, 'search.html')
   
