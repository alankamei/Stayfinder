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
