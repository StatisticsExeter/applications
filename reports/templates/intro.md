---
title: "A demonstration pipeline"
author: "MTHM503 Student"
date: "April 2026"
---

## Introduction to Pipelines

This document demonstrates the difference between a monolithic analysis and a **decoupled pipeline**. By rendering a document that displays artefacts generated as part of a pipeline, we can work on individual components more efficiently.

## Visualising Artefacts

We used a Python script within our DVC pipeline to generate a scatterplot. Instead of generating the plot *inside* this document, we simply reference the existing file from our `cache` folder:

![Spurious Correlation: Kerosene vs Divorce Rate](artefacts/intro/scatterplot.png){width=80%}

## Analysis Results

We also computed specific metrics and saved the results in text files. Below, we read these results back into the document to present the findings.

### Correlation Analysis
Here is the estimated correlation between Kerosene Sales in India and the Divorce Rate in Maine:

{{CORRELATION}}

## Regression Model Summary

The following table shows the results of a linear model predicting the Divorce Rate in Maine based on Kerosene sales in India. Note the extremely high (and extremely spurious) R-squared value:
Python

<pre style="font-size: 10px; line-height: 1.1; overflow-x: auto;">
{{REGRESSION_SUMMARY}}
</pre>
