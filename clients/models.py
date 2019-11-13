from django.db import models
from django.urls import reverse

class Client(models.Model) :
    SEX_KINDS = (
        (None, 'Выберите пол'),
        ('м', 'мужской'),
        ('ж', 'женский'),
    )
    
    CALC_KINDS = (
        (None, 'Выберите тип расчета'),
        ('1', 'наличный'),
        ('2', 'безналичный'),
        ('3', 'перечисление'),
        ('4', 'льгота'),        
    )
    
    name = models.CharField(max_length=50, unique = True, verbose_name = 'Фамилия Имя Отчество:')
#    fio1name = models.CharField(max_length=50)
#    fio2name = models.CharField(max_length=50)
#    fio3name = models.CharField(max_length=50)
    sex = models.TextField(max_length = 1, choices=SEX_KINDS, null = True, verbose_name = 'Пол:')
    type_calc = models.TextField(max_length = 16, choices=CALC_KINDS, null = True, verbose_name = 'Тип расчета:')
    birth = models.DateField(blank = True, null = True, verbose_name = 'Дата рождения:')
    prof = models.CharField(max_length=50, blank = True, null = True, verbose_name = 'Профессия:')
    experience = models.FloatField(blank = True, null = True, verbose_name = 'Стаж работы:');
    firm = models.ForeignKey('Firm', on_delete = models.DO_NOTHING, null = True, verbose_name = 'Место работы:')
    add_info = models.TextField(blank = True, null = True, verbose_name = 'Дополнительная информация:')
    rec_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания записи:') 
    rec_modified = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения записи:') 
    
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])
    
    class Meta: 
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['name']
    
class Firm(models.Model) :
    name = models.CharField(max_length=50, unique = True, verbose_name = 'Наименование:')
    type_ownership = models.CharField(max_length=50, blank = True, null = True, verbose_name = 'Форма собственности:')
    type_econom_activity  = models.ForeignKey('OKVED', on_delete = models.DO_NOTHING, null = True, verbose_name = 'Код по ОКВЭД:')
    add_info = models.TextField(blank = True, null = True, verbose_name = 'Дополнительная информация:')
    rec_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания записи:') 
    rec_modified = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения записи:') 
    
    def get_absolute_url(self):
        return reverse('firm-detail', args=[str(self.id)])
    
    def __str__(self) :
        return self.name
    
    class Meta: 
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name']

class OKVED(models.Model) :
    code = models.CharField(max_length=8, unique = True, verbose_name = 'Код ОКВЭД:')
    name = models.CharField(max_length=100, verbose_name = 'Расшифровка:')
    section = models.CharField(max_length=100, blank = True, null = True, verbose_name = 'Раздел:')
    subsection  = models.CharField(max_length=100, blank = True, null = True, verbose_name = 'Подраздел:')
    add_info = models.TextField(blank = True, null = True, verbose_name = 'Дополнительная информация:')
    rec_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания записи:') 
    rec_modified = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения записи:') 
    
    def __str__(self) :
        return self.code
    
    class Meta: 
        verbose_name_plural = 'Коды ОКВЭД'
        verbose_name = 'Код ОКВЭД'
        ordering = ['code']
