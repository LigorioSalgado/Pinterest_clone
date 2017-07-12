from django import forms


class SignupForm(forms.Form):  
    

    email = forms.EmailField(
        max_length=100,
        widget = forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"correo@gmail.com"
            }
        )
    )

    username =forms.CharField(max_length=100,
    widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"username"
        }
    ))

    password = forms.CharField(max_length=100,
    widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"password"
        }
    ))

    confirm_password =forms.CharField(max_length=100,
    widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"password"
        }
    ))

    def clean(self):
        cleaned_data = super(SignupForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )



class LoginForm(forms.Form):
    
    username =forms.CharField(max_length=100,
    widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"username"
        }
    ))

    password = forms.CharField(max_length=100,
    widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"password"
        }
    ))

