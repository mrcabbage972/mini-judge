# mini-judge
Simple implementation of LLM-As-Judge for pairwise evaluation of Q&A models.

# Usage
Install the package using pip:
```pip install mini-judge```

Then, you can use the package as follows.
First, set the OPENAI_API_KEY environment variable to your OpenAI API key.
Then, you can run the following command to evaluate the candidate answers in `candidate_answers_path` against the reference answers in `ref_answers_path` using `judge_model` as the judge model.
```
mini-judge \
--judge_model <judge_model> \
--questions_path <questions_path> \
--candidate_answers_path <candidate_answers_path> \
--ref_answers_path <ref_answers_path> \
--output_path <output_path>
```

To run a quick demo, use the following command to evaluate the candidate answers in `example_data/candidate_answers.jsonl` against the reference answers in `example_data/ref_answers.jsonl` using GPT-4 as the judge model.
```
mini_judge --output_path <output_path>
```
