from datetime import date

from pydantic import BaseModel, Field
from enum import Enum
from decimal import Decimal


class Problem(BaseModel):
    issue: list[str] = Field(description="Описание проблемы, второй слайд - Проблема")
    target_audience: str = Field(
        description="Целевая аудитория, второй слайд - Проблема"
    )
    solution: list[str] = Field(description="Решение проблемы, четвертый слайд - Решение")


class Member(BaseModel):
    full_name: str = Field(description="ФИО, 10 слайд - Команда")
    proffesion: str = Field(description="Род деятельности, 10 слайд - Команда")
    photo: None  # TODO: изображение (вообще забить)


class Investor(BaseModel):
    name: str = Field(description="Имя компании, 11 слайд - Инвесторы")
    image: None  # TODO: изображение (вообще забить) maybe парсинг


class Stage(str, Enum):
    pre_seed = "pre-seed"
    seed = "seed"
    round_A = "раунд А"
    round_B = "раунд Б"
    round_C = "раунд С"
    ipo = "IPO"


class Spending(BaseModel):
    name: str = Field(description="Имя траты, 12 слайд - Инвестиционный раунд")
    percent: str = Field(description="Процент траты, 12 слайд - Инвестиционный раунд")


class InvestingRound(BaseModel):
    amount: Decimal = Field(
        description="Сколько всего будет привлечено денег в рамках раунда, 12 слайд - Инвестиционный раунд"
    )
    stage: Stage = Field(description="Имя раунда, 12 слайд - Инвестиционный раунд")
    spending: list[Spending] = Field(
        description="На что тратят в процентах, 12 слайд - Инвестиционный раунд"
    )


class RoadmapStep(BaseModel):
    name: str = Field(description="Имя шага, 13 слайд - Дорожная карта")
    start_date: date = Field(description="Дата начала, 13 слайд - Дорожная карта")
    end_date: date = Field(description="Дата конца, 13 слайд - Дорожная карта")


class TypeContact(str, Enum):
    phone = "phone"
    email = "email"
    site = "site"
    vk = "vk"
    telegram = "telegram"
    whatsapp = "whatsapp"
    viber = "viber"
    other = "other"
    # facebook = "facebook"
    # instagram = "instagram"


class Contact(BaseModel):
    type: TypeContact = Field(description="Тип, 14 слайд - Контакты")
    value: str = Field(description="Значение, 14 слайд - Контакты")


class CreatePresentation(BaseModel):
    project_name: str = Field(description="Название проекта/компании, первый слайд - Проект")
    short_description: str = Field(
        description="Краткое описание проекта/ключевая ценность, первый слайд - Проект"
    ) # TODO: на основе ии тащить
    problem: list[Problem] = Field(
        description="Проблемы, второй-четвертый слайд - Проблема и Решение"
    )
    description: str = Field(description="Описание, третий слайд - Описание")
    # TODO: TAM SAM SOM слайд 5 - Рынок
    # TODO Конкуренты 6 слайд, парсинг, на основе предыдущих 4 слайдов данные
    # TODO Бизнес-модель и ценообразование слайд 7
    clients: list[str] = Field(description="Клиенты, maybe 8 слайд")  # TODO изображения
    revenue: str | None = Field(description="Выручка, 9 слайд - Финансы") # Если компании нет
    clients_count: str = Field(description="Число клиентов, 9 слайд - Финансы")
    churn_rate: str = Field(description="Коэффициент оттока, 9 слайд - Финансы")
    inn: str | None = Field(
        description="Инн компании, если существует, для парсинга в checko"
    )
    is_exist: bool = Field(default=False, description="Существует ли компания, для инн")
    # TODO: https://checko.ru/company/anspot-1217700374495 парсинг Конкуренты + финансы (выручка + капитализация по годам) + Контакты
    members: list[Member] = Field(description="Члены команды, 10 слайд - Команда")
    investors: list[Investor] | None = Field(
        description="Инвесторы, 11 слайд - Инвесторы"
    )
    investing_rounds: list[InvestingRound] = Field(
        description="Инвестиционные раунды, 12 слайд - Инвестиционный раунд"
    )
    roadmap: list[RoadmapStep] = Field(
        description="Дорожная карта, 13 слайд - Дорожная карта"
    )
    contacts: list[Contact] = Field(description="Контакты, 14 слайд - Контакты")
    sphere: str = Field(description="Сфера деятельности компаний, для картинок/расчётов")
