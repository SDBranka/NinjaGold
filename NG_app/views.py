from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    request.session['gold'] = 0
    request.session['feed'] = []
    return render(request, "index.html")

def game_setup(request):
    if request.method == "POST":
        request.session['goal'] = int(request.POST['goal'])
        request.session['turns'] = int(request.POST['turns'])
        request.session['gold'] = 0
        request.session['feed'] = []
        request.session['turn_count'] = 0
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
        if request.session['gold'] < request.session['goal'] and request.session['turns'] > 0:
        # x = strftime'(%Y/%m/%d %H:%M %p', gmtime())
            if request.POST['location'] == "Farm":
                amount = random.randint(10, 20)
                request.session['gold'] += amount
                request.session['feed'].append(f"Earned {amount} golds from the farm! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
                request.session['turns'] -= 1
                request.session['turn_count'] +=1
            elif request.POST['location'] == "Cave":
                amount= random.randint(5, 10)
                request.session['gold'] += amount
                request.session['feed'].append(f"Earned {amount} golds from the cave! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
                request.session['turns'] -= 1
                request.session['turn_count'] +=1
            elif request.POST['location'] == "House":
                amount = random.randint(2, 5)
                request.session['gold'] += amount
                request.session['feed'].append(f"Earned {amount} golds from the house! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
                request.session['turns'] -= 1
                request.session['turn_count'] +=1
            elif request.POST['location'] == "Casino":
                amount = random.randint(-50, 50)
                request.session['gold'] += amount
                request.session['turns'] -= 1
                request.session['turn_count'] +=1
                if amount > -1:
                    request.session['feed'].append(f"Earned {amount} golds from the casino! {strftime('%Y/%m/%d %H:%M %p', gmtime())}")
                else:
                    request.session['feed'].append(f"Entered a casino and lost {amount} golds... Ouch. {strftime('%Y/%m/%d %H:%M %p', gmtime())}")                
            if request.session['goal'] < request.session['gold']:
                return redirect("/win")
            if request.session['turns'] == 0:
                return redirect("/lose")
            return redirect("/game")
    else:
        return redirect("/")

def win(request):
    return render(request, "win.html")

def lose(request):
    return render(request, "lose.html")

def reset(request):
    return redirect("/")