import os
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

import fire
import openai
from dotenv import load_dotenv
from loguru import logger
from mini_judge.data_io import load_answers_file
from mini_judge.data_io import load_questions_file
from mini_judge.judge_execution import trial
from mini_judge.trial_result_manager import TrialResultManager
from pkg_resources import resource_filename
from tqdm import tqdm


def main(judge_model: str = 'gpt-4',
         questions_path: str = resource_filename('mini_judge', 'example_data/questions.jsonl'),
         candidate_answers_path: str = resource_filename('mini_judge', 'example_data/candidate_answers.jsonl'),
         ref_answers_path: str = resource_filename('mini_judge', 'example_data/ref_answers.jsonl'),
         output_dir: str = 'output',
         query_parallelism: int = 2):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if openai.api_key is None:
        logger.error('OPENAI_API_KEY is not set')
        exit(1)

    logger.info('Loading data')
    questions = load_questions_file(questions_path)
    candidate_answers = load_answers_file(candidate_answers_path)
    ref_answers = load_answers_file(ref_answers_path)

    assert len(questions) == len(candidate_answers) == len(ref_answers)

    trial_result_mgr = TrialResultManager()
    if query_parallelism > 1:
        with ThreadPoolExecutor(query_parallelism) as executor:
            map_op = executor.map(trial, repeat(judge_model), questions, candidate_answers,
                                  ref_answers)
            for trial_outcome in tqdm(map_op, total=len(candidate_answers), desc='Evaluating'):
                trial_result_mgr.update(trial_outcome)
    else:
        for q, m_a, r_a in tqdm(zip(questions, candidate_answers, ref_answers), desc='Evaluating'):
            trial_outcome = trial(judge_model, q, m_a, r_a)
            trial_result_mgr.update(trial_outcome)

    logger.info(trial_result_mgr)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    trial_result_mgr.serialize_judge_answers(os.path.join(output_dir, 'judge_answers.jsonl'))
    trial_result_mgr.serialize_stats(os.path.join(output_dir, 'trial_stats.jsonl'))


if __name__ == '__main__':
    fire.Fire(main)
