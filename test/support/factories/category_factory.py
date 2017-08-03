
from api.models.category import Category


def create_category(title=None):
    if title is None:
        title="Normal_user"
    return Category.create_category(title)

