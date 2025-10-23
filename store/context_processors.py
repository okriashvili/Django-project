# context_processors.py გამოიყენება იმისათვის რომ მოხდეს ბაზიდან მონაცემების წამოღება და შემდგომ html ფაილში გამოსახვა
from store.models import Product, Category


# ნაცვლად იმისა რომ views ფუნქციებში მონაცემები ცალ-ცალკე არ წამოვიღოთ,
# უმჯობესია რომ contect_processorsში წამოვიღოთ მონაცემები და ამ ფაილიდან შევძლოთ მონაცემების გატანება და გამოსახვა htmlფაილებში
# ამისათვის ჯერ modelsდან უნდა დავაიმპორტოთ მონაცემები, შემდგომ შევქმნათ ფუნქცია რომლიდანაც შევძლებთ მონაცემების წამოღებას
# ხოლო წამოღებული მონაცემის დაკავშირება viewsში კი ხდება settings.pyდან სადაც templates ცვლადში, context_processors keyში უნდა ჩავამატოთ შემდეგი სახით>>>
# აპლიკაციის სახელი . ფაილის დასახელება . ფუნქციის სახელი
# ჩვენს შემთხვევაში store.context_processors.global_settings

def global_settings(request):
    site_name = 'my store'
    # site_name გამოგვიტანს იმას რასაც მონაცემად გადავცემთ
    all_products = Product.objects.all()
    # all_category = Category.objects.all()
    last_five_product = all_products.order_by('-created_at')[:5]
    # ხოლო მონაცემის ამოღების შემდეგ უნდა დავაბრუნოთ contextოს სახით
    products = all_products.order_by().select_related('categories')
    return  {'all_products': all_products, 'products': products, 'last_five_product': last_five_product}

