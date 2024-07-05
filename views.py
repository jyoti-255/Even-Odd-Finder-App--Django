from django.shortcuts import render

# Create your views here.
def home(request):
      if request.GET.get("num"):
        num=int(request.GET.get("num"))
        if num%2==0:
            msg="even"
        else:
           msg="odd"
        return render(request,"home.html",{"msg":msg})
      else:
           return render(request,"home.html")
