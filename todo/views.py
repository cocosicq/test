from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from open_facebook import OpenFacebook
from django.http import HttpResponse
import ssl
import requests
from .forms import PostForm
from .forms import RemotePostForm




ssl._create_default_https_context = ssl._create_unverified_context



# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = SocialAccount.objects.get(user=request.user)
            access_token = SocialToken.objects.get(account_id=user, account__provider='facebook')
            idUser = user.uid
            graph = OpenFacebook(access_token=access_token)

            if graph.is_authenticated():

                idPages = (graph.get('me/accounts/'))
                id_Pages_List = [id['id'] for id in idPages['data']]
                id_Pages_List = ", ".join(id_Pages_List)


                id_Page_Access_Token = (graph.get(id_Pages_List, fields='access_token'))
                id_Page_Access_Token = (id_Page_Access_Token['access_token'])


                graph = OpenFacebook(access_token=id_Page_Access_Token)

                feed_url = 'https://graph.facebook.com/'+id_Pages_List+'/feed?message='+post.text+'&access_token='+id_Page_Access_Token
                feed_Request = requests.post(feed_url)

                if(feed_Request.status_code == 200):
                    return render(request, 'todo/home.html', {'user': request.user,'access_token': id_Page_Access_Token,'page_id': id_Pages_List })
                else:
                    return HttpResponse(feed_Request)
                return render(request, 'todo/loginFacebook.html', {'access_token': access_token, 'idUser': idUser})
            else:
                return render(request, 'todo/loginFacebook.html')

    else:
        form = PostForm()
    return render(request, 'todo/add_new_post.html', {'form': form})



def remote_post_new(request):
    if request.method == "POST":
        form = RemotePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = SocialAccount.objects.get(user=request.user)
            access_token = SocialToken.objects.get(account_id=user, account__provider='facebook')
            idUser = user.uid
            graph = OpenFacebook(access_token=access_token)

            if graph.is_authenticated():

                idPages = (graph.get('me/accounts/'))
                id_Pages_List = [id['id'] for id in idPages['data']]
                id_Pages_List = ", ".join(id_Pages_List)


                id_Page_Access_Token = (graph.get(id_Pages_List, fields='access_token'))
                id_Page_Access_Token = (id_Page_Access_Token['access_token'])


                graph = OpenFacebook(access_token=id_Page_Access_Token)

                feed_url = 'https://graph.facebook.com/'+id_Pages_List+'/feed?&published=false&message='+post.text+'&access_token='+id_Page_Access_Token+'&scheduled_publish_time='+str(post.time.timestamp())
                feed_Request = requests.post(feed_url)

                if(feed_Request.status_code == 200):
                    return render(request, 'todo/home.html', {'user': request.user,'access_token': id_Page_Access_Token,'page_id': id_Pages_List })
                else:
                    return HttpResponse(feed_Request)
                return render(request, 'todo/loginFacebook.html', {'access_token': access_token, 'idUser': idUser})
            else:
                return render(request, 'todo/loginFacebook.html')

    else:
        form = RemotePostForm()
    return render(request, 'todo/add_new_remote_post.html', {'form': form})


