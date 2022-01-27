from django.contrib.auth.forms import UserCreationForm
#메소드가 아닌 변수여도 import해올 수 잇음!!!!

class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #여기는 self안해줘도 어차피 상속받으면서 self가 자동으로 입력될 거라 self를 안넣어주는 것임

        self.fields['username'].disabled = True
        #이 부분이 없다면, 그냥 usercreationForm과 차이가 없음
        #이부분을 통해서, username부분을 비활성화 시켜주는 것