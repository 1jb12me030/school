from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import School

def school_listing(request):
    if 'pincode' in request.GET:
        pincode = request.GET['pincode']
        schools = School.objects.filter(pincode=pincode)
    else:
        schools = School.objects.all()

    paginator = Paginator(schools, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school_listing.html', {'page_obj': page_obj})
