<h1 align="center">
<span>Mini Judge</span>
</h1>

[![PyPI version](https://badge.fury.io/py/mini-judge.svg)](https://badge.fury.io/py/mini-judge)
<a href="https://github.com/mrcabbage972/mini-judge/actions/workflows/pre-commit.yml">![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mrcabbage972/mini-judge/pre-commit.yml?label=pre-commit)</a>


Simple implementation of LLM-As-Judge for pairwise evaluation of Q&A models.

# Installation
Install the package using pip:
```pip install mini-judge```

# Usage
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
# Data Format
All input data files are presumed to be in [jsonl](https://jsonlines.org/) format.

The `candidate_answers` and `ref_answers` files should have each line as a json with an `answer` tag.

Similarly, the questions file should have json lines with a `question` tag.

All other tags will be ignored.

# References
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, & Ion Stoica. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena [ArXiv](https://arxiv.org/abs/2306.05685).
