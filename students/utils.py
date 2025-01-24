import requests
import urllib.parse
from django.conf import settings

def send_sms(phone_number, message):
    """
    Sends a single English SMS via the EasySendSMS API.
    
    :param phone_number: The recipient's phone number
    :param message: The SMS message text (English, URL-encoded)
    :return: Response dictionary or None if an error occurs
    """
    import requests
    import urllib.parse
    from django.conf import settings

    base_url = settings.EASYSENDSMS_BASE_URL
    username = settings.EASYSENDSMS_USERNAME
    password = settings.EASYSENDSMS_PASSWORD
    api_key = settings.EASYSENDSMS_API_KEY  # New API key
    
    # URL-encode the message
    encoded_message = urllib.parse.quote(message)

    # Construct the request URL with the API key
    url = (
        f"{base_url}?username={username}"
        f"&password={password}"
        f"&from={settings.EASYSENDSMS_SENDER_ID}"
        f"&to={phone_number}"
        f"&text={encoded_message}"
        f"&type=0"  # English messages
        f"&api_key={api_key}"  # Include the API key
    )
    
    try:
        # Send GET request to the API
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Parse JSON response (if API returns JSON)
    except requests.exceptions.RequestException as e:
        print(f"SMS sending failed: {e}")
        return None
