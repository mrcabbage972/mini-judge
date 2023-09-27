import json
from typing import List


def load_answers_file(path: str) -> List[str]:
    with open(path) as f:
        answers = [json.loads(line)['answer'] for line in f.readlines()]
    return answers


def load_questions_file(path: str) -> List[str]:
    with open(path) as f:
        questions = [json.loads(line)['question'] for line in f.readlines()]
    return questions
