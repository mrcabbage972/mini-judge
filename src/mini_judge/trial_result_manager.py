import json

from mini_judge.judge_execution import TrialOutcome


class TrialResultManager:
    """
    Responsible for managing the results of a trial.
    Keeps track of the number of wins for the candidate and reference answers.
    Has serialization methods for the judge answers and trial stats.
    """
    def __init__(self):
        self.candidate_wins = 0
        self.ref_wins = 0
        self.total = 0

        self.judge_answers = []

    def update(self, trial_outcome: TrialOutcome):
        verdict = trial_outcome.trial_verdict
        if verdict == 1:
            self.candidate_wins += 1
        elif verdict == -1:
            self.ref_wins += 1
        self.total += 1
        self.judge_answers.append(trial_outcome.judge_answer)

    def calc_stats(self):
        return {'candidate_win_rate': self.candidate_wins / (self.candidate_wins + self.ref_wins),
                'candidate_wins': self.candidate_wins,
                'ref_wins': self.ref_wins,
                'undecided': self.total - self.candidate_wins - self.ref_wins,
                'total': self.candidate_wins + self.ref_wins}

    def __repr__(self):
        stats = self.calc_stats()

        return f'Candidate Win Rate: {stats["candidate_win_rate"]}\n' \
               f'Candidate Wins: {stats["candidate_wins"]}\n' \
               f'Ref Wins: {stats["ref_wins"]}\n' \
               f'Undecided: {stats["undecided"]}\n' \
               f'Total: {stats["total"]}\n'

    def serialize_judge_answers(self, output_path: str):
        with open(output_path, 'w') as f:
            for answer in self.judge_answers:
                f.write(json.dumps({'judge_answer': f'{answer}'}) + '\n')

    def serialize_stats(self, output_path: str):
        with open(output_path, 'w') as f:
            f.write(json.dumps(self.calc_stats()) + '\n')
