import random


def generate_otp():
    return str(random.randint(100000, 999999))


# Dummy WhatsApp sender
# Replace with Meta WhatsApp API later

def send_whatsapp_otp(phone, otp):
    print(f"Sending OTP {otp} to WhatsApp number {phone}")