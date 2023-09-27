judge_prompt_template = """
Determine if the candidate answer is better than the reference answer.
If the model answer is better, end your response with a [[YES]].
Otherwise, end your response with a [[NO]].

Question:
{question}

Candidate Answer:
{candidate_answer}

Reference Answer:
{ref_answer}
"""
