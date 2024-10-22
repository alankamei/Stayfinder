from django.shortcuts import render

from .models import AdsSlide, Hotel, Room
# Create your views here.

def home(request):

    ads_list = AdsSlide.objects.all()
    picked_hotel_list = Hotel.objects.all().filter(picked_of_day=True)
    top_ten_room_list = Room.objects.all().filter(top_ten=True)


    context={
        "ads_list":ads_list,
        "picked_hotel_list":picked_hotel_list,
        "top_ten_room_list":top_ten_room_list
    }
    return render(request, 'home.html',context)


def hotels(request):
    hotel_lists = Hotel.objects.all()
    
    context={
        "hotel_lists":hotel_lists
    }
    return render(request, 'hotels.html', context)


def hotel_details(request):
    hotel_id=request.GET['hotel']
    
    hotel_details=Hotel.objects.filter(pk=hotel_id)[0]
    room_list=Room.objects.filter(hotel=hotel_details)
    
    context={
        "hotel_details":hotel_details,
        "room_list":room_list
    }
    
    return render(request, 'hotel_details.html', context)