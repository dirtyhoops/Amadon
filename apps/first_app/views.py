from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'totalspent' not in request.session:
        request.session['totalspent'] = 0
    if 'totalitem' not in request.session:
        request.session['totalitem'] = 0
    if 'itemprice' not in request.session:
        request.session['itemprice'] = 0
    return render(request, "first_app/index.html")

def checkout(request):
    checkoutinfo = {
        'total_a': request.session['total'],
        'totalspent_a': request.session['totalspent'],
        'totalitem_a': request.session['totalitem'],
        'itemprice_a': request.session['itemprice']
    }
    return render(request, "first_app/checkout.html", checkoutinfo)

def buy(request):
    if request.method == 'POST':
        itemid = request.POST.get("itemid")
        quantity = float(request.POST['quantity'])
        
        if itemid == "1":
            request.session['total'] = 19.99 * quantity
            request.session['itemprice'] = 19.99
        if itemid == "2":
            request.session['total'] += 29.99 * quantity
            request.session['itemprice'] = 29.99
        if itemid == "3":
            request.session['total'] += 4.99 * quantity
            request.session['itemprice'] = 4.99
        if itemid == "4":
            request.session['total'] += 49.99 * quantity
            request.session['itemprice'] = 49.99
        request.session['totalspent']+= request.session['total']

        print("total is ", request.session['totalspent'])
       
        #adds 1 to the total item counter
        request.session['totalitem'] += int(1*quantity)

        return redirect('/checkout')


def clear(request):
    request.session.clear()

    return redirect('/')
