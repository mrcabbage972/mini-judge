# mini-judge
Simple implementation of LLM-As-Judge for pairwise evaluation of Q&A models.

# Usage
Install the package using pip:
```pip install mini-judge```

Then, you can use the package as follows:
```
mini-judge \
--judge_model <judge_model> \
--questions_path <questions_path> \
--candidate_answers_path <answers_path> \
--ref_answers_path <answers_path> \
--output_path <output_path>
```
