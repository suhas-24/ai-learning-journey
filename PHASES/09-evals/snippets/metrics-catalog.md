# Metrics Catalog

Use this as a quick reference when choosing what to measure.

The goal is not to measure everything. The goal is to measure the few things that tell you whether the system is actually doing its job.

| Metric | Best for | Caution |
| --- | --- | --- |
| Faithfulness | retrieval-grounded answers | requires good context and judge design |
| Answer relevance | direct response quality | can hide unsupported claims |
| Context precision | noisy retrieval detection | low recall can still be hidden |
| Context recall | missing evidence detection | harder to estimate well |
| Task success rate | end-to-end workflow quality | may hide where the failure happened |
| Tool success rate | integration health | not enough by itself |
| Refusal correctness | safety behavior | judge bias can matter |
| Cost per run | operational efficiency | low cost is not the same as quality |

Return to [README](../README.md).
