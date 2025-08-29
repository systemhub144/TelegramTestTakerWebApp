from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base, CloseAnswerEnum, AnswerTypeEnum


class Test(Base):
    test_name: Mapped[str] = mapped_column(String)
    open_questions: Mapped[int] = mapped_column(default=0)
    close_questions: Mapped[int] = mapped_column(default=0)
    test_time: Mapped[int] = mapped_column(default=60)
    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    is_ended: Mapped[bool] = mapped_column(default=False)

    test_attempt: Mapped[list['TestAttempt']] = relationship(
        'TestAttempt',
        back_populates='test',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    answer: Mapped[list['Answer']] = relationship(
        'Answer',
        back_populates='test',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    user: Mapped[list['User']] = relationship(
        'User',
        back_populates='test',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Test {self.test_name}>'


class User(Base):
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)

    test_attempt: Mapped[list["TestAttempt"]] = relationship(
        'TestAttempt',
        back_populates='user',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    def __repr__(self):
        return f'<User {self.user_id}>'


class TestAttempt(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    test_id: Mapped[int] = mapped_column(ForeignKey('tests.id'))
    score: Mapped[int] = mapped_column(default=0)
    wrong_answers: Mapped[int] = mapped_column(default=0)
    correct_answers: Mapped[int] = mapped_column(default=0)
    started_at: Mapped[datetime]
    completed_at: Mapped[datetime]

    user: Mapped[User] = relationship(
        'User',
        back_populates='test_attempt',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    test: Mapped[Test] = relationship(
        'Test',
        back_populates='test_attempt',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    user_answer: Mapped[list["UserAnswer"]] = relationship(
        'UserAnswer',
        back_populates='test_attempt',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )


    def __repr__(self):
        return f'<TestAttempt user_id={self.user_id} test_id={self.test_id}>'


class Answer(Base):
    question_number: Mapped[int] = mapped_column(nullable=False)
    question_type: Mapped[AnswerTypeEnum] = mapped_column(nullable=False)
    correct_answer: Mapped[CloseAnswerEnum | str] = mapped_column(String(150), nullable=False)
    test_id: Mapped[int] = mapped_column(ForeignKey('tests.id'))

    test: Mapped[Test] = relationship(
        'Test',
        back_populates='answer',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    user_answer: Mapped[list['Test']] = relationship(
        'UserAnswer',
        back_populates='answer',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )


    def __repr__(self):
        return f'<Answer question_number={self.question_number} test={self.test_id}>'


class UserAnswer(Base):
    attempt_id: Mapped[int] = mapped_column(ForeignKey('testattempts.id'))
    answer_id: Mapped[int] = mapped_column(ForeignKey('answers.id'))
    user_answer: Mapped[str] = mapped_column(String(150), nullable=False)
    is_correct: Mapped[bool] = mapped_column(nullable=False)
    test_id: Mapped[int] = mapped_column(ForeignKey('tests.id'))

    test_attempt: Mapped[TestAttempt] = relationship(
        'TestAttempt',
        back_populates='user_answer',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    answer: Mapped[Answer] = relationship(
        'Answer',
        back_populates='user_answer',
        cascade='all, delete-orphan'  # Удаляет посты при удалении пользователя
    )

    test: Mapped[Test] = relationship(
        'Test',
        back_populates='user_answer',
        cascade='all, delete-orphan'
    )


    def __repr__(self):
        return f'<UserAnswer attempt_id={self.attempt_id} question={self.answer_id}>'