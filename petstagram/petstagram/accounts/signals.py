from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram.accounts.models import Account

USER_MODEL = get_user_model()


@receiver(post_save, sender=USER_MODEL)
def create_account(sender, instance, created, **kwargs):
	if created:
		Account.objects.create(
			user=instance
		)
