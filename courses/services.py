from django.core.exceptions import ValidationError
from accounts.enums import UserRoles


def directormanager(creator):
    if creator.role != (UserRoles.director.value or UserRoles.manager.value):
        raise ValidationError(
            ('Siz direktor yoki manager emassiz'),
            params={'value': creator.role},
        )
    return creator