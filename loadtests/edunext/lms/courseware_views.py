from locust import task
import logging

from .base import EdunextLmsTasks


class CoursewareViewsTasks(EdunextLmsTasks):
    """
    Models traffic for endpoints in lms.djangoapps.courseware.views
    """

    @task(1)
    def index(self):
        """
        Request a randomly-chosen top-level page in the course.
        """
        path = 'courseware' + self.course_data.courseware_path
        self.get(path, name='courseware:index')
