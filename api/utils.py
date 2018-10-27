import gzip
import shutil
from django.core.mail import EmailMessage
from core.models import Link
import urllib2
from django.conf import settings
import os


def get_html_data(html_file_link):
    # Extract HTML data in list from the list of link
    extracted_html_data = []
    for link in html_file_link:
        try:
            page = urllib2.urlopen(urllib2.Request(link))
            page = page.read()
        except urllib2.URLError:
            page = "<h1>Requested Page: {link} - Content Not Available</h1>".format(link=link)
        extracted_html_data.append(page)
    return extracted_html_data


def create_html_file(email_id):
    # Create HTML files after extracting the HTML data
    url = list(Link.objects.filter(email=email_id).values_list("url", flat=True))
    page_data = get_html_data(url)
    file_path = []
    for count, item in enumerate(page_data):
        current_file_path = "{dir}/{email}_{count}.html".format(dir=settings.MEDIA_ROOT, email=email_id, count=count + 1)
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        with open(current_file_path, "wb") as html_file:
            file_path.append(current_file_path)
            html_file.write(item)
    return file_path


def email_user(subject, message, from_email, email_id, attachment):
    # Sending Email to user
    email = EmailMessage(subject=subject, body=message, from_email=from_email, to=[email_id])
    email.attach_file(attachment)
    # Todo: https://support.google.com/mail/answer/6590?p=BlockedMessage&visit_id=636762671636310930-237979971&rd=1
    # Gmail doesn't allow to send the zip files. For reference see the above link
    email.send()
    return email


def zip_file(email_id):
    # Creating a zip file
    filenames = create_html_file(email_id)
    zip_file = settings.MEDIA_ROOT + '/{email}.gz'.format(email=email_id)
    for file_name in filenames:
        with open(file_name, 'rb') as f_in:
            with gzip.open(zip_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    email_user("Download Html file", "Please Find the attachment", None, email_id, zip_file)
    return True
