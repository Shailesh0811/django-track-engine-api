from django.db import models
import json
# Create your models here.

ISSUES_FILE = '/Users/shaileshmohite/Documents/AirTribe/django-track-engine-api/issues.json'
REPORTERS_FILE = '/Users/shaileshmohite/Documents/AirTribe/django-track-engine-api/reporters.json'

from abc import ABC, abstractmethod


def _load_json_array(path):
    """Return a list from JSON file; empty or invalid files become []."""
    try:
        with open(path, 'r') as f:
            raw = f.read().strip()
            if not raw:
                return []
            data = json.loads(raw)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return []

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if '@' not in self.email:
            raise ValueError('Invalid email')

    def persist(self):
        self.validate()
        reporters = _load_json_array(REPORTERS_FILE)
        reporters.append(self.to_dict())
        with open(REPORTERS_FILE, 'w') as f:
            json.dump(reporters, f)
        return self.to_dict()

    def get_reporter_by_id(self, id):
        reporters = _load_json_array(REPORTERS_FILE)
        for reporter in reporters:
            if reporter['id'] == int(id):
                return reporter
        return None

    def get_all_reporters(self):
        return _load_json_array(REPORTERS_FILE)

class Issue(BaseEntity):
    def __init__(self, id, title, description, status, priority, reporter_id, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at

    def validate(self):
        if not self.title:
            raise ValueError("Title is required")

    def describe(self):
        return f"{self.title} [{self.priority}]"

    def get_all_issues(self):
        with open(ISSUES_FILE, 'r') as f:
            return json.load(f) 

    def get_issue_by_id(self, id):
        with open(ISSUES_FILE, 'r') as f:
            issues = json.load(f)
            print(issues)
            for issue in issues:
                print(issue['id'])
                if issue['id'] == int(id):
                    return issue
            return None

    def get_issues_by_status(self, status):
        with open(ISSUES_FILE, 'r') as f:
            issues = json.load(f)
            return [issue for issue in issues if issue['status'] == status]

class Bug(Issue):
    def describe(self):
        return f"{self.title} [{self.priority}] - {self.description}"

class Feature(Issue):
    def describe(self):
        return f"{self.title} [{self.priority}] - {self.description}"

class Critical(Issue):
    def describe(self):
        return f"{self.title} [{self.priority}] - {self.description} — needs immediate attention"

class LowPriority(Issue):
    def describe(self):
        return f"{self.title} [{self.priority}] - {self.description} — low priority"

class MediumPriority(Issue):
    def describe(self):
        return f"{self.title} [{self.priority}] - {self.description} — medium priority"