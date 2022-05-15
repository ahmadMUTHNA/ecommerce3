import re
from site import addusersitepackages
from django.shortcuts import render,redirect
from . models import Product,Order,UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
	context = {"product":Product.objects.all()}
	return render(request, 'store/index.html', context)

def datil(request,id):
	product_datil=Product.objects.get(id=id)
	context = {'product_datil':product_datil}
	return render(request, 'store/datil.html', context)

def checkout(request,id):
	name=request.POST.get('name')
	number_order=request.POST.get('nameorder')
	addres=request.POST.get('addres')
	count_order=request.POST.get('count_order')
	number_phone=request.POST.get('number_phone')
	da=Order(name=name,number_Phone=number_phone,addres=addres,number_order=number_order,count_order=count_order)
	if request.method=='POST':
		da.save()	
	product_datil=Product.objects.get(id=id)
	context = {'product_datil':product_datil}
	return render(request, 'store/checkout.html', context)

def main(request):
	context = {}
	return render(request, 'store/main.html', context)

def product(request):
	pro=Product.objects.all()
	name=request.GET.get('productname')
	if name:
		pro=pro.filter(name__icontains=name)

	productDescription=request.GET.get('productDescription')
	if productDescription:
		pro=pro.filter(descriotion__icontains=productDescription)

	firstBrice=request.GET.get('firstBrice')
	lastBrice=request.GET.get('lastBrice')
	if lastBrice and firstBrice:
		if firstBrice.isdigit() and lastBrice.isdigit():
			pro=pro.filter(price__gte=firstBrice,price__lte=lastBrice)




	context = {
		"product":pro,
	}
	return render(request, 'store/product.html', context)

def shose_bage(request):
	context = {"product":Product.objects.filter(category='shose_bage')}
	return render(request, 'store/shose_bage.html', context)
def clothes(request):
	context = {"product":Product.objects.filter(category='clothes')}
	return render(request, 'store/clothes.html', context)

def laptop(request):
	context = {"product":Product.objects.filter(category='laptop')}
	return render(request, 'store/laptop.html', context)
	
def mobile(request):
	context = {"product":Product.objects.filter(category='mobile')}
	return render(request, 'store/mobile.html', context)
def search(request):
	context = {}
	return render(request, 'store/search.html', context)

def login(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		adress=request.POST.get('adress')
		city=request.POST.get('city')
		state=request.POST.get('state')
		zip=request.POST.get('zip')
		email=request.POST.get('email')
		username=request.POST.get('username')
		password=request.POST.get('password')
		if fname and lname and adress and city and state and zip and email and username and password:
			if User.objects.filter(username=username).exists():
				messages.info(request,'the user name is taken')
			else:
				if User.objects.filter(email=email).exists():
					messages.info(request,'the Email is taken')
				else:
					# add users
					user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)		
					user.save()
					#add user profile
					userprofile=UserProfile(user=user,adress=adress,city=city,zip_number=zip,state=state)
					userprofile.save()
					messages.info(request,'create acount')
					Added=True
		else:
			messages.info(request,'chake empty filed')
		messages.info(request,'this is message1')
		return render(request, 'store/login.html',{
			'Added':Added,
		})
	else:
		return render(request, 'store/login.html')
def signin(request):
	
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
		else:
			messages.info(request,"Eror in passowrd or username")
		return redirect('products:signin')
	else:
		return render(request, 'store/signin.html')

def profile(request):
	context = {}
	if request.user.is_authenticated:
		userinfo=UserProfile.objects.get(user=request.user)
		context={"userinfo":userinfo}
	
	return render(request, 'store/profile.html',context)

def logout(request):
		if request.user.is_authenticated:
			auth.logout(request) 

		return redirect('products:home')
def like_product(request,idPro):
	if request.user.is_authenticated:
		like_pro=Product.objects.get(id=idPro)
		if UserProfile.objects.filter(user=request.user,like_product=like_pro).exists():
			pass

		else:
			userprofile=UserProfile.objects.get(user=request.user)
			userprofile.like_product.add(like_pro)
	else:
		messages.info(request,"you must login")
	
	# return ("")
	return redirect('products:datil', idPro)

def show_product_like(request):
	context = {}
	if request.user.is_authenticated:
		userinfo=UserProfile.objects.get(user=request.user)
		pro=userinfo.like_product.all()
		context = {'product':pro}
	
	return render(request, 'store/product.html',context)



def buy(request):
	context = {}
	return render(request, 'store/buy.html', context)
	
	