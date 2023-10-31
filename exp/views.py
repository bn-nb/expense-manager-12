import csv
from django.shortcuts import render, redirect
from .models import Expense, Schedule, Image
from djp.settings import BASE_DIR
from datetime import datetime
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

ts_now = int(datetime.timestamp(datetime.now()))
ts_year = ts_now - 31536000
ts_month = ts_now - 2592000
ts_week = ts_now - 604800

exps = [x for x in Schedule.objects.filter(timestamp__lte=ts_now)]
for i in exps:
    t = Expense()
    t.timestamp = i.timestamp
    t.exp_type = i.exp_type
    t.sub_type = i.sub_type
    t.amount = i.amount
    t.user = i.user
    t.save()
    Schedule.objects.filter(sno=i.sno).delete()


@login_required(login_url='login')
def home(request):
    return render(request, 'exp/home.html')


@login_required(login_url='login')
def all(request):
    alltime = {
        'Automobile': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', user=request.user))]),
        'Entertainment': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', user=request.user))]),
        'Family': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', user=request.user))]),
        'Insurance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', user=request.user))]),
        'Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', user=request.user))]),
        'Travel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', user=request.user))]),
        'Utilities': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', user=request.user))]),
    }

    lastyear = {
        'Automobile': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', timestamp__gte=ts_year, user=request.user))]),
        'Entertainment': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', timestamp__gte=ts_year, user=request.user))]),
        'Family': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', timestamp__gte=ts_year, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', timestamp__gte=ts_year, user=request.user))]),
        'Insurance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', timestamp__gte=ts_year, user=request.user))]),
        'Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', timestamp__gte=ts_year, user=request.user))]),
        'Travel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', timestamp__gte=ts_year, user=request.user))]),
        'Utilities': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', timestamp__gte=ts_year, user=request.user))]),
    }

    lastmonth = {
        'Automobile': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', timestamp__gte=ts_month, user=request.user))]),
        'Entertainment': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', timestamp__gte=ts_month, user=request.user))]),
        'Family': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', timestamp__gte=ts_month, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', timestamp__gte=ts_month, user=request.user))]),
        'Insurance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', timestamp__gte=ts_month, user=request.user))]),
        'Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', timestamp__gte=ts_month, user=request.user))]),
        'Travel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', timestamp__gte=ts_month, user=request.user))]),
        'Utilities': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', timestamp__gte=ts_month, user=request.user))]),
    }

    lastweek = {
        'Automobile': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', timestamp__gte=ts_week, user=request.user))]),
        'Entertainment': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', timestamp__gte=ts_week, user=request.user))]),
        'Family': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', timestamp__gte=ts_week, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', timestamp__gte=ts_week, user=request.user))]),
        'Insurance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', timestamp__gte=ts_week, user=request.user))]),
        'Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', timestamp__gte=ts_week, user=request.user))]),
        'Travel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', timestamp__gte=ts_week, user=request.user))]),
        'Utilities': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', timestamp__gte=ts_week, user=request.user))]),
    }
    context = {
        'alltime': alltime,
        'lastmonth': lastmonth,
        'lastyear': lastyear,
        'lastweek': lastweek
    }
    return render(request, 'exp/all.html', context)


@login_required(login_url='login')
def auto(request):
    alltime_auto = {
        'Fuel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Fuel', user=request.user))]),
        'Maintenance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Maintenance', user=request.user))]),
    }

    lastyear_auto = {
        'Fuel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Fuel', timestamp__gte=ts_year, user=request.user))]),
        'Maintenance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Maintenance', timestamp__gte=ts_year, user=request.user))]),
    }

    lastweek_auto = {
        'Fuel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Fuel', timestamp__gte=ts_week, user=request.user))]),
        'Maintenance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Maintenance', timestamp__gte=ts_week, user=request.user))]),
    }

    lastmonth_auto = {
        'Fuel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Fuel', timestamp__gte=ts_month, user=request.user))]),
        'Maintenance': sum([x.amount for x in list(Expense.objects.filter(exp_type='Automobile', sub_type='Maintenance', timestamp__gte=ts_month, user=request.user))]),
    }
    context_auto = {
        'alltime': alltime_auto,
        'lastmonth': lastmonth_auto,
        'lastyear': lastyear_auto,
        'lastweek': lastweek_auto
    }
    return render(request, 'exp/auto.html', context_auto)


@login_required(login_url='login')
def ent(request):
    alltime_ent = {
        'Movies': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Movies', user=request.user))]),
        'Party': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Party', user=request.user))]),
        'Concert': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Concert', user=request.user))]),
        'Sports': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Sports', user=request.user))])
    }

    lastweek_ent = {
        'Movies': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Movies', timestamp__gte=ts_week, user=request.user))]),
        'Party': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Party', timestamp__gte=ts_week, user=request.user))]),
        'Concert': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Concert', timestamp__gte=ts_week, user=request.user))]),
        'Sports': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Sports', timestamp__gte=ts_week, user=request.user))])
    }

    lastmonth_ent = {
        'Movies': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Movies', timestamp__gte=ts_month, user=request.user))]),
        'Party': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Party', timestamp__gte=ts_month, user=request.user))]),
        'Concert': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Concert', timestamp__gte=ts_month, user=request.user))]),
        'Sports': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Sports', timestamp__gte=ts_month, user=request.user))])
    }

    lastyear_ent = {
        'Movies': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Movies', timestamp__gte=ts_year, user=request.user))]),
        'Party': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Party', timestamp__gte=ts_year, user=request.user))]),
        'Concert': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Concert', timestamp__gte=ts_year, user=request.user))]),
        'Sports': sum([x.amount for x in list(Expense.objects.filter(exp_type='Entertainment', sub_type='Sports', timestamp__gte=ts_year, user=request.user))])
    }
    context_ent = {
        'alltime': alltime_ent,
        'lastmonth': lastmonth_ent,
        'lastyear': lastyear_ent,
        'lastweek': lastweek_ent
    }
    return render(request, 'exp/ent.html', context_ent)


@login_required(login_url='login')
def fam(request):

    alltime_fam = {
        'Child_Care': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Child_Care', user=request.user))]),
        'Toys': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Toys', user=request.user))]),
        'Others': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Others', user=request.user))])
    }

    lastyear_fam = {
        'Child_Care': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Child_Care', timestamp__gte=ts_year, user=request.user))]),
        'Toys': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Toys', timestamp__gte=ts_year, user=request.user))]),
        'Others': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Others', timestamp__gte=ts_year, user=request.user))])
    }

    lastweek_fam = {
        'Child_Care': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Child_Care', timestamp__gte=ts_week, user=request.user))]),
        'Toys': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Toys', timestamp__gte=ts_week, user=request.user))]),
        'Others': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Others', timestamp__gte=ts_week, user=request.user))])
    }

    lastmonth_fam = {
        'Child_Care': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Child_Care', timestamp__gte=ts_month, user=request.user))]),
        'Toys': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Toys', timestamp__gte=ts_month, user=request.user))]),
        'Others': sum([x.amount for x in list(Expense.objects.filter(exp_type='Family', sub_type='Others', timestamp__gte=ts_month, user=request.user))])
    }
    context_fam = {
        'alltime': alltime_fam,
        'lastmonth': lastmonth_fam,
        'lastyear': lastyear_fam,
        'lastweek': lastweek_fam
    }
    return render(request, 'exp/fam.html', context_fam)


@login_required(login_url='login')
def food(request):
    alltime_food = {
        'Breakfast': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Breakfast', user=request.user))]),
        'Lunch': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Lunch', user=request.user))]),
        'Dinner': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Dinner', user=request.user))]),
        'Snacks': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Snacks', user=request.user))]),
        'Groceries': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Groceries', user=request.user))])
    }

    lastmonth_food = {
        'Breakfast': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Breakfast', timestamp__gte=ts_month, user=request.user))]),
        'Lunch': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Lunch', timestamp__gte=ts_month, user=request.user))]),
        'Dinner': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Dinner', timestamp__gte=ts_month, user=request.user))]),
        'Snacks': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Snacks', timestamp__gte=ts_month, user=request.user))]),
        'Groceries': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Groceries', timestamp__gte=ts_month, user=request.user))])
    }

    lastyear_food = {
        'Breakfast': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Breakfast', timestamp__gte=ts_year, user=request.user))]),
        'Lunch': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Lunch', timestamp__gte=ts_year, user=request.user))]),
        'Dinner': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Dinner', timestamp__gte=ts_year, user=request.user))]),
        'Snacks': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Snacks', timestamp__gte=ts_year, user=request.user))]),
        'Groceries': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Groceries', timestamp__gte=ts_year, user=request.user))])
    }

    lastweek_food = {
        'Breakfast': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Breakfast', timestamp__gte=ts_week, user=request.user))]),
        'Lunch': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Lunch', timestamp__gte=ts_week, user=request.user))]),
        'Dinner': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Dinner', timestamp__gte=ts_week, user=request.user))]),
        'Snacks': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Snacks', timestamp__gte=ts_week, user=request.user))]),
        'Groceries': sum([x.amount for x in list(Expense.objects.filter(exp_type='Food', sub_type='Groceries', timestamp__gte=ts_week, user=request.user))])
    }
    context_food = {
        'alltime': alltime_food,
        'lastmonth': lastmonth_food,
        'lastyear': lastyear_food,
        'lastweek': lastweek_food
    }
    return render(request, 'exp/food.html', context_food)


@login_required(login_url='login')
def ins(request):
    alltime_ins = {
        'Auto': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Auto', user=request.user))]),
        'Health': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Health', user=request.user))]),
        'Life': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Life', user=request.user))])
    }

    lastmonth_ins = {
        'Auto': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Auto', timestamp__gte=ts_month, user=request.user))]),
        'Health': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Health', timestamp__gte=ts_month, user=request.user))]),
        'Life': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Life', timestamp__gte=ts_month, user=request.user))])
    }

    lastweek_ins = {
        'Auto': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Auto', timestamp__gte=ts_week, user=request.user))]),
        'Health': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Health', timestamp__gte=ts_week, user=request.user))]),
        'Life': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Life', timestamp__gte=ts_week, user=request.user))])
    }

    lastyear_ins = {
        'Auto': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Auto', timestamp__gte=ts_year, user=request.user))]),
        'Health': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Health', timestamp__gte=ts_year, user=request.user))]),
        'Life': sum([x.amount for x in list(Expense.objects.filter(exp_type='Insurance', sub_type='Life', timestamp__gte=ts_year, user=request.user))])
    }
    context_ins = {
        'alltime': alltime_ins,
        'lastmonth': lastmonth_ins,
        'lastyear': lastyear_ins,
        'lastweek': lastweek_ins
    }
    return render(request, 'exp/ins.html', context_ins)


@login_required(login_url='login')
def tax(request):
    alltime_tax = {
        'Property_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Property_Tax', user=request.user))]),
        'Vehicle_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Vehicle_Tax', user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Other', user=request.user))]),
    }

    lastyear_tax = {
        'Property_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Property_Tax', timestamp__gte=ts_year, user=request.user))]),
        'Vehicle_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Vehicle_Tax', timestamp__gte=ts_year, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Other', timestamp__gte=ts_year, user=request.user))]),
    }

    lastweek_tax = {
        'Property_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Property_Tax', timestamp__gte=ts_week, user=request.user))]),
        'Vehicle_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Vehicle_Tax', timestamp__gte=ts_week, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Other', timestamp__gte=ts_week, user=request.user))]),
    }

    lastmonth_tax = {
        'Property_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Property_Tax', timestamp__gte=ts_month, user=request.user))]),
        'Vehicle_Tax': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Vehicle_Tax', timestamp__gte=ts_month, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Tax', sub_type='Other', timestamp__gte=ts_month, user=request.user))]),
    }
    context_tax = {
        'alltime': alltime_tax,
        'lastmonth': lastmonth_tax,
        'lastyear': lastyear_tax,
        'lastweek': lastweek_tax
    }
    return render(request, 'exp/tax.html', context_tax)


@login_required(login_url='login')
def travel(request):
    alltime_travel = {
        'Airplane': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Airplane', user=request.user))]),
        'Bus': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Bus', user=request.user))]),
        'Train': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Train', user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Food', user=request.user))]),
        'Hotel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Hotel', user=request.user))]),
        'Taxi': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Taxi', user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Other', user=request.user))]),
        'Misc': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Misc', user=request.user))]),
    }

    lastmonth_travel = {
        'Airplane': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Airplane', timestamp__gte=ts_month, user=request.user))]),
        'Bus': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Bus', timestamp__gte=ts_month, user=request.user))]),
        'Train': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Train', timestamp__gte=ts_month, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Food', timestamp__gte=ts_month, user=request.user))]),
        'Hotel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Hotel', timestamp__gte=ts_month, user=request.user))]),
        'Taxi': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Taxi', timestamp__gte=ts_month, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Other', timestamp__gte=ts_month, user=request.user))]),
        'Misc': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Misc', timestamp__gte=ts_month, user=request.user))]),
    }

    lastweek_travel = {
        'Airplane': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Airplane', timestamp__gte=ts_week, user=request.user))]),
        'Bus': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Bus', timestamp__gte=ts_week, user=request.user))]),
        'Train': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Train', timestamp__gte=ts_week, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Food', timestamp__gte=ts_week, user=request.user))]),
        'Hotel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Hotel', timestamp__gte=ts_week, user=request.user))]),
        'Taxi': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Taxi', timestamp__gte=ts_week, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Other', timestamp__gte=ts_week, user=request.user))]),
        'Misc': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Misc', timestamp__gte=ts_week, user=request.user))]),
    }

    lastyear_travel = {
        'Airplane': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Airplane', timestamp__gte=ts_year, user=request.user))]),
        'Bus': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Bus', timestamp__gte=ts_year, user=request.user))]),
        'Train': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Train', timestamp__gte=ts_year, user=request.user))]),
        'Food': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Food', timestamp__gte=ts_year, user=request.user))]),
        'Hotel': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Hotel', timestamp__gte=ts_year, user=request.user))]),
        'Taxi': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Taxi', timestamp__gte=ts_year, user=request.user))]),
        'Other': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Other', timestamp__gte=ts_year, user=request.user))]),
        'Misc': sum([x.amount for x in list(Expense.objects.filter(exp_type='Travel', sub_type='Misc', timestamp__gte=ts_year, user=request.user))]),
    }
    context_travel = {
        'alltime': alltime_travel,
        'lastmonth': lastmonth_travel,
        'lastyear': lastyear_travel,
        'lastweek': lastweek_travel
    }
    return render(request, 'exp/travel.html', context_travel)


@login_required(login_url='login')
def util(request):
    alltime_util = {
        'Water': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Water', user=request.user))]),
        'Television': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Television', user=request.user))]),
        'Electrical': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Electrical', user=request.user))]),
        'Gas': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Gas', user=request.user))]),
        'Internet': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Internet', user=request.user))]),
        'Telephone': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Telephone', user=request.user))]),
    }

    lastmonth_util = {
        'Water': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Water', timestamp__gte=ts_month, user=request.user))]),
        'Television': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Television', timestamp__gte=ts_month, user=request.user))]),
        'Electrical': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Electrical', timestamp__gte=ts_month, user=request.user))]),
        'Gas': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Gas', timestamp__gte=ts_month, user=request.user))]),
        'Internet': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Internet', timestamp__gte=ts_month, user=request.user))]),
        'Telephone': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Telephone', timestamp__gte=ts_month, user=request.user))]),
    }

    lastyear_util = {
        'Water': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Water', timestamp__gte=ts_year, user=request.user))]),
        'Television': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Television', timestamp__gte=ts_year, user=request.user))]),
        'Electrical': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Electrical', timestamp__gte=ts_year, user=request.user))]),
        'Gas': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Gas', timestamp__gte=ts_year, user=request.user))]),
        'Internet': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Internet', timestamp__gte=ts_year, user=request.user))]),
        'Telephone': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Telephone', timestamp__gte=ts_year, user=request.user))]),
    }

    lastweek_util = {
        'Water': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Water', timestamp__gte=ts_week, user=request.user))]),
        'Television': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Television', timestamp__gte=ts_week, user=request.user))]),
        'Electrical': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Electrical', timestamp__gte=ts_week, user=request.user))]),
        'Gas': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Gas', timestamp__gte=ts_week, user=request.user))]),
        'Internet': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Internet', timestamp__gte=ts_week, user=request.user))]),
        'Telephone': sum([x.amount for x in list(Expense.objects.filter(exp_type='Utilities', sub_type='Telephone', timestamp__gte=ts_week, user=request.user))]),
    }
    context_util = {
        'alltime': alltime_util,
        'lastmonth': lastmonth_util,
        'lastyear': lastyear_util,
        'lastweek': lastweek_util
    }
    return render(request, 'exp/util.html', context_util)


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        rec = Expense()
        rec.timestamp = int(datetime.timestamp(datetime.strptime(request.POST.get('timestamp').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        rec.exp_type = request.POST.get('exp_type')
        rec.sub_type = request.POST.get('sub_type')
        rec.amount = int(request.POST.get('amount'))
        rec.user = request.user
        rec.save()
        return redirect('exp-home')
    return render(request, 'exp/add.html')


@login_required(login_url='login')
def sch1(request):
    if request.method == 'POST':
        rec = Schedule()
        rec.timestamp = int(datetime.timestamp(datetime.strptime(request.POST.get('timestamp').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        rec.exp_type = request.POST.get('exp_type')
        rec.sub_type = request.POST.get('sub_type')
        rec.amount = int(request.POST.get('amount'))
        rec.user = request.user
        rec.save()
        return redirect('exp-home')
    return render(request, 'exp/sch1.html')


@login_required(login_url='login')
def imgup(request):
    ts_now = int(datetime.timestamp(datetime.now()))
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            return redirect('exp-home')
    else:
        form = ImageForm()
    return render(request, 'exp/imgup.html', {'form': form, 'default': ts_now})


@login_required(login_url='login')
def imgdp(request):
    if request.method == 'GET':
        images = Image.objects.filter(user=request.user)
        return render(request, 'exp/imgdp.html', {'receipt_images': images})


@login_required(login_url='login')
def budget(request):
    if request.method == 'POST':
        ref_data = {}
        with open(str(BASE_DIR) + '/media/budget.txt') as file:
            data = file.readlines()
            for a in range(1, 9):
                ref_data[f'{a}'] = int(data[a - 1][:-1])
        ref_data['t1'] = int(datetime.timestamp(datetime.strptime(request.POST.get('time1').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        ref_data['t2'] = int(datetime.timestamp(datetime.strptime(request.POST.get('time2').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        html = ''
        data1 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Automobile').order_by('sub_type', 'timestamp'))
        data2 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Entertainment').order_by('sub_type', 'timestamp'))
        data3 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Family').order_by('sub_type', 'timestamp'))
        data4 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Food').order_by('sub_type', 'timestamp'))
        data5 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Insurance').order_by('sub_type', 'timestamp'))
        data6 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Tax').order_by('sub_type', 'timestamp'))
        data7 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Travel').order_by('sub_type', 'timestamp'))
        data8 = list(Expense.objects.filter(timestamp__gte=ref_data['t1'], timestamp__lte=ref_data['t2'], exp_type__iexact='Utilities').order_by('sub_type', 'timestamp'))

        b1 = ref_data['1']
        net1 = b1 - sum([x.amount for x in data1])
        if data1:
            html += f'''<tr>
              <th>{data1[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data1[0].timestamp)} </td>
              <td >{data1[0].sub_type} </td>
              <td >{data1[0].amount} </td>
              <td rowspan={len(data1)}> Automobile </td>
              <td rowspan={len(data1)}> { b1 } </td>
              <td rowspan={len(data1)}> { net1 } </td>'''
            if net1 > 0:
                html += f"<td rowspan={len(data1)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data1)} style='background-color: crimson'>RISK</td></tr>"
            if data1[1:]:
                for rec in data1[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b2 = ref_data['2']
        net2 = b2 - sum([x.amount for x in data2])
        if data2:
            html += f'''<tr>
              <th>{data2[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data2[0].timestamp)} </td>
              <td >{data2[0].sub_type} </td>
              <td >{data2[0].amount} </td>
              <td rowspan={len(data2)}> Entertainment </td>
              <td rowspan={len(data2)}> { b2 } </td>
              <td rowspan={len(data2)}> { net2 } </td>'''
            if net2 > 0:
                html += f"<td rowspan={len(data2)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data2)} style='background-color: crimson'>RISK</td></tr>"
            if data2[1:]:
                for rec in data2[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b3 = ref_data['3']
        net3 = b3 - sum([x.amount for x in data3])
        if data3:
            html += f'''<tr>
              <th>{data3[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data3[0].timestamp)} </td>
              <td >{data3[0].sub_type} </td>
              <td >{data3[0].amount} </td>
              <td rowspan={len(data3)}> Family </td>
              <td rowspan={len(data3)}> { b3 } </td>
              <td rowspan={len(data3)}> { net3 } </td>'''
            if net3 > 0:
                html += f"<td rowspan={len(data3)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data3)} style='background-color: crimson'>RISK</td></tr>"
            if data3[1:]:
                for rec in data3[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b4 = ref_data['4']
        net4 = b4 - sum([x.amount for x in data4])
        if data4:
            html += f'''<tr>
              <th>{data4[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data4[0].timestamp)} </td>
              <td >{data4[0].sub_type} </td>
              <td >{data4[0].amount} </td>
              <td rowspan={len(data4)}> Food </td>
              <td rowspan={len(data4)}> { b4 } </td>
              <td rowspan={len(data4)}> { net4 } </td>'''
            if net4 > 0:
                html += f"<td rowspan={len(data4)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data4)} style='background-color: crimson'>RISK</td></tr>"
            if data4[1:]:
                for rec in data4[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b5 = ref_data['5']
        net5 = b5 - sum([x.amount for x in data5])
        if data5:
            html += f'''<tr>
              <th>{data5[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data5[0].timestamp)} </td>
              <td >{data5[0].sub_type} </td>
              <td >{data5[0].amount} </td>
              <td rowspan={len(data5)}> Insurance </td>
              <td rowspan={len(data5)}> { b5 } </td>
              <td rowspan={len(data5)}> { net5 } </td>'''
            if net5 > 0:
                html += f"<td rowspan={len(data5)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data5)} style='background-color: crimson'>RISK</td></tr>"
            if data5[1:]:
                for rec in data5[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b6 = ref_data['6']
        net6 = b6 - sum([x.amount for x in data6])
        if data6:
            html += f'''<tr>
              <th>{data6[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data6[0].timestamp)} </td>
              <td >{data6[0].sub_type} </td>
              <td >{data6[0].amount} </td>
              <td rowspan={len(data6)}> Tax </td>
              <td rowspan={len(data6)}> { b6 } </td>
              <td rowspan={len(data6)}> { net6 } </td>'''
            if net6 > 0:
                html += f"<td rowspan={len(data6)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data6)} style='background-color: crimson'>RISK</td></tr>"
            if data6[1:]:
                for rec in data6[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b7 = ref_data['7']
        net7 = b7 - sum([x.amount for x in data7])
        if data7:
            html += f'''<tr>
              <th>{data7[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data7[0].timestamp)} </td>
              <td >{data7[0].sub_type} </td>
              <td >{data7[0].amount} </td>
              <td rowspan={len(data7)}> Travel </td>
              <td rowspan={len(data7)}> { b7 } </td>
              <td rowspan={len(data7)}> { net7 } </td>'''
            if net7 > 0:
                html += f"<td rowspan={len(data7)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data7)} style='background-color: crimson'>RISK</td></tr>"
            if data7[1:]:
                for rec in data7[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''

        b8 = ref_data['8']
        net8 = b8 - sum([x.amount for x in data8])
        if data8:
            html += f'''<tr>
              <th>{data8[0].sno}</th>
              <td style="font-size: 30px;"> {datetime.fromtimestamp(data8[0].timestamp)} </td>
              <td >{data8[0].sub_type} </td>
              <td >{data8[0].amount} </td>
              <td rowspan={len(data8)}> Utilities </td>
              <td rowspan={len(data8)}> { b8 } </td>
              <td rowspan={len(data8)}> { net8 } </td>'''
            if net8 > 0:
                html += f"<td rowspan={len(data8)} style='background-color: lime'>SAFE</td></tr>"
            else:
                html += f"<td rowspan={len(data8)} style='background-color: crimson'>RISK</td></tr>"
            if data8[1:]:
                for rec in data8[1:]:
                    html += f'''<tr>
                  <th>{rec.sno}</th>
                  <td style="font-size: 30px;"> {datetime.fromtimestamp(rec.timestamp)} </td>
                  <td >{rec.sub_type} </td>
                  <td >{rec.amount} </td></tr>'''
        return render(request, 'exp/budget.html', {'html': html})

    else:
        return render(request, 'exp/budget.html')


@login_required(login_url='login')
def report(request):
    if request.method == 'POST':
        time1 = int(datetime.timestamp(datetime.strptime(request.POST.get('time1').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        time2 = int(datetime.timestamp(datetime.strptime(request.POST.get('time2').replace('T', ' ') + ':00', '%Y-%m-%d %H:%M:%S')))
        main_data = [x for x in Expense.objects.filter(user=request.user, timestamp__gte=time1, timestamp__lte=time2)]
        output = []
        for exp in main_data:
            dicty = {"Date": str(datetime.fromtimestamp(exp.timestamp)), "Expense": str(exp.exp_type), 'Sub_Type': str(exp.sub_type), 'Amount': int(exp.amount)}
            output.append(dicty)
        with open(str(BASE_DIR) + '/media/report.csv', 'w+', newline='') as report:
            writer = csv.DictWriter(report, fieldnames=['Date', 'Expense', 'Sub_Type', 'Amount'])
            writer.writeheader()
            writer.writerows(output)
        return render(request, 'exp/report.html', {'output': output})
    return render(request, 'exp/report.html')


@login_required(login_url='login')
def sch2(request):
    exps = [x for x in Schedule.objects.filter(timestamp__lte=ts_now)]
    for i in exps:
        t = Expense()
        t.timestamp = i.timestamp
        t.exp_type = i.exp_type
        t.sub_type = i.sub_type
        t.amount = i.amount
        t.user = i.user
        t.save()
        Schedule.objects.filter(sno=i.sno).delete()
    context = [x for x in Schedule.objects.filter(user=request.user)]
    output = []
    for exp in context:
        dicty = {"Date": str(datetime.fromtimestamp(exp.timestamp)), "Expense": str(exp.exp_type), 'Sub_Type': str(exp.sub_type), 'Amount': int(exp.amount)}
        output.append(dicty)
    return render(request, 'exp/sch2.html', {'output': output})


@login_required(login_url='login')
def editbd(request):
    if request.method == 'POST':
        listy = []
        for a in range(1, 9):
            listy.append(str(request.POST.get(f'{a}')) + '\n')
        with open(str(BASE_DIR) + '/media/budget.txt', 'w+') as file:
            file.writelines(listy)
        return redirect('exp-budget')
    return render(request, 'exp/editbd.html')
