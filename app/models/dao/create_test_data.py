import datetime

from app.models.dao.add_methods_dao import pass_test, add_full_test
from app.models.database import AnswerTypeEnum, CloseAnswerEnum

from asyncio import run


user_test_data = {
    'test_id': 27,
    'username': 'sardor',
    'user_id': 1,
    'city': 'Tashkent',
    'started_at': datetime.datetime.now(),
    'completed_at': datetime.datetime.now(),
    'answers':['A', 'B', 'C', 'D', 'E', 'F', 'E', 'A', 'B', 'C', 'HELLO', 'Bee', 'Car', 'Door', 'Earth'],
}

run(pass_test(user_test_data=user_test_data))


test_data = {
    'test_id': 27,
    'test_name': 'test1',
    'open_questions': 10,
    'close_questions': 5,
    'test_time': 120,
    'start_time': datetime.datetime.now(),
    'end_time': datetime.datetime.now(),
    'is_ended': False,
    'answers': [
        {
            'question_number': 1,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.A,
        },
        {
            'question_number': 2,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.B,
        },
        {
            'question_number': 3,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.C,
        },
        {
            'question_number': 4,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.D,
        },
        {
            'question_number': 5,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.E,
        },
        {
            'question_number': 6,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.F,
        },
        {
            'question_number': 7,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.A,
        },
        {
            'question_number': 8,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.B,
        },
        {
            'question_number': 9,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.C,
        },
        {
            'question_number': 10,
            'question_type': AnswerTypeEnum.OPEN,
            'correct_answer': CloseAnswerEnum.D,
        },
        {
            'question_number': 11,
            'question_type': AnswerTypeEnum.CLOSE,
            'correct_answer': 'All',
        },
        {
            'question_number': 12,
            'question_type': AnswerTypeEnum.CLOSE,
            'correct_answer': 'Bee',
        },
        {
            'question_number': 13,
            'question_type': AnswerTypeEnum.CLOSE,
            'correct_answer': 'Car',
        },
        {
            'question_number': 14,
            'question_type': AnswerTypeEnum.CLOSE,
            'correct_answer': 'Door',
        },
        {
            'question_number': 15,
            'question_type': AnswerTypeEnum.CLOSE,
            'correct_answer': 'Elephant',
        },
    ]
}

run(add_full_test(test_data))
