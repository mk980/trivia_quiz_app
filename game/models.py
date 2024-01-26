from django.db import models


# Create your models here.
class Game(models.Model):
    user = models.CharField(max_length=20, null=False, blank=False)
    game_session = models.ForeignKey(GameSession, 
                                     on_delete=models.PROTECT, 
                                     null=False,
                                     blank=False)
    
    
class GameSession(models.Model):
    
