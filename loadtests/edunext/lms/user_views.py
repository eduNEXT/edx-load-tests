import logging

from locust import task
from base import EdunextLmsTasks


class StudentViewsTasks(EdunextLmsTasks):
    """
    Models traffic for endpoints in student.views.
    """

    def _request(self, method, path, *args, **kwargs):
        """
        Overriden method to handle paths that are not realted to the courses.
        """
        return getattr(self.client, method)(path, *args, **kwargs)

    @task(1)
    def dashboard(self):
        """
        Request the dashboard.
        """
        path = '/dashboard'
        self.get(path, name='dashboard')
