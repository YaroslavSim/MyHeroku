"""Academy extras."""
from django import template

register = template.Library()


@register.filter()
def get_col_students(value, step):
    """Get col students function."""
    if len(value) == 0:
        return f'No student in group'
    elif len(value) == 1:
        return f'{len(value)} student'
    else:
        return f'{len(value)} students'
