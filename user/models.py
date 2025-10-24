from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# თუკი გვინდა ახალი იუზრის შექმნა მაშინ models.pyში უნდა შევქმნათ ახალი მოდელი,
# Create your models here.
# class CustomUser(AbstractBaseUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     phone = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     password1 = models.CharField(max_length=255)
#     password2 = models.CharField(max_length=255)

# როდესაც შევქმნით პროექტს და სანამ გავუშვებთ მიგრაციას, ჯერ settings.py ში უნდა გავუწეროთ რომ გამოიყენოს CustomerUser იუზერის რეგისტრაციისათვის
# AUTH_USER_MODEL = 'appName.CustomUser'
# AUTH_USER_MODELში აპლიკაციის სახელი და კლასის დასახელება
# ოღონდ ეს უნდა შევცვალოთ მანამმ სანამ მიგრაციებს გავუშვებთ, მიგრაციების გაშვების შემდეგ მოგვიწევს მთლიანი მონაცემთა საცავი წავშალოთ და თავიდან გავუშვათ მიგრაცია,
# ამიტომ როდესაც აპლიკაციას შევქმნით მომენტალურად უნდა შევცვალოთ ის თუ რომელი იუზერი გამოიყენოს და ამის შემდეგ გავუშვათ მიგრაცია.

# ან შეგვიძლია მხოლოდ კლასი შევქმნათ და დავუწეროთ pass - არაფერი გააკეთოს, მაგრამ AUTH_USER_MODELის გადატვირთვა მაინც დაგვჭირდება
# და შემდეგომ დავამატოთ ფილდები