"""
Load test for the edx-platform LMS.
"""
import os
import sys

# due to locust sys.path manipulation, we need to re-add the project root.
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from locust import HttpLocust

from base import EdunextLmsTasks
from courseware_views import CoursewareViewsTasks
from user_views import StudentViewsTasks
from helpers import settings, markers


settings.init(f'edunext_lms.locustfile', required_data=[
    'courses',
    'LOCUST_TASK_SET',
    'LOCUST_MIN_WAIT',
    'LOCUST_MAX_WAIT',
], required_secrets=[
    'USERS_CREDENTIALS'
])

markers.install_event_markers()


class LmsTest(EdunextLmsTasks):
    """
    TaskSet that pulls together all the LMS-related TaskSets into a single unified test.
    """

    tasks = {
        CoursewareViewsTasks: 2,
        StudentViewsTasks: 1,
    }


class LmsLocust(HttpLocust):
    task_set = LmsTest
    min_wait = settings.data['LOCUST_MIN_WAIT']
    max_wait = settings.data['LOCUST_MAX_WAIT']

    def __init__(self, *args, **kwargs):
        super(LmsLocust, self).__init__(*args, **kwargs)
        self._user_id = None
        self._email = None
        self._password = None
        self._is_logged_in = False
        self._is_enrolled = False
