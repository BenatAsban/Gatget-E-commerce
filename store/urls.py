from django.urls import path
from . import views
from django.http import HttpResponse


def ignore_favicon(request):
    return HttpResponse(status=204)

urlpatterns =[
    path('favicon.ico', ignore_favicon),
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('categories',views.categories,name="categories"),
    path('products/<str:name>',views.productsview,name="products"),
    path('products/<str:cname>/<str:pname>',views.product_details,name="product_details"),

]