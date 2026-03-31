# Books

This section is the reading spine for the journey. The point is not to "finish" every book. The point is to use each book to build a concept map: what the book teaches, which ideas matter most, and which phase of the roadmap turns the ideas into working systems.

## How To Read

- read with the current phase open beside the book
- extract a small concept map after each chapter or part
- write one concrete note about how the idea would change a project
- stop reading when the book stops adding new leverage for the current phase

## Priority Reading Order

| # | Book | Best phase | Main teaching value |
| --- | --- | --- | --- |
| 1 | AI Engineering - Chip Huyen | 2 and 7 | Systems view of LLM applications, evaluation, deployment, and reliability |
| 2 | Hands-On Large Language Models - Alammar & Grootendorst | 2 and 3 | Friendly bridge from theory to practical LLM workflows |
| 3 | The LLM Engineering Handbook - Iusztin & Labonne | 5 to 7 | Retrieval, orchestration, and production design patterns |
| 4 | Building LLMs for Production - Bouchard & Peters | 7 to 9 | Operational thinking for shipping and measuring model systems |
| 5 | Build a Large Language Model (from Scratch) - Raschka | 10 | Model internals and fine-tuning intuition |
| 6 | The Hundred-Page Machine Learning Book - Burkov | 1 | Fast orientation in ML foundations |
| 7 | Designing Machine Learning Systems - Chip Huyen | 9 | Measurement, monitoring, and production tradeoffs |

## 1. AI Engineering - Chip Huyen

This is the most important book on the list because it explains AI as an engineering discipline instead of a prompt-writing hobby.

### What it covers

- the difference between model capabilities and product reliability
- how to think about data, evaluation, deployment, and iteration
- why good systems need feedback loops instead of one-time prompts
- the structure of AI products in real teams

### Core topics and subtopics

- model behavior
- prompt and context design
- data pipelines
- retrieval and grounding
- evaluation and test sets
- deployment and monitoring
- tradeoffs between accuracy, latency, and cost

### How to use it in this roadmap

- Phase 2: understand what model usage looks like in production
- Phase 7: revisit the chapters on systems, reliability, and iteration
- Phase 9: use it as the broader systems companion to evaluation work

## 2. Hands-On Large Language Models

This book is useful when I need a gentler but still technical bridge from theory to practice.

### What it covers

- what embeddings are and how they represent meaning
- how LLMs are trained and used at a practical level
- prompt patterns and generation behavior
- retrieval, vector search, and basic application workflows

### Core topics and subtopics

- tokenization
- embeddings
- prompting patterns
- semantic search
- retrieval-augmented generation
- model behavior and failure modes

### How to use it in this roadmap

- Phase 2: to understand the moving parts of an LLM system
- Phase 3: to translate concept knowledge into spec language
- Phase 5: as a support text when retrieval concepts start to overlap

## 3. The LLM Engineering Handbook

This book belongs to the middle of the roadmap because it leans into practical system building.

### What it covers

- application architecture for LLM systems
- retrieval pipelines and knowledge grounding
- agentic workflows
- framework choices and system design
- production considerations such as latency and maintainability

### Core topics and subtopics

- prompt orchestration
- RAG design
- chunking and embeddings
- agent loops
- tool use and external services
- deployment and observability

### How to use it in this roadmap

- Phase 5: retrieval and memory design
- Phase 7: orchestration, state, and system control
- Phase 9: evaluation and production quality

## 4. Building LLMs for Production

This is the book to reach for when the project starts looking real and the "it works locally" phase is no longer enough.

### What it covers

- how to think about model systems in operational environments
- the relationship between reliability, cost, and user trust
- monitoring, tracing, and evaluation in deployed systems
- practical workflow design for production teams

### Core topics and subtopics

- production architecture
- logging and observability
- performance and latency
- cost controls
- release discipline
- failure recovery

### How to use it in this roadmap

- Phase 7: harness engineering
- Phase 8: production safety and governance
- Phase 9: monitoring and measurement

## 5. Build a Large Language Model (from Scratch)

This book matters because it helps demystify how a model actually works under the hood.

### What it covers

- the mechanics of building a transformer-style model
- the meaning of weights, training, and optimization
- how training data shapes behavior
- why model adaptation is different from prompting

### Core topics and subtopics

- neural network fundamentals
- token representations
- attention
- training loops
- loss and optimization
- inference behavior

### How to use it in this roadmap

- Phase 10: model adaptation and fine-tuning intuition
- also useful earlier if I want stronger mental models for embeddings and generation

## 6. The Hundred-Page Machine Learning Book

This is the fast orientation book. It is not the deepest one, but it is useful for vocabulary and intuition.

### What it covers

- the core language of machine learning
- the difference between common ML approaches
- overfitting, generalization, and evaluation basics
- enough structure to make later AI engineering reading easier

### Core topics and subtopics

- supervised learning
- unsupervised learning
- model fitting
- error and bias
- evaluation basics

### How to use it in this roadmap

- Phase 1 as background reading
- Phase 2 to reduce intimidation around ML vocabulary

## 7. Designing Machine Learning Systems

This is the book to revisit when the system needs better measurement and more operational thinking.

### What it covers

- how ML systems fail in production
- data drift and quality problems
- evaluation systems
- deployment tradeoffs
- monitoring and iteration

### Core topics and subtopics

- problem framing
- data collection
- model training and validation
- deployment
- monitoring
- iteration loops

### How to use it in this roadmap

- Phase 9: observability and evals
- Phase 11: project framing and portfolio narrative

## Personal Notes

- If a book does not help me make a better decision in code or architecture, I should slow down and question why I am reading it now.
- The strongest books here are the ones that connect concept, system, and production reality.
- Books become valuable when I turn their ideas into phase notes, experiments, and project changes.
