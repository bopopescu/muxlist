from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from muxlist.account.utils import send_new_user_email

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self', blank=True, null=True)
    invites = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.user.__unicode__()

def create_userprofile(sender, instance, created, **kwargs):
    if created:
        print "Making userprofile"
        UserProfile.objects.create(user=instance)
        if NEW_USER_NOTIFICATIONS:
            send_new_user_email(instance)

models.signals.post_save.connect(create_userprofile, sender=User)

class Invite(models.Model):
    owner = models.ForeignKey(User)
    email = models.EmailField()
    code = models.CharField(max_length=32, unique=True, db_index=True)

    def __unicode__(self):
        return u"%s - %s" % (self.owner, self.email)

    class Meta:
        unique_together = ('owner', 'email')

class InviteRequest(models.Model):
    email = models.EmailField(max_length=128, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email
