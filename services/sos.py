import webbrowser
import urllib.parse


def send_sos(phone_number, source, destination):
    """
    Opens WhatsApp with a pre-filled emergency message.
    """

    message = f"""
🚨 EMERGENCY ALERT 🚨

I may need help.

📍 Source: {source}
🎯 Destination: {destination}

Please contact me immediately.
"""

    encoded_message = urllib.parse.quote(message)

    url = f"https://wa.me/{phone_number}?text={encoded_message}"

    webbrowser.open_new_tab(url)

    return True


if __name__ == "__main__":

    phone = "91XXXXXXXXXX"

    send_sos(
        phone,
        "Delhi",
        "Noida"
    )