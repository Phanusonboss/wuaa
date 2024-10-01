from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Phanuson"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":123,"name":"Phanuson","salary":10000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)
