"""
URL configuration for first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
# პირველრგიში სანად pathში შევუქმნით ენდფოინთს და გავუწერთ ფუქნციას, ეს ფუქნციები უნდა დავაიმპორტოთ
from store.views import index, about



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # მას შემდეგ რაც დავაიმპორტებთ, pathში ჯერ უნდა გავუწეროთ ენდფოინთი, ისევე როგორც flaskში ვუწერდით,
#     # რათა ბრაუზერში ამ ენდფოინთის გამოძახბისას მიაკითხოს იმ ფუნქციას რომელსაც pathში გავუწერთ
#     path('index/' , index, name='index'),
#     # ფუნქციასთან ერთად უნდა დავუწეროთ nameიც, რომელიც შემდეგომში ამ ორ გვერდს შორის დასაკავშირებლად უნდა გამოვიყენოთ
#
#     path('about/', about, name='about'),
# ]

# მაგრამ ყველა ენდფოინთი რომ არ ვწეროთ ხელით,
# ამის ნაცვლად უმჯობესია რომ urls.py  ფაილი შევქმნათ აპლიკაციაში, და უშალოდ ამ ფაილში გავწროთ ენდფოინთები,
# ხოლო ამ ენდფოინთების ასამუშავებლად კი includeის გამოყენებით აქ წამოვიღოთ ეს ენდფოინთები და აქედან ავამუშავოთ
# includes გამოსაყენებლად კი ჯერ path თან ერთად უნდა დავაიმპორტოთ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
# თუკი route ში დავტოვებთ ცარიელს სტრინგს, მაშინ აპლიკაციაში გადასვლა არ მოგვიწევს ენდფოინთების გამოსაძახებლად
# მაგრამ თუკი მეორე აპლიკაციასაც შევქმნით და დავამატებთ, მაშინ ორიცე ცარიელი არ უნდა დავტოვოთ, წინააღმდეგ შემთხვევაში წაიკითხავს იმას რომელიც პირველი წერია
] + debug_toolbar_urls()
# აპლიკაციის ენდფოინთები გავწერეთ უშუალოდ აპლიკაციაშივე შექმნილ urls ფაილში რომელსაც ვიძახებთ includeდან
# ხოლო იმისათვის რომ ამ ენდფოინთებზე შევიდეთ, ჯერ უნდა შევიდეთ უშუალოდ აპლიკაციაში და შემდეგ შევიდეთ აპლიკაციის ენდფოინთებზე
