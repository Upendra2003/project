from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import UserDetails

def user_details(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user = UserDetails.objects.create(user_name=user_name)
        user_url = request.build_absolute_uri(reverse('user_detail', args=[user_name]))
        user.user_url = user_url
        user.save()
        return redirect(user_url)
    return render(request, 'user/index.html')

def user_detail(request, user_name):
    user = get_object_or_404(UserDetails, user_name=user_name)
    return render(request, 'user/user_detail.html', {'user': user})
