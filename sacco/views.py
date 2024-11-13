from django.http import HttpResponse
from django.shortcuts import render

from sacco.models import customer


# Create your views here.
def test(request):
    # c1 = customer(first_name='John', last_name='Smith', email='john@gmail.com', dob='2006-07-12', gender='Male',weight=45)
    # c1.save()
    # c2 = customer(first_name='Joyce',last_name='millie',email='joyce@gmail.com', dob='2007-07-23',gender='female',weight=45)
    # c2.save()
    c1= customer.objects.get(id=1)
    print(c1)
    d1= deposit(amount=1000,customer=c1)
    d1.save()
    customers = customer.objects.count()
    return HttpResponse(f'ok done we have {customers} customers')