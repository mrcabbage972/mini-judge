from mini_judge.judge_prompt import judge_prompt_template


def test_judge_prompty_format():
    question = "aaa"
    candidate_answer = "bbb"
    ref_answer = "ccc"
    prompt = judge_prompt_template.format(question=question, candidate_answer=candidate_answer,
                                          ref_answer=ref_answer)
    assert question in prompt
    assert candidate_answer in prompt
    assert ref_answer in prompt
