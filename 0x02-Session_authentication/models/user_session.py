# models/user_session.py
"""Module defining the UserSession model for storing user session
information."""


from models.base import Base


class UserSession(Base):
    """ UserSession model class """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize UserSession instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', '')
        self.session_id = kwargs.get('session_id', '')
