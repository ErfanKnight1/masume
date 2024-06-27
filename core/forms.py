from django import forms


class CustomerForm(forms.Form):
   name = forms.CharField(label="کاربر", max_length=225, widget=forms.TextInput(
attrs={"class": "form-control", "placeholder": "نام و نام خوانوادگی"}))
  
   phone=forms.IntegerField(label="شماره تلفن",widget=forms.NumberInput(
attrs={"class": "form-control", "placeholder": "شماره تلفن"}))
   
   email = forms.EmailField(label="ایمیل", widget=forms.TextInput(attrs={"class": 
"form-control", "placeholder": "ایمیل"}))
  
   text = forms.CharField(label="پیام", max_length=10000, widget=forms.TextInput(
attrs={"class": "form-control", "placeholder": "پیام"}))
   


class ProfileForm(forms.Form):
    # name = forms.CharField(label="کاربر", max_length=225, widget=forms.TextInput(
    # attrs={"class": "form-control", "placeholder": "نام و نام خوانوادگی"}))
  
    # phone=forms.IntegerField(label="شماره تلفن",widget=forms.NumberInput(
    # attrs={"class": "form-control", "placeholder": "شماره تلفن"}))
   
    # email = forms.EmailField(label="ایمیل", widget=forms.TextInput(attrs={"class": 
    # "form-control", "placeholder": "ایمیل"}))
  
    text = forms.CharField(label="متن پیام", max_length=10000, widget=forms.TextInput(
    attrs={"class": "form-control", "placeholder": "لطفا پیام خود را وارد کنید"}))   

   


class RegistraionForm(forms.Form):
    username = forms.CharField(label="نام کاربری", max_length=50, widget=forms.TextInput(
attrs={"class": "form-control form-control-pill", "placeholder": "نام کاربری"}))

    password = forms.IntegerField(label="رمز عبور", widget=forms.NumberInput(
attrs={"class": "form-control form-control-pill", "placeholder": "رمز عبور"}))

    repeat_password = forms.IntegerField(label="تکرار رمز", widget=forms.NumberInput(
attrs={"class": "form-control form-control-pill", "placeholder": "تکرار رمز"}))



class LoginForm(forms.Form):
    user_name = forms.CharField(label="نام کاربری", max_length=80,widget=forms.TextInput(
attrs={"class": "form-control", "placeholder": "نام کاربری"}))
    password = forms.CharField(label="کلمه عبور",widget=forms.NumberInput(
attrs={"class": "form-control", "placeholder": "کلمه عبور"}))