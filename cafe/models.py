from secrets import choice
from django.db import models

class Cafe(models.Model):
    store_name = models.CharField(max_length=100)      # 店名
    address = models.CharField(max_length=100)         # 住所
    business_hours = models.CharField(max_length=100)  # 営業時間
    regular_holiday = models.CharField(max_length=100) # 定休日
    wifi = models.CharField(max_length=100)            # WiFi有無 
    access = models.CharField(max_length=100)          # アクセス
    hp = models.CharField(max_length=100)              # ホームページ

    def __str__(self):
        return self.store_name