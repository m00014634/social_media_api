from pydantic import BaseModel,validator
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: str
    about: Optional[str]

    # Проверка почты
    @validator('email')
    def check_email(cls,mail):
        if '@' in mail:
            return mail
        raise TypeError('Почта указана неверно')


    # Проверка номера
    @validator('phone_number')
    def check_phone_number(cls, number):
        pass




