Edunext Load Tests
=========================

This folder contains load tests for edunext SaaS software components. New tests should be developed here.

How to configure the test ?
---------------------------
The configuration file for the specific test should be located in the `settings_files` folder and should have the prefix `edunext_`.
Check the file `edunext_lms.yml.example`.

How to use it ?
--------------
Create virtualenv using python 3.6.7 (`python3.6 -m virtualenv edx_load_tests_venv`), activate it and run:
```
locust \
--host=https://example.edunext.io \ # Site to run the test
-f loadtests/edunext/lms \
--logfile=locust.log \
--loglevel=DEBUG \
--csv=statistics.csv \ # Optional output file name to export statistics automatically
--no-web \ # Optional to run test without web interface
-c 20 \ # Amount of users
-r 1 \ # User Hatch rate
-n 300  # OPtional number the requests to run before test stops

```
