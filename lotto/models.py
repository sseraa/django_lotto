#데이터 베이스에 들어갈 테이블의 구조를 클래스로 만듦.
from django.db import models
from django.utils import timezone
import random
# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))
        for _ in range(0,self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort() #list 원본 정렬 및 inplace
            self.lottos += str(guess) +'\n' #보여지는 화면에서 줄바꿈

        self.update_date = timezone.now() # generate가 실행되는 순간의 get time
        self.save() #from models.Model #하나 행(from generate) 저장 --like Commit # DB에 반영됨

    def __str__(self): #print(self) 했을때 보이는 형태가 이렇게 -- 설정 안해두면 <타입/클래스 어쩌구 >
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) #pk(id) models.Model의 함수
