from django.db import models
from django.utils import timezone

#makemigrations - створює інструкції для додавання нової таблиці в базу даних
#migrate - виконує ці інструкції

#Post - публікація. кожен ряд в таблиці - відомості про 1 публікацію
    #кожна його властивість - колонка у таблиці, котра теж назвивається Post 
class Post(models.Model): 
    title = models.CharField(max_length=100) #CharField - тип для короткого тексту
    text = models.TextField() #для зберігання тексту
    created_at = models.DateField(default=timezone.now) #час коли таблиця створена
    post_slug = models.CharField(max_length=80, default="default_post") #коротка назва поста для url
    img = models.ImageField(default = 'blog/static/img/default.jpeg', upload_to='blog/static/img', height_field=None, width_field=None,
                             max_length=200, verbose_name="Картинка для поста") #поле для зображення
        #upload_to='' - папка для завантаження
        #static -  статичні файли 
        #max_length=200 - максимальна довжина посилання на зображення
    def save(self, *arg, **kwargs): #ф-ція для збереження картинок на сайт, < зображення
        super().save() #збереження для класу models
        img = Image.open(self.img.path) #шлях зображення
        if img.height > 720 or img.width > 1080:
            img.thumbnail((720, 1080))
            img.save(self.img.path)
    def __str__(self): #при викликанні print буде повертатися саме заголовок(title)
        return self.title
