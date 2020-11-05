import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# TestRail Data
testrail_data = {
    'user': os.environ.get('TESTRAIL_USER'),  # your user name
    'password': os.environ.get('TESTRAIL_PASSWORD'),  # your password
    'email': os.environ.get('TESTRAIL_EMAIL'),  # your email
    'url': os.environ.get('TESTRAIL_HOST')  # testrail host
}

# Hosts
main_url = os.environ.get('SUPRO_BACK_HOST')
api_url = os.environ.get('SUPRO_API_HOST')

# Auth data
email = os.environ.get('SUPRO_EMAIL')  # your email
password = os.environ.get('SUPRO_PASSWORD')  # your password

# Testrun IDs
run_id_auth = -1
run_id_main = -1
run_id_tasks = -1

# Release version
build_version = '47402'
