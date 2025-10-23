from django.urls import path
from store.views import (
    HomeView, products_json,
    ProductDetailView, ProductCreateView, ProductUpdateView,
    ProductDeleteView, ProductListView
)
from django.views.generic import TemplateView


app_name = "store"

# ყველა ენდფოინთი urls.py გაწერის ნაცვლად უმჯობესია თითოეულ აპლიკაციას შიგნითვე შევუქმნათ urls ფაილი
# და ამავე ფაილში გავუწეროთ ეს ენდფოინთები,
# ხოლო ამ ენდფოინთების ასამუშავებლად კი includesს გამოყენებით წავიღოთ urls.py ფაილში
# ამ მიდგომით თითოეული ენდფოინთი იქნება აპლიკაციაში და მათ გამოსაძახებლად
#ი pathში ჯერ უნდა შევიდეთ აპლიკაციაში შემდეგ კი შევიდეთ ამ ენდფოინთებზე

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    # თუკი routeს ცარიელს დავტოვებთ, მაშინ ენდფოინთის გამოძახების გარეშე გაეშვება ეს გვერდი
    # მარგამ მხოლოდ ერთხელ შეგვიძლია ენდფოინთის ცარეილი დატოვება
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('products.json/', products_json, name='products_json'),
    path('products/',  ProductListView.as_view(), name='product_list'),
    path('products/<int:product_pk>/', ProductDetailView.as_view(), name='product_details'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),



# რადგანაც მეორე პარამეტრიც გადავეცით ფუნქციას, routeში ახალი path უნდა შევუქმნათ, აქ შემოდის ის რითიც უნდა დავიჭიროთ id,
# თუკი მონაცემთა ბაზიდან წამოვა id 3, მაშინ აქ უნდა დაიჭიროს 3იანი, რის შემდეგაც გამოიტანს იმ მონაცემს რომლის ID იქნება 3

# ენდფოინთის შემქნის შემდეგ ინდა დავუწვას / დახრილი ხაზი და <> მეტობა ნაკლებობის ნიშანში უნდა გავუწეროთ
# 1: მონაცემი ტიპი, რა მონაცემის ტიპი უნდა შემოვიდეს
# 2: უშუალოდ ჩვენს მიერ ფუქნციაში გადაცემულ პარამეტრი, რათა ეს პარამეტრი დაიჭიროს, როცა ამ პარამეტრს დაიჭერს,
# ფუქნციაში ეს მონაცემი გაუტოლდება ID ის და ამ აიდით წამოიღებს მონაცემს რომელიც დაგვიბრუნდება ვიზუალურად
# მაგრამ იმ შემთხვევაშ თუკი ID არ არსებობს საიტი გავა ერორზე, იმისათვის რომ ერორზე არ გავიდეს, ვიყენებთ get_object_404, თუ პროდუქტი იქნება დააბრუნებს ამ პროდუქტს
# ხოლო თუ არ იქნება მაშინ გამოიტანს რომ პროდუქტი არ არსებობს / ეს get_object_404 უნდა დავაიმპორტოთ და გამოვიყენოთ ფუქნციაშივე >>>
]



# ფუნქციის შემდეგ გაწერილ nameებს ვიყენებთ იმისათვის რომ html დოკუმენტეი დავაკავშიროთ ერთმანეთს, nameში გაწერილ სახელებს კი ამ კავშირისატვის ვიყენებთ
# ეს კავშირი კი უშუალოდ html დოკუმენტში უნდა შევქმნათ, რისთვისაც ვიყენებთ jinja2 ის ენას
# a href თეგით უნდა დავაკავშიროთ, ხოლო jinjas ენით კუ უნდა შევქმნათ დამაკავშირებელი ლინკი
# {% url 'store:about' %}
# ფიგურულ ფრჩხილებში უნდა დავუწეროთ პროცემტის ნიშანი {% %} შიგნით კი უნდა ავაგოთ url,
# ჯერ უნდა დავუწეროთ url და შემდეგ კი აპლიკაციის დასახელება და ის სახელი რომელიც pathში გავუწერეთ nameში