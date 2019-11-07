import pytest
import os
from jam.wsgi import create_application

@pytest.fixture(scope="session", autouse=True)
def app(request):
    project_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'project')
    return create_application(project_folder, load_task=True, testing=True)

@pytest.fixture(scope="session", autouse=True)
def admin(app):
    return app.admin

@pytest.fixture(scope="session", autouse=True)
def task(app):
    return app.task

@pytest.fixture(scope="module")
def fields_item(task):
    item = task.item.copy()
    item.empty()
    item.open(open_empty=True)
    item.append()
    item.post()
    item.apply()
    return item


