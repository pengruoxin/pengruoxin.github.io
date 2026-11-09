---
layout: page
title: HeteroWeave
description: Variable-cardinality reassembly of heterogeneous pretrained vision models.
permalink: /research/heteroweave/
img: assets/img/research/heteroweave-framework.png
importance: 1
category: research
related_publications: false
---

<p class="research-status">Vision Model Reassembly · Submitted to a CCF-A venue</p>

## Building new vision models from reusable pretrained blocks

Modern vision systems leave behind many pretrained models with complementary capabilities. HeteroWeave asks whether their internal blocks can be treated as reusable components: instead of selecting one complete model, can we compose a new architecture from useful computation distributed across several sources?

Existing reassembly approaches typically retain one block at each aligned position. HeteroWeave expands that design space by allowing a variable number of heterogeneous blocks to participate together, so the search decides both **which blocks to use** and **how many should collaborate**.

<figure class="research-figure research-figure-wide">
  <img src="{{ '/assets/img/research/heteroweave-framework.png' | relative_url }}" alt="HeteroWeave pipeline from heterogeneous pretrained blocks to variable-cardinality composition and multi-objective architecture search">
  <figcaption>HeteroWeave turns several pretrained models into a shared block library, makes different compositions executable, and searches for architectures with different performance–resource trade-offs.</figcaption>
</figure>

## What the framework changes

### Variable-cardinality composition

At each functional position, the architecture may use one block or let several compatible blocks run in parallel. Shared interfaces align their inputs, while lightweight adaptation and fusion make blocks from different model families work inside the same candidate architecture.

### Low-cost candidate ranking with CLAS

The number of possible compositions grows too quickly to train every candidate. **CLAS** estimates candidate quality from block-level activation-pattern statistics after a forward pass. Its square-root aggregation reduces the tendency of activation-based scores to reward a candidate merely because more blocks expanded its activation space.

Across two independent validation pools, CLAS reaches Spearman rank correlations of **0.775** and **0.570** with short-training results. This makes it useful as a search signal rather than as a substitute for final training and evaluation.

### Multi-objective search

HeteroWeave jointly optimizes the CLAS score, parameter count, and FLOPs. Pareto-guided evolutionary search retains nondominated candidates instead of collapsing performance and resource use into one fixed weighting, leaving multiple architectures for different deployment budgets.

<figure class="research-figure">
  <img src="{{ '/assets/img/research/heteroweave-search.png' | relative_url }}" alt="Pareto search results comparing estimated model quality, parameter count, and computation">
  <figcaption>The search keeps candidates that offer distinct trade-offs among estimated quality, model size, and computation.</figcaption>
</figure>

## Experimental evidence

On ImageNet-1K, a selected HeteroWeave architecture reaches **79.457% Top-1 accuracy**. Compared with the serial single-block reassembly baseline, it improves accuracy by **1.079 percentage points** while using **26.7% fewer parameters** and **11.9% fewer FLOPs**.

A resource-matched comparison holds both alternatives at 29.18M parameters and approximately 4.70G FLOPs. The parallel composition remains 1.87 percentage points more accurate, separating the effect of the composition structure from simply adding capacity.

<figure class="research-figure">
  <img src="{{ '/assets/img/research/heteroweave-results.png' | relative_url }}" alt="Repeated ImageNet-1K results comparing HeteroWeave with serial single-block reassembly">
  <figcaption>Three-seed ImageNet-1K results for the selected architecture and the serial single-block reassembly baseline.</figcaption>
</figure>

## Scope

The study evaluates the framework across image classification, vision-language retrieval, semantic segmentation, and object detection. The results show that the best participation cardinality varies by task and position, supporting search over cardinality rather than always maximizing the number of participating blocks.
