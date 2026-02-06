from django.core.mail import send_mail
from django.conf import settings


def send_mail_after_enquirey_form(email,name):
    subject = "We received your enquiry"
    message = (
        "Thank you for contacting us!\n\n"
        "We’ve received your enquiry and our team will get back to you shortly.\n\n"
        "Best regards,\n"
        "Support Team"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


# def send_mail_for_sell_product_form(name,):
#     subject = "Product sell request received"
#     message = (
#         "Thank you for submitting your product for sale.\n\n"
#         "Our team will review the details and contact you if needed.\n\n"
#         "Best regards,\n"
#         "Sales Team"
#     )

#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         [email],
#         fail_silently=False,
#     )



def send_mail_for_book_services(email="cooltechservices0226@gmail.com",name="",phone=""):
    subject = "Service booking confirmation"
    message = (
        "Your service booking has been received successfully.\n\n"
        "We’ll reach out soon with confirmation and next steps.\n\n"
        "Best regards,\n"
        "Service Team"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


def send_mail_for_contact_form(email, name, message):
    subject = "We received your message"
    print(name ,email,message)
    body = (
        f"Hi {name},\n\n"
        "Thank you for contacting us.\n\n"
        "We have received your message and will get back to you shortly.\n\n"
        "Your message:\n"
        f"{message}\n\n"
        "Best regards,\n"
        "Support Team"
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )



def send_mail_to_owner_for_contact(name, email="", message="",contact = False,bookservice=False,sell_product = False):
    subject = ""
    if contact:
        subject = "New Contact Form Submission"
    elif bookservice:
        subject = "New Book Service Form Submission"
    elif sell_product:
        subject = "New Product Sell Form Submission"
    else:
        subject = "New Form Submission"
    body = (
        f"{subject}:\n\n"
        f"Name: {name}\n"
        f"Email: {email }\n\n" if email else ""
        f"Message:\n{message}"
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        ["cooltechservices0226@gmail.com"],  # OWNER EMAIL
        fail_silently=False,
    )
