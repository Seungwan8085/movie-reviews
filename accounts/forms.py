from django.contrib.auth.forms import UserCreationForm

class UserCreateForm (UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].label=False
        #     self.fields[fieldname].help_text=None
            self.fields[fieldname].widget.attrs.update({'class':'form-control'})

        self.fields['username'].label='사용자ID'
        self.fields['username'].help_text='아이디를 입력하세요'

        self.fields['password1'].label='패스워드'
        self.fields['password1'].help_text=None

        # self.fields['password2'].label='패스워드2'
        self.fields['password2'].label= False
        self.fields['password2'].help_text='다시 한번 암호를 입력하세요'
            