from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.

def index(request):
    request.session['gold'] = 0
    request.session['feed'] = []
    return render(request, "index.html")

def game_setup(request):
    if request.method == "POST":
        request.session['goal'] = request.POST['goal']
        request.session['turns'] = request.POST['turns']
        request.session['gold'] = 0
        request.session['feed'] = []
        return redirect("/game")
    else:
        return redirect("/")

def game(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['feed'] = []
    return render(request, "game.html")

def process_money(request):
    if request.method == "POST":
        if int(request.session['gold']) < int(request.session['goal']) and int(request.session['turns']) > len(request.session['feed']):
        # x = strftime'(%Y/%m/%d %H:%M %p', gmtime())
            if request.POST['location'] == "Farm":
                amount = random.randint(10, 20)
                print(f"Amount is: {amount}")
                print(f"len of feed: {len(request.session['feed'])}")
                request.session['gold'] += amount
                request.session['feed'].append(f"Earned {amount} golds from the farm! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
            if request.POST['location'] == "Cave":
                amount= random.randint(5, 10)
                request.session['gold'] += amount
                print(f"Amount is: {amount}")
                request.session['feed'].append(f"Earned {amount} golds from the cave! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
            if request.POST['location'] == "House":
                amount = random.randint(2, 5)
                request.session['gold'] += amount
                print(f"Amount is: {amount}")
                request.session['feed'].append(f"Earned {amount} golds from the house! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
            if request.POST['location'] == "Casino":
                amount = random.randint(-50, 50)
                if amount > -1:
                    request.session['gold'] += amount
                    print(f"Amount is: {amount}")
                    request.session['feed'].append(f"Earned {amount} golds from the casino! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
                else:
                    request.session['gold'] += amount
                    request.session['feed'].append(f"Entered a casino and lost {amount} golds... Ouch. {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
            return redirect("/game")
        if int(request.session['goal']) < int(request.session['gold']):
            return redirect("/win")
        elif int(request.session['turns']) == len(request.session['feed']):
            return redirect("/lose")
    else:
        return redirect("/game")

def win(request):
    return render(request, "win.html")

def lose(request):
    return render(request, "lose.html")

def reset(request):
    # request.session.clear()
    # request.session['gold'] = 0
    # request.session['feed'] = []
    return redirect("/")