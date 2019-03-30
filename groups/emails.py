from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render


def send_invite_email(invite_class, invite_id):
    try:
        invite = invite_class.objects.get(pk=invite_id, status=0)
    except invite_class.DoesNotExist:
        pass
    else:
        from django.template import loader
        html_message = loader.render_to_string(
            'emails/invite_email.html',
            {
              'invite': invite
            }
        )

        text = loader.render_to_string(
            'emails/invite_email.txt',
            {
              'invite': invite
            }
        )

        send_mail(
            subject='New invitation!',
            message=text,
            from_email='feelings@example.com',
            recipient_list=[invite.to_user.email],
            html_message=html_message
        )

        # request = HttpRequest()
        # text = render(request, 'emails/invite_email.txt', context={'invite': invite})
        # html = render(request, 'emails/invite_email.html', context={'invite': invite})
        # send_mail(
        # subject='New invitation!',
        # message=text.content.decode('utf-8'),
        # from_email='feelings@example.com',
        # recipient_list=[invite.to_user.email],
        # html_message=html.content.decode('utf-8')
        # )