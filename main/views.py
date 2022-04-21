from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm, CustomerUpdateForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Customer

@login_required(login_url="/login")
def home(request):
    customers = Customer.objects.order_by("-created_at").all()

    # Delete the Customer & Ban the User
    # Update the Customer
    if request.method == "POST":
        customer_id = request.POST.get("customer-id")
        user_id = request.POST.get("user-id")
        customer_update = CustomerUpdateForm(request.POST.get("customer-update"))
            
        if customer_id:
            customer = Customer.objects.filter(id=customer_id).first()
            if customer and (customer.manager == request.user or request.user.has_perm("main.delete_customer")):
                customer.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
                # getting server error 
        elif customer_update:
            customer = Customer.objects.filter(id=customer_update).first()
            if customer and (customer.manager == request.user or request.user.has_perm("main.update_customer")):
                if form.is_valid():
                    form.save()
                    return redirect("/home")
                else:
                    form = customer_update
                    return render(request, 'main/create_customer.html', {"form":form})
        
    return render(request, 'main/home.html', {"customers": customers})                
            
@login_required(login_url="/login")
@permission_required("main.add_customer", login_url="/login", raise_exception=True)
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.manager = request.user
            customer.save()
            return redirect("/home")
    else:
        form = CustomerForm()
    return render(request, 'main/create_customer.html', {"form":form})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html',{"form" : form})