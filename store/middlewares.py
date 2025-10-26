# middlewareს დასაწერად უნდა დავიმპორტოთ django.utils.deprecationდან MiddlewareMixin
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

# ასევე დაგვჭირდება მოდელები, რომელ მოდელებს უნდა ემუშავოს
from store.models import Product

# Middlewareს კი ვწერთ კლასში, რომელიც უნდა იყოს MiddlewareMixinშვილობილი
# ამ middlewaresის ასამუშავებლად ეს კლასი უნდა დავამატოთ settings.pyში middlewareს ლისტში
# როდესაც შემოდის request, ეს მოთხოვნა გაივლის ყველა იმ middlewares რომელიც ჩაშენებულია djangoში,
# middlewareში თუკი დავამატებთ, ჩვენს შექმნილ middlewares, ავტომატურად ამასაც გაივლის და ამოქმედება ფუნქციონალი
# რომელიც დაივლის viewებს ავტომატურად
class ProductCountMiddleware(MiddlewareMixin):

    # viewს დამუშავების დროს რა მოხდეს იწერება process_viewფუქნციაში რომელსაც გადაეცემა
    # self, request, view_func, view_args, view_kwargs - გადაცემული პარამეტრები არის ჩაშენებული djangoში

    # აქ იწერება ის ლოგიკა რომელიც გაზრდის viewს ავტომატურად როდესაც გაეშვება request და გაივლის middlewareებს, შემდგომ კი უკუსვლით დაბრუნდება response,
    def process_view(self, request, view_func, view_args, view_kwargs):
        # ფუნქციას უნდა გადაეცეს resolver რომელიც უნდა დავაიმპორტოთ django.urlsდან და გავუტოლოთ request ის path > resolve(request.path_info
        resolver = resolve(request.path_info)
        #ეს resolve(request.path_info) > ამოიღებს requestის pathს

        # უნდა ჩავრთოთ if ბლოკი რომელიც გააკეთებს > ეს view_nameს უნდა გადავცეთ urlში გაწერილი name
        if resolver.view_name == 'store:product_details':
            # თუკი resolverით pathდან ამოღებული view_name დაემთხვევა urlში გაწერილ nameს
            # მაშინ უნდა ამოვიღოთ ამ პროდუქტის pk > urlს რა product_pk იც შესდის ის ok უნდა დავიჭოროთ
            product_pk = view_kwargs.get('product_pk')
            # product_pk უნდა გახდეს, urlში გადაცემული pk, რომლითაც გავდივართ კონკრეტული აითემის დეტალურ გვერდზე

            # როცა უკვე ამოღებული გვაქვს კონკრეტული პროდუქტის pk, უნდა ამოვიღოთ ამ pkით პროდუქტი, რათა ამ პროდიქტის view გავზარდოთ

            # იმისათვისნ რომ ერორი არ  მოხდეს შეგვიძლია გამოვიყენოთ if ბლოკი, რომ თუ გვაქვს product_pk ამოღებული, მხოლოდ ამ შემთხვევაში გაეშვას if ბლოკი
            if product_pk:
                product = Product.objects.get(pk=product_pk)

                # როცა უკვე პროდუქტიც გვიჭირავს, უნდა გავზარდოთ view და დავასეივოთ ეს ინფორმაცია
                product.views += 1
                product.save(update_fields=['views'])
            # იმისათვის რომ დასეივების დროს ყველა ფილდი არ განახლდეს, შეგვიძლია update_fields გადავცეთ რომ მხოლოდ view დააფდეითოს და არა მთლიანი პროდუქტი
        # ბოლოს ფუნქციის



    # ასევე უნდა შევქმნათ requestის პროცესი, რომელიც ამუშავდება როცა requestშემოვა ჩვენს სერვერზე,
    # ამას ვიყენებთ იმისათვის რომ request მოთხოვნა დავიჭიროთ
    def process_request(self, request):
        # requestის დროს არ არის საჭირო მონაცემი დაბრუნდეს, ამიტომ იმისათვის რომ ფუნქციამ იმუშავოს შეგვიძლია print გამოვიყენოთ და არა return
        print('hello world')

    # requestთან ერთად ასევე გვჭირდება reeponseიც, რომელიც requestმოთხოვნის > response-პასუხს დაიჭერს
    def process_response(self, request, response):
        # process_responseს აუცილებლად უნდა დავაბრუნებინოთ response
        return response
