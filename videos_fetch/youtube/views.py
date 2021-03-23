from django.shortcuts import render
from .models import *
#from .tasks import *
from django.core.paginator import Paginator
from .tasks import do
from background_task.models import Task

# Create your views here.
def index(request):
    pre_task(300)
    all_videos = VideoData.objects.all().order_by('-video_publishing_datetime')
    # print(all_videos)
    paginator = Paginator(all_videos, 20)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    return render(request, 'index.html', {'Videos': videos})

def pre_task(repeat):
    #scheduling task
    print("starting job !!")
    Task.objects.all().delete()
    do(repeat=repeat)
