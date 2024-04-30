from django.db import models

# Create your models here.


#投稿についてのテーブルクラス
class NewsPost(models.Model):
    CATEGORY = (('TECH SKILL','tehSkill'),
                ('サッカー・フットサル','soccer_footsal'),
                ('登山','climb'),
                ('食事','food'),)

    title = models.CharField(
            verbose_name='タイトル',
            max_length=200
            )
    content = models.TextField(
              verbose_name='本文'
            )
    image1 = models.ImageField(
             verbose_name='イメージ画像1',
             upload_to = 'photo1'
            )
    image2 = models.ImageField(
             verbose_name='イメージ画像2',
             upload_to = 'photo1',
             blank = True,
             null = True
            )
    category = models.CharField(
               verbose_name='カテゴリ',
               max_length=50,
               choices = CATEGORY
            )

    posted_at = models.DateTimeField(
                verbose_name='投稿日時',
                auto_now_add=True 
            )

    def __str__(self):
        return self.title