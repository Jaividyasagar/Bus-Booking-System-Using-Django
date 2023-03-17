from django.shortcuts import render
from django.http import HttpResponse
from .forms import Ticket
from .models import BusDetails

def home(request):
    return render(request,'busapp/home.html')

def busdetails(request):
    buses = BusDetails.objects.all()
    return render(request,'busapp/buses.html',{"buses":buses})

def ticketbookform(request):
    form = Ticket()
    return render(request,'busapp/form.html',{"form":form})


def result(request):
    try:
        if request.method == 'POST':
            busnumber = request.POST.get('busno')
            destiny = request.POST.get('destination')
            travellers = int(request.POST.get('noofpersons'))
        busqueryset = BusDetails.objects.get(bus_no=busnumber)
        bus_number = busqueryset.bus_no
        bus_seatsavl = busqueryset.seats_available
        bus_dest = busqueryset.destinations
        bus_ticketcost = busqueryset.ticket_costs
        bus_time = busqueryset.departure_time
        if travellers<=bus_seatsavl:
            bus_seatsavl = bus_seatsavl - travellers
            BusDetails(bus_no=bus_number,departure_time=bus_time,destinations=bus_dest,seats_available=bus_seatsavl,ticket_costs=bus_ticketcost).save()
            return render(request,'busapp/price.html',{"ticketprice":bus_ticketcost*travellers, "bus_time":bus_time})
        else:
            return HttpResponse("Sorry! Ticket Not booked")
    except Exception as e:
        return HttpResponse(e)
