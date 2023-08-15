from django.shortcuts import render

# Create your views here.
def news_view(request):
    return render(request,'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'Yesterady DASAR was released'
    sub_msg2 = 'Planning for aashiqui-3 with Mahesh sir & Sunny'
    sub_msg3 = 'Dont go for movies.....Practice Django.....'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Yesterady IPL was started'
    sub_msg2 = 'Sunday match will be RCB & MI'
    sub_msg3 = 'Gujarat won yesterday match'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_view(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'India Pm was Modi ji'
    sub_msg2 = 'April Budget has released '
    sub_msg3 = 'Telangana CM KCR'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)