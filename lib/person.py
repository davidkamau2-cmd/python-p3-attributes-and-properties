#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # initialize internal attributes to safe defaults
        self._name = ""
        self._job = ""

        # Only run validation / setters for attributes explicitly provided
        if name is not None:
            self.name = name
        if job is not None:
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    @property
    def email(self):
        if hasattr(self, "_name"):
            email_name = self._name.lower().replace(" ", ".")
            return f"{email_name}@example.com"
        else:
            return ""

    @property
    def phone(self):
        if hasattr(self, "_job"):
            phone_job = self._job.lower().replace(" ", "")
            return f"({phone_job}) 123-456-7890"
        else:
            return ""

    def __repr__(self):
        return f"Person(name='{self.name}', job='{self.job}')"
