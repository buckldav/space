from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    class Departments(models.TextChoices):
        # The All caps single letter is the DB/backend side words
        # and then the lower case letters that are words are what User Joe sees.
        COMMAND = "Command", "Command"      # up way way point up 
        ENGINEERING = "Engineering", "Engineering"  # down way way point down
        TACTICALSECURITY = "Tactical/Security", "Tactical / Security"  # left way way point left
        SCIENCE = "Science", "Science"# right way way point right
        OPERATIONSSYSTEMS = "Operations/Systems", "Operations/Systems"
        LIFESUPPORT_ENV = "LifeSupport/Environmental", "Life Support / Environmental" 
        MEDICAL = "Medical", "Medical"
        HOLOGRAPHIC_RECREATION = "Holographic/Recreation", "Holographic / Recreation"
        AUXSPECIALSYSTEMS = "AuxiliaryAndSpecialSystems", "Auxiliary / Special Systems"
    # Stuff in inventory haves these things to need to has data
    item_name = models.CharField(max_length=500,
                                 default="GenericItemName")
    descriptions = models.CharField(max_length=500,
                                    default=None,
                                    null=True,
                                    blank=True)
    department = models.CharField(
        max_length=50,
        choices=Departments.choices
    )
    is_working = models.BooleanField(default=True)
