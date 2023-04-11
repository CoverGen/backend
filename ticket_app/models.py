from django.db import models
from django.contrib.auth.hashers import make_password


# test precommit
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=128)
    telephone = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)


class Planner(models.Model):
    id_planner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Moderator(models.Model):
    id_moderator = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    id_planner = models.ForeignKey(Planner, on_delete=models.CASCADE)


class Assistant(models.Model):
    email = models.EmailField(primary_key=True)
    reference_name = models.CharField(max_length=32)
    id_mod = models.ForeignKey(Moderator, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.TimeField()
    details = models.TextField(help_text="What is your event aboout?")


class Event_Moderators(models.Model):
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE)


class Ticket(models.Model):
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE)
    email_assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    reference_name = models.CharField(max_length=32)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    date_generated = models.DateTimeField(auto_now=True)
    ticket_numer = models.IntegerField()
    n_assistants = models.SmallIntegerField(default=1)
    reusable = models.BooleanField(default=False)


class QR(models.Model):
    id_event_s = models.CharField(max_length=255)
    id_ticket_s = models.CharField(max_length=255)
    # Encryption to implement
