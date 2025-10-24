from django.contrib.auth.forms import UserCreationForm
# მომხმარებლის ფორმის შესაქმნელად django.contrib.auth.formsდან უნდა დავაიმპორტოთ UserCreationForm
# ამ ფორმის შექმნა არაა საჭირო რადგანაც djangoს აქვს გაწერილი, მაგრამ შეგვიძლია ჩვენივე ფორმა შევქმნათ და ის გამოვიყენოთ


from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class UserRegistrationView(CreateView):
    model = User
    # ფორმის შემქნა ჩვეინთაც შეგვიძლია, ან შეგვიძლია djangoში ჩაშენებული ფორმა გამოვიყენოთ
    # მაგრამ შეგვიძლია დავამატოთ filedები ფორმაში, მაგ: მეილის ფორმა და ა შ.
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'



# მომხმარებლის დასალოგინებლად უნდა შევქმნათ  კლასი რომელიც უნდა გავხადოთ LoginViewს შვილობილი
class UserLoginView(LoginView):
    template_name = 'login.html'

    # დეფაულტად login.htmlს მოყვება რომ დალოგინების შემდეგ გადამისამართდეს accounts/profile/ გვერდზე
    # ამიტომ აქ ვიყენებთ next_page მეთოდს სხვა გვერდზე გადასასვლელად, success_urlის ნაცვლად
    next_page = reverse_lazy('store:index')





