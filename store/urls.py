from django.urls import path
from . import views
app_name='store' 
urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('<int:id>', views.datil, name="datil"),
	path('checkout/<int:id>', views.checkout, name="checkout"),
	path('main/', views.main, name="main"),
	path('product/', views.product, name="product"),
	path('shose_bage/', views.shose_bage, name="shose_bage"),
	path('clothes/', views.clothes, name="clothes"),
	path('laptop/', views.laptop, name="laptop"),
	path('mobile/', views.mobile, name="mobile"),
	path('search/', views.search, name="search"),
	path('login/', views.login, name="login"),
	path('signin/', views.signin, name="signin"),
	path('profile/', views.profile, name="profile"),
	path('logout/', views.logout, name="logout"),
	path('like<int:idPro>', views.like_product, name="like_product"),
	path('show_product_like/', views.show_product_like, name="show_product_like"),
	path('buy/', views.buy, name="buy"),

]