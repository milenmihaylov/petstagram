from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from petstagram import settings
from petstagram.accounts.models import Account

USER_MODEL = get_user_model()


def send_successful_registration_email(user):
	html_message = render_to_string(
		'email/email-greeting.html',
		{'user': user},
	)
	plain_message = strip_tags(html_message)

	send_mail(
		subject='Registration successful',
		message=plain_message,
		html_message=html_message,
		from_email=settings.EMAIL_HOST_USER,
		recipient_list=['milenmihaylov42' + f'+{user.username}' + '@gmail.com']  # user.email TODO add it when user has email
	)


@receiver(post_save, sender=USER_MODEL)
def create_account(sender, instance, created, **kwargs):
	if created:
		Account.objects.create(
			user=instance
		)
		send_successful_registration_email(instance)  # (instance)
