---
layout: page
title: Research
permalink: /research/
description: Research projects in model reassembly, architecture search, and computer vision.
nav: true
nav_order: 2
display_categories: [research]
---

<section class="research-index" aria-labelledby="heteroweave-title">
  <a class="research-index-figure" href="{{ '/research/heteroweave/' | relative_url }}" aria-label="Open the HeteroWeave research overview">
    <img src="{{ '/assets/img/research/heteroweave-framework.png' | relative_url }}" alt="HeteroWeave combines blocks from heterogeneous pretrained models using variable-cardinality composition and multi-objective search">
  </a>
  <div class="research-index-copy">
    <p class="section-label">Vision Model Reassembly · Main Project</p>
    <h2 id="heteroweave-title">HeteroWeave</h2>
    <p class="research-index-lede">Variable-cardinality reassembly of heterogeneous pretrained vision models.</p>
    <p>HeteroWeave treats pretrained vision-model blocks as reusable components, allows several compatible blocks to collaborate at one functional position, and searches for architectures that balance predictive quality, parameter count, and computation.</p>
    <ul class="research-index-facts" aria-label="HeteroWeave highlights">
      <li><strong>CLAS</strong><span>low-cost candidate ranking</span></li>
      <li><strong>79.457%</strong><span>ImageNet-1K Top-1</span></li>
      <li><strong>Submitted</strong><span>to a CCF-A venue</span></li>
    </ul>
    <a class="academic-link" href="{{ '/research/heteroweave/' | relative_url }}">Read the full research overview →</a>
  </div>
</section>
