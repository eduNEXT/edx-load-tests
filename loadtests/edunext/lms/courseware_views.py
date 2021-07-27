from locust import task
import logging

from base import EdunextLmsTasks

logger = logging.getLogger(__name__)

class CoursewareViewsTasks(EdunextLmsTasks):
    """
    Models traffic for endpoints in lms.djangoapps.courseware.views
    """

    @task(1)
    def index(self):
        """
        Request a randomly-chosen top-level page in the course.
        """
        logger.info(f'Current user email: { self.locust._email }')
        path = 'courseware' + self.course_data.courseware_path
        self.get(path, name='courseware:index')

    # @task(50)
    # def index(self):
    #     """
    #     Request a randomly-chosen top-level page in the course.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     path = 'courseware' + self.course_data.courseware_path
    #     self.get(path, name='courseware:index')

    # @task(10)
    # def course_home(self):
    #     """
    #     Requests the main course home page that contains the course outline.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     self.get('course', name='courseware:course_home')

    # @task(10)
    # def info(self):
    #     """
    #     Request the course info tab.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     self.get('info', name='courseware:course_info')

    # @task(4)
    # def progress(self):
    #     """
    #     Request the progress tab.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     self.get('progress', name='courseware:progress')

    # @task(4)
    # def instructor(self):
    #     """
    #     Request the progress tab.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     self.get('instructor', name='instructor:home')

    # @task(1)
    # def about(self):
    #     """
    #     Request the LMS' internal about page for this course.
    #     """
    #     logger.info(f'Current user email: { self.locust._email }')
    #     self.get('about', name='courseware:about')

    # @task(8)
    # def stop(self):
    #     """
    #     Switch to another TaskSet.
    #     """
    #     self.interrupt()