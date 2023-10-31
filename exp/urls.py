from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='exp-home'),
    path('all', views.all, name='exp-all'),
    path('auto', views.auto, name='exp-auto'),
    path('ent', views.ent, name='exp-ent'),
    path('fam', views.fam, name='exp-fam'),
    path('food', views.food, name='exp-food'),
    path('ins', views.ins, name='exp-ins'),
    path('tax', views.tax, name='exp-tax'),
    path('travel', views.travel, name='exp-travel'),
    path('util', views.util, name='exp-util'),
    path('add', views.add, name='exp-add'),
    path('sch1', views.sch1, name='exp-sch1'),
    path('imgup', views.imgup, name='exp-imgup'),
    path('imgdp', views.imgdp, name='exp-imgdp'),
    path('budget', views.budget, name='exp-budget'),
    path('editbd', views.editbd, name='exp-editbd'),
    path('report', views.report, name='exp-report'),
    path('sch2', views.sch2, name='exp-sch2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
