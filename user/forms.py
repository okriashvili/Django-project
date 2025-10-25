# django ში გვაქვს ჩაშენებული ფორმა მომხმარებლის რგისტარაციისათვის,
# მაგრამ შეგვიძლია შევმქნათ ჩვენივე ფორმა, ან გამოვიყენოთ აშენებული და დავამატოთ მოდელები(ფილდები)


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




# ახალი იუზერის ფორმის შესაქმნელად models.pyში უნდა დავწეროთ ახალი კლასი, ახალი ფილდებით, კლასი უნდა გავხადოთ AbstractBaseUserის შვილობილი კლასი, რომელიც ჩაშენებულია djangoში
        # class CustomUser(AbstractBaseUser):
        #     name = models.CharField(max_length=255)
        #     email = models.EmailField(max_length=255, unique=True)
        #     phone = models.CharField(max_length=255)
        #     address = models.CharField(max_length=255)
        #     password1 = models.CharField(max_length=255)
        #     password2 = models.CharField(max_length=255)
        #
# მაგრამ თუკი გვინდა რომ ჩვენი იუზერის ფორმა შევქმნათ და djangoს ფორმა არ გამოვიყენოთ,
# როდესაც შევქმნით პროექტს და გავუშვებთ მიგრაციას, ჯერ settings.py ში უნდა გავუწეროთ რომ გამოიყენოს CustomerUser იუზერის რეგისტრაციისათვის
# AUTH_USER_MODEL = 'appName.CustomUser'
# AUTH_USER_MODELში აპლიკაციის სახელი და კლასის დასახელება
# ოღონდ ეს უნდა შევცვალოთ მანამმ სანამ მიგრაციებს გავუშვებთ, მიგრაციების გაშვების შემდეგ მოგვიწევს მთლიანი მონაცემთა საცავი წავშალოთ და თავიდან გავუშვათ მიგრაცია,
# ამიტომ როდესაც აპლიკაციას შევქმნით მომენტალურად უნდა შევცვალოთ ის თუ რომელი იუზერი გამოიყენოს და ამის შემდეგ გავუშვათ მიგრაცია.


# ან შეგვიძლია მხოლოდ კლასი შევქმნათ და დავუწეროთ pass - არაფერი გააკეთოს, მაგრამ AUTH_USER_MODELის გადატვირთვა მაინც დაგვჭირდება
# და შემდეგომ დავამატოთ ფილდები



# ხოლო თუკი გვინდა რომ დავამატოთ ფილდები, ამისათვის უნდა შევქმნათ ახალი კლასი და გავხადოთ UserCreationForm ის შვილობილი
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')
    phone = forms.CharField(required=False)
    address = forms.CharField(max_length=100)
    first_name = forms.CharField(required=False)
    # Last_name = forms.CharField(required=False)

    # ამის შემდეგ უნდა დავამატოთ ახალი ფილდები და meta კლასში გადავტვირთოთ filds
    # fileds გავატანოთ ახალი ფილდი

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'address', 'first_name', 'last_name', 'password1', 'password2')  # Specify fields here too

# საბოლოოდ კი viewsშიც უნდა გავუწეროთ რომ გამოიტენოთ არა UserCreationForm არამედ ის კლასი რომელიც შევქმენით ფორმის გადასატვირთად

