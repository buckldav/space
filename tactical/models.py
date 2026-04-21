from django.db import models

# Create your models here.
class Phasers(models.Model):
    # All the little Jimmies who are point places
    class Direction(models.TextChoices):
        # The All caps single letter is the DB/backend side words
        # and then the lower case letters that are words are what User Joe sees.
        UP = "U", "up"      # up way way point up 
        DOWN = "D", "down"  # down way way point down
        LEFT = "L", "left"  # left way way point left
        RIGHT = "R", "right"# right way way point right

    phaser_is_working = models.BooleanField(default=True) # is the phaser working? Yea or nay? 
    direction_fireing = models.CharField(
        max_length=1, # magic words that mean something probably (max # of chars that DB keep)
        choices=Direction.choices, # these is which choices are the choices that this choses
        default=Direction.RIGHT, # default direction is right
        )
