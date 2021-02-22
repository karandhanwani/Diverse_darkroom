from django.db import models

# Create your models here.
class form(models.Model):
    client_name = models.CharField("Name", max_length=100)
    client_email = models.EmailField("Email", max_length=300)
    client_message = models.TextField("Messages")
    message_draft_on = models.DateTimeField("Drafted On",null=True)

    def __str__(self):
        return f'Name: {self.client_name}\nEmail: {self.client_email}\nMessage: {self.client_message}'
    
