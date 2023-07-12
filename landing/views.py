from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')

def submit_pincode(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        # Perform further processing/validation here

        # Example validation: PIN code should be 6 digits
        if len(pincode) != 6 or not pincode.isdigit():
            error_message = "Invalid PIN code format. Please enter a 6-digit PIN code."
            return render(request, 'landing_page.html', {'error_message': error_message})

        # Process the valid PIN code here
        success_message = "PIN code submitted successfully!"
        return render(request, 'landing_page.html', {'success_message': success_message})
    else:
        return render(request, 'landing_page.html')
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def submit_pincode(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        # Perform further processing/validation here

        # Example validation: PIN code should be 6 digits
        if len(pincode) != 6 or not pincode.isdigit():
            error_message = "Invalid PIN code format. Please enter a 6-digit PIN code."
            return render(request, 'landing_page.html', {'error_message': error_message})

        # Process the valid PIN code here
        success_message = "PIN code submitted successfully!"
        return render(request, 'landing_page.html', {'success_message': success_message})
    else:
        return render(request, 'landing_page.html')
