from django.db import models


# Create your models here.

# ted uz musime dat do settings appku

class Question(models.Model):
    # Each field is represented by an instance of a Field class (instance jsou treba CharField a tak)
    # na zacatku to pojmenujeme  a to se bude pouzivat jako nazev sloupce v databazi a taky v djangu
    # muzeem tomu dat i nas human-readable-forman, jako jsme udelali u publication date, resp. date published
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text