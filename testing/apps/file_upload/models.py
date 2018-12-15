from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def user_directory_path(instance, filename):
   
   # instance mewakili nama class, dimana kita dapat memanggil semua
   # atribute/field yang terdapat pada class tersebut

   # contoh mengambil nilai dari field tahun pada class MyModel
    print (instance.tahun)
    ext = filename.split('.')#[-1]
    filename = '{}.{}'.format(instance.tahun, ext[-1])
    return 'file_{0}/qanun_{1}'.format('qanun', filename)

class MyModel(models.Model):
    tahun = models.IntegerField('tahun', 
        validators=[MinValueValidator(1984), max_value_current_year], 
        default=current_year)
    upload = models.FileField(upload_to=user_directory_path)

