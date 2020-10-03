from testrail_api import APIClient
from config import testrail_data as ts, build_version as version
import urllib3


def get_run(run_id):
    return client.send_get('get_run/{}'.format(run_id))


def get_user_by_email(email):
    return client.send_get('get_user_by_email&email={}'.format(email))


def get_case(case_id):
    return client.send_get('get_case/{}'.format(case_id))


def get_cases(run_id, suite_id):
    return client.send_get('get_cases/{}&suite_id={}'.format(run_id, suite_id))


def get_results_for_run(run_id):
    return client.send_get('get_results_for_run/{}'.format(run_id))


def update_case(case_id, run_id, data):
    return client.send_post('update_case/{}'.format(run_id), data)


def get_results_for_case(run_id, case_id):
    return client.send_get('get_results_for_case/{}/{}'.format(run_id, case_id))


def add_result_for_case(run_id, case_id, status):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    data = {'status_id': status, 'comment': 'The result was added automatically.', 'version': version,
            'elapsed': None, 'defects': None, 'assignedto_id': id_user}

    client.send_post('add_result_for_case/{}/{}'.format(run_id, case_id), data)


user = ts['user']
password = ts['password']
email = ts['email']
url = ts['url']

client = APIClient(url, user, password)

id_user = get_user_by_email(email)['id'] if get_user_by_email(email).get('id') else 0

# Для тестов
data = {'status_id': 1, 'comment': None, 'version': '47402', 'elapsed': None, 'defects': None, 'assignedto_id': id_user}
