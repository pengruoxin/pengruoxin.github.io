---
layout: about
title: About
permalink: /
subtitle: M.Sc. Student · Artificial Intelligence and Big Data Computing

profile: false

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<div class="academic-intro">
  <p class="academic-kicker">Computer Vision · Model Reuse · Architecture Search</p>
  <p class="academic-lede">I am an M.Sc. student in Artificial Intelligence and Big Data Computing at The Hong Kong Polytechnic University. I study how reusable components from existing vision models can be composed into more accurate and resource-efficient architectures.</p>
  <p>Before PolyU, I studied Data Science and Big Data Technology at China Agricultural University, where I worked on computer-vision systems for agricultural applications.</p>
</div>

<section id="research-interests" class="academic-section">
  <header class="section-heading">
    <p class="section-label">Research</p>
    <h2>Research Interests</h2>
  </header>
  <div class="interest-grid">
    <article>
      <h3>Vision Model Reassembly</h3>
      <p>Reusing functional blocks from independently pretrained vision models and studying how multiple sources can contribute within one architecture.</p>
    </article>
    <article>
      <h3>Efficient Architecture Search</h3>
      <p>Designing low-cost evaluation signals and multi-objective search methods that balance predictive quality, parameter count, and computation.</p>
    </article>
    <article>
      <h3>Applied Computer Vision</h3>
      <p>Building and evaluating visual recognition systems for agricultural classification, quality assessment, and animal-behavior analysis.</p>
    </article>
  </div>
</section>

<section id="featured-research" class="academic-section featured-research">
  <div class="featured-copy">
    <p class="section-label">Vision Model Reassembly · Featured Research</p>
    <h2>HeteroWeave</h2>
    <p class="featured-summary">A framework for composing a new vision model from reusable blocks drawn from several pretrained models.</p>
    <p>Instead of forcing every position to keep exactly one source block, HeteroWeave allows a variable number of compatible blocks to work together. It uses a low-cost candidate score and Pareto-guided search to find different accuracy–efficiency trade-offs without fully training every possible composition.</p>
    <div class="metric-row" aria-label="HeteroWeave key results">
      <div><strong>79.457%</strong><span>ImageNet-1K Top-1</span></div>
      <div><strong>−26.7%</strong><span>parameters</span></div>
      <div><strong>−11.9%</strong><span>FLOPs</span></div>
    </div>
    <p><a class="academic-link" href="{{ '/research/heteroweave/' | relative_url }}">Read the research overview →</a></p>
  </div>
  <a class="featured-figure" href="{{ '/research/heteroweave/' | relative_url }}" aria-label="Open the HeteroWeave research overview">
    <img src="{{ '/assets/img/research/heteroweave-framework.png' | relative_url }}" alt="HeteroWeave combines reusable blocks from several pretrained vision models and searches for accuracy–efficiency trade-offs">
  </a>
</section>

<section id="publications" class="academic-section">
  <header class="section-heading section-heading-inline">
    <div>
      <p class="section-label">Research Outputs</p>
      <h2>Selected Publications</h2>
    </div>
    <a href="{{ '/publications/' | relative_url }}">View all →</a>
  </header>
  <div class="publications">
    {% bibliography --query @*[selected=true] %}
  </div>
</section>

<section id="education" class="academic-section">
  <header class="section-heading">
    <p class="section-label">Background</p>
    <h2>Education</h2>
  </header>
  <div class="academic-timeline">
    <article>
      <p class="timeline-date">2025–2027</p>
      <div>
        <h3>The Hong Kong Polytechnic University</h3>
        <p>M.Sc. in Artificial Intelligence and Big Data Computing</p>
      </div>
    </article>
    <article>
      <p class="timeline-date">2021–2025</p>
      <div>
        <h3>China Agricultural University</h3>
        <p>B.Eng. in Data Science and Big Data Technology · GPA 3.76/4.00 · Rank 5/29</p>
      </div>
    </article>
  </div>
</section>
