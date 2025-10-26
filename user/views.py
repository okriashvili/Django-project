from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# მომხმარებლის ფორმის შესაქმნელად django.contrib.auth.formsდან უნდა დავაიმპორტოთ UserCreationForm
# ამ ფორმის შექმნა არაა საჭირო რადგანაც djangoს აქვს გაწერილი, მაგრამ შეგვიძლია ჩვენივე ფორმა შევქმნათ და ის გამოვიყენოთ


from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

import user
from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class UserRegistrationView(CreateView):
    model = User
    # ფორმის შემქნა ჩვეინთაც შეგვიძლია, ან შეგვიძლია djangoში ჩაშენებული ფორმა გამოვიყენოთ
    # მაგრამ შეგვიძლია დავამატოთ filedები ფორმაში, მაგ: მეილის ფორმა და ა შ.
    form_class = CustomUserCreationForm
    template_name = 'register.html'

    # რეგისტრაციის დროს success_urlში გვიწერია რომ გადაიყვანოს store ის index გერდზე, ამ შემთხვევაში გაგვიყვანს index გვერდზე, მაგრამ დალოგინებული არ ვვიქნებით
    # გამოიტანს ისეთ გვერდს სადაც მომხმარებელს სჭირდება ვერიფიკაციის გავლა,
    success_url = reverse_lazy('store:index')

    # ამიტომ იმისათვის რომ რეგისტრაციის შემდეგ მომხამრებელი ავტომატურად გადავიდეს index გვერდზე და თან იქნეს დალოგინებული, საჭიროა რომ გადავუტვირთოთ form_valid მეთოდი
    # def form_valid(self, form):
    #     # ფუნქცია უნდა გადავცეთ form
    #     # ვინაიდან მომხმარებელი რეგისტრირდება უნდა ამოვიღოთ user, რომელიც ჩაშენნებულია და ავტომატურად ხვდებს რომ დარეგისტრირებული მომხმარებელზე განახორციელოს წვდომა
    #     # შემდგომ კი დასეივებული ფორმა უნდა გავუტოლოთ userს, რათა რეგისტრაციის დროს შემოსული ფორმა გაუტოლდეს userს
    #     user = form.save()
    #     # შემდგომ ვიყენებთ login მეთოდს
    #     # ვიძახებთ login მეთოდს რომელსაც გადავცემთ დასეივებულ ფორმას და self.request უნდა გადაეცეს
    #     login(self.request, user)
    #     # login მეთოდმა უნდა გააკეთოს რომ დასეივებული იუზერი დაალოგინოს, რომელიც მსგავსად მუშაობს როგორც loginview,
    #     # ამიტომ არ გვჭირდება loginის ფორმის თავიდან შევსება
    #
    #     # ბოლოს კი უნდა დააბრუნოს form_valid გადატვირთული ფუნქციონალი,
    #     # super(). ით გადავტივრტეთ form_valid რომელსაც გადავეცით form
    #     return super().form_valid(form)



# გადატვირთული form_valid მეთოდის იზამს იმას რომ, შემოვა რეგისტრაციის form, რომელიც დასეივდება user ცვლადში,
# და login მეთოდი იზმას იმას რომ ავტომატურად დაალოგინებს დარეგისტრირებულ მომხმარებელს
# და დავაბრუნებინებთ form_valid(form)ს რომელიც ზემოთხსენებულს აკეთებს

# form_valid დან შეგვიძლია რომ ფილდებს დაკომიტებისას შევუცვალოთ მონაცემები,მაგ:
# როდესაც ვავსებთ ფორმა გაეშვება commit რომელიც მონაცემთა ბაზაში ასახავს შემოვყანილ მონაცემებს
# ამისათვის შეგვიძლია form_saveს commit გავუხადოთ False
    def form_valid(self, form):
        # user ის მოანცემების შეყვანისას, მას შემდეგ რა ფრომას დავასეივებთ, ეგრევე არ დაკომიტდეს
        response = super().form_valid(form)

        # user.is_active ფილდი დეფაულტად არის True, მაგრამ შევიცვალეთ Falseით
        # is_active მიანიჭებს მომხმარებელს უფლებას აქტიურია თუ არა

        # user.is_superuser = True
        # user.is_superuser - მიანიჭებს სუპერმომხმარებლის უფლებას
        # მაგრამ ამისათვის user.is_staffიც უნდა ჩავურთოთ Trueზე

        # user.is_staff = True
        # IS_STAFF კი თანამშრომლის სტატისს მიანიჭებს

        # ამის სემდეგ დავასეივეთ user ის


        # ბოლოში კი დავაბრუნოთ form_valid(form) და გადავცეთ form, რომელიც გააკეთებს იმას რაც ზემოთ გვიწერია
        return response
# ამ შემთხვევაში როდესაც მომხმარებელი დარეგისტრირდება, user ის ფორმა დასეივდება როგორც, userს არ ექნება უფლება საიტზე წვდომა განახორციელოს
# is_activeც ჩაშეებულია djangoში რომელიც მომხმარებელს აძლევს წვდომას საიტზე, ამის გათიშვის შემთხვევაში კი საიტზე ვეღარ შევა





# მომხმარებლის დასალოგინებლად უნდა შევქმნათ  კლასი რომელიც უნდა გავხადოთ LoginViewს შვილობილი
class UserLoginView(LoginView):
    # დეფაულტად template_name loginviewში არის login.html, მაგრამ შეგვიძლია გადავუტივრთოთ
    template_name = 'login.html'

    # დეფაულტად login.htmlს მოყვება რომ დალოგინების შემდეგ გადამისამართდეს accounts/profile/ გვერდზე
    # ამიტომ აქ ვიყენებთ next_page მეთოდს სხვა გვერდზე გადასასვლელად, success_urlის მსგავსი ფუნქციონალი აქვს მაგრამ განსხვავდება
    next_page = reverse_lazy('store:index')



# logut ისთვის შევბმნათ view
# როდესაც ვქმნით logout viewს, მას აქვს მხოლოდ post და options მეთოდები, მაგრამ დასალოგაუთებად სისტემა უშცებს get მოთხოვნას,
# 1: ამიტომაც შეგვიძლია მოთხოვნის მეთოდი გადავუტვირთოთ და გავუწეროთ რომ გახდეს get ან > მაგრამ getის გადატვირთვას ჯობია რომ>>>
# 2: რადგანაც დეფაულტად არ გააჩნია get მეთოდი ხოლო დასალოგაუთებლად უშვებს get მოთხოვნას, უნდა შევქმნათ from > html დოკუმენტაციაში და ხელით გავუწეროთ method='post', ხოლო actionში ვუწერთ იმ urls რომელი viewც უნდა გაეშვას
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('store:index')





