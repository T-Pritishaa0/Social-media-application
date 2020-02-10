from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from main.models import User
from friend.models import Friend
from django.contrib.auth.models import login_required
# Create your views here.


class FriendView(TemplateView):
    
    template_name = 'friend/friend.html'

    def get(self, request):
        users  = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        args = {'users': users, 'friends': friends}
        return render(request, self.template_name, args)


@login_required(login_url='account:login')        
@classmethod
def add_friend(cls, current_user, new_friend):
    friend, created = cls.objects.get_or_create(
        current_user=current_user)
    friend.users.add(new_friend)

@login_required(login_url='account:login') 
@classmethod
def delete_friend(cls, current_user, new_friend):
    friend, created = cls.objects.get_or_create(
        current_user=current_user)
    friend.users.remove(new_friend)

@login_required(login_url='account:login')       
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.add_friend(request.user, friend)
    elif operation == 'remove':
        Friend.delete_friend(request.user, friend)
    return redirect('friend:friend')
