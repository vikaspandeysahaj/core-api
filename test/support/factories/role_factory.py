
from api.models.role import Role


def create_role(title=None):
    if title is None:
        title="Normal_user"
    return Role.create_role(title)

