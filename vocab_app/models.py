from django.db import models
from django.contrib.auth.models import User

class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example_sentence = models.TextField()

    def __str__(self):
        return self.word

class DailyPrompt(models.Model):
    prompt_text = models.TextField()

    def __str__(self):
        return self.prompt_text

class DailyWriteUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    write_up = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
