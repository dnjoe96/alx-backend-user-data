#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from typing import Callable
from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method to add a new user """
        user = User(id=1, email=email, hashed_password=hashed_password)
        self._session.add(user)
        return user

    # @staticmethod
    def find_user_by(self, **vals: dict) -> User:
        """ find a user by an arbitrary attribute """
        try:
            user = self._session.query(User).filter_by(**vals).first()
        except TypeError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user
