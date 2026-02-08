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



def send_mail_to_owner_for_bookservice(
    full_name,
    phone_number,
    email,
    service_requirements
):
    subject = "📚 New Book Service Request"

    # Plain text fallback
    text_body = f"""
New Book Service Request

Name: {full_name}
Email: {email}
Phone Number: {phone_number}

Service Requirements:
{service_requirements}
"""

    # HTML email design
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: #ffffff; padding: 25px; border-radius: 8px;">
            
            <h2 style="color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                New Book Service Request
            </h2>

            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone Number:</strong> {phone_number}</p>

            <hr style="border: none; border-top: 1px solid #eee;">

            <p><strong>Service Requirements:</strong></p>
            <p style="white-space: pre-line;">{service_requirements}</p>

       
        </div>
    </body>
    </html>
    """

    send_mail(
     
        subject,
        text_body,
        settings.DEFAULT_FROM_EMAIL,
        ["cooltechservices0226@gmail.com"],  # Owner email
        fail_silently=False,
        html_message=html_body,
    )



def send_mail_to_owner_for_productsell(
    name,
    address,
    product_name,
    description,
    phone_number,
    price
):
    subject = "🛒 New Product Sell Request"

    text_body = f"""
New Product Sell Request

Name: {name}
Address: {address}
Product Name: {product_name}
Description: {description}
Phone Number: {phone_number}
Expected Price: {price}
"""

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: #ffffff; padding: 25px; border-radius: 8px;">
            
            <h2 style="color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                New Product Sell Request
            </h2>

            <p><strong>Name:</strong> {name}</p>
            <p><strong>Address:</strong> {address}</p>

            <hr style="border: none; border-top: 1px solid #eee;">

            <p><strong>Product Name:</strong> {product_name}</p>
            <p><strong>Description:</strong><br>{description}</p>

            <hr style="border: none; border-top: 1px solid #eee;">

            <p><strong>Phone Number:</strong> {phone_number}</p>
            <p><strong>Expected Price:</strong> ₹{price}</p>

         
        </div>
    </body>
    </html>
    """

    send_mail(
        subject,
        text_body,
        settings.DEFAULT_FROM_EMAIL,
        ["cooltechservices0226@gmail.com"],
        fail_silently=False,
        html_message=html_body,
    )




def send_mail_for_review_to_owner(name, rating):
    subject = "New Review Form Submission"

    text_body = f"""
    Hello,

    You have received a new review submission.

    Reviewer Name: {name}
    Rating: {rating} ⭐

    Please check your admin panel for more details.

    Regards,
    CoolTech Services Team
    """

    html_body = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f6f9fc;">
        <div style="max-width: 600px; margin: auto; background: #ffffff; padding: 20px; border-radius: 8px;">
            <h2 style="color: #2c3e50; text-align: center;">📩 New Review Received</h2>
            <p>Hello,</p>

            <p>You have received a new review submission:</p>

            <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;"><strong>Reviewer Name</strong></td>
                    <td style="padding: 10px; border: 1px solid #ddd;">{name}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;"><strong>Rating</strong></td>
                    <td style="padding: 10px; border: 1px solid #ddd;">{rating} ⭐</td>
                </tr>
            </table>

            <p>Please check your admin dashboard for full details.</p>

            <p style="margin-top: 30px;">
                Regards,<br>
                <strong>CoolTech Services Team</strong>
            </p>
        </div>
    </div>
    """

    send_mail(
        subject,
        text_body,
        settings.DEFAULT_FROM_EMAIL,
        ["cooltechservices0226@gmail.com"],
        fail_silently=False,
        html_message=html_body,
    )



