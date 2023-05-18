from django.urls import path

app_name = 'account_app'


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world' )
]
