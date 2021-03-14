from django import forms


#khlee add 21/03/03
class LoginForm(forms.Form):
    # LoginForm 에서 입력받을 값은 2개 (아이디, 패스워드)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)