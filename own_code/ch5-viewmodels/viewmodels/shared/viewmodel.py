from typing import Optional

from starlette.requests import Request


class ViewModelBase:
    
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None

        self.is_logged_in = False

    def to_dict(self) -> dict:
        return self.__dict__