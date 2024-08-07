from django.db import models
from django.utils.translation import gettext_lazy as _
# know about gettext_lazy

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Quizzes(models.Model):

    class Meta:
        verbose_name=_("Quiz")
        verbose_name_plural=_('Quizzes')
        ordering=['id']
    
    title=models.CharField(_("Quiz Title"),default=_("New Quiz"), max_length=255) # first argument is verbose name 
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,default=1)  # there can be many quizzes of one category , default=1 means take first category 
    date_created=models.DateTimeField( auto_now_add=True)  # auto_now would be use when we have date_updated field
    def __str__(self) -> str:
        return self.title

# this is abstract model and don't created 
class Updated(models.Model):
    date_updated=models.DateTimeField(_('Last Updated'),auto_now=True)
    class Meta:
        abstract=True

class Question(Updated):

    class Meta:
        verbose_name=_("Question")
        verbose_name_plural=_("Questions")
        ordering=['id']

    SCALE=(
        (0,_('Fundamental')),
        (1,_('Beginner')),
        (2,_('Intermediate')),
        (3,_('Advanced')),
        (4,_('Expert'))
    )

    TYPE=(
        (0,_('Multiple Choice')),
    )

    technique=models.IntegerField(_("Type of question "), choices=TYPE, default=0)  # type of question , like we take multiple choice for now 
    title=models.CharField(_("Title"), max_length=250)
    difficulty=models.IntegerField(_("Difficulty"), choices=SCALE, default=0)
    date_created=models.DateTimeField(_("Date created"), auto_now_add=True)
    is_active =models.BooleanField(_("Active status"),default=False)  # tell whether question is active or not (for quiz)
    quiz=models.ForeignKey(Quizzes,related_name='question',on_delete=models.DO_NOTHING)

class Answer(Updated):
    question=models.ForeignKey(Question,related_name='answer',on_delete=models.DO_NOTHING)
    answer_text=models.CharField(_("Answer Text"), max_length=250)
    is_right=models.BooleanField(default=False)