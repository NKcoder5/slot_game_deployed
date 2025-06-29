from django.db import models

# Create your models here.

class PlayerScore(models.Model):
    player_name = models.CharField(max_length=100, default='Anonymous')
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player_name} - {self.score}"
