# Agentic AI Contributor for Open-Source Go Projects

## Overview

This project implements an Agentic AI system that assists in solving GitHub issues from open-source Go repositories.

The system automatically:

* Understands GitHub issues
* Analyzes repository structure and source code
* Identifies relevant files and context
* Builds repository-aware context using Retrieval-Augmented Generation (RAG)
* Creates a fix plan
* Generates code modifications
* Performs validation checks
* Produces a Pull Request (PR) title and description

The objective of this project is to demonstrate repository understanding, code reasoning, automated code generation, and validation using Large Language Models (LLMs).

---

## Architecture

```text
GitHub Issue
     |
     v
Issue Analyzer Agent
     |
     v
Repository Search Agent
     |
     v
Context Builder (RAG)
     |
     v
Fix Planner Agent
     |
     v
Code Generator Agent
     |
     v
Validation Agent
     |
     v
PR Generator Agent
```

---

## Supported Repositories

The system supports the following Go repositories:

* gin-gonic/gin
* spf13/cobra
* go-playground/validator
* golangci/golangci-lint

Users can provide a GitHub issue URL from any supported repository, and the agent will analyze the issue, retrieve repository context, generate a fix plan, propose code changes, and create a pull request summary.

---

## Project Structure

```text
agentic-go-contributor/

├── agents/
│   ├── __init__.py
│   ├── issue_analyzer.py
│   ├── repo_search.py
│   ├── context_builder.py
│   ├── planner.py
│   ├── code_generator.py
│   ├── validator.py
│   └── pr_generator.py
│
├── repositories/
│
├── outputs/
│   ├── patch.diff
│   └── pr.md
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Features

### Issue Understanding

Extracts and analyzes GitHub issue information.

### Repository Analysis

Clones and scans the target Go repository.

### Context Retrieval (RAG)

Uses FAISS and Sentence Transformers to retrieve the most relevant source files and code sections related to a GitHub issue.

### Fix Planning

Generates a structured plan to address the issue.

### Code Generation

Produces suggested code modifications and code patches.

### Validation

Runs validation checks and test commands when available.

### Pull Request Generation

Creates a PR title and description summarizing the proposed changes.

---

## Technologies Used

* Python
* OpenAI API
* GitPython
* FAISS
* Sentence Transformers
* BeautifulSoup
* Requests

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pratikdasiitkgp-code/agentic-go-contributor.git
cd agentic-go-contributor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Example:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Usage

Run the application:

```bash
python main.py
```

Provide a GitHub issue URL when prompted:

```text
https://github.com/gin-gonic/gin/issues/1234
```

The system will:

1. Analyze the GitHub issue
2. Clone or access the repository
3. Retrieve relevant repository context
4. Generate a fix plan
5. Produce code suggestions
6. Run validation checks
7. Generate a Pull Request summary

---

## Sample Output

### Generated Plan

```text
1. Identify affected files.
2. Analyze root cause.
3. Modify implementation.
4. Add or update tests.
5. Validate changes.
```

### Generated Pull Request

```text
Title:
Fix request validation behavior

Description:
- Updated validation logic
- Improved error handling
- Added additional test coverage
- Validation completed successfully
```

---

## Output Files

### patch.diff

Contains the generated code patch or proposed code modifications.

### pr.md

Contains the generated Pull Request title and description.

---

## Future Improvements

* Multi-agent collaboration
* Automatic GitHub Pull Request creation
* Improved repository indexing
* Advanced code patch generation
* Support for additional programming languages
* Automated issue prioritization

---

## Limitations

* Generated patches should be reviewed by developers before applying them.
* Validation depends on the availability of required tools such as the Go compiler.
* Repository understanding is limited by the quality of retrieved context and issue descriptions.

---

## Author

Pratik Das

M.Tech, IIT Kharagpur

Areas of Interest:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Computer Vision
* Large Language Models (LLMs)

---

## License

This project is intended for educational and internship evaluation purposes.
