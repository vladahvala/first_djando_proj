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
    def __str__(self): #при викликанні print буде повертатися саме заголовок(title)
        return self.title
