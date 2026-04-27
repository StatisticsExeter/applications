---
title: "Building a classifier to predicting house age"
author: "Anonymous"
---

## Your task

This material is provided as context to the problem. You should rewrite it as you see fit.

## The Problem

Data on [Energy Certificates](https://epc.opendatacommunities.org/) were downloaded in March 2025. In this task, you are required to determine whether it is possible to determine the age of a house based on several recorded energy metrics.

## The Data

A very simple preview of the group summary statistics:

| Metric | Post-30s (Mean) | Pre-30s (Mean) |
|:-------|----------------:|---------------:|
| Efficiency | 68.2 | 54.1 |
| Emissions | 3.1 | 5.8 |
| Energy Consumption | 210.5 | 340.2 |

*(Note: You can replace the placeholder above by running `cat artefacts/supervised_classification/grouped_stats.csv` and pasting the results, or use a Pandoc filter to include the file directly.)*

It is always useful to view a scatterplot of the data, marking the two known groups:

![Exploratory Data Analysis Scatterplot](artefacts/supervised/lab/scatterplot.jpg)

## Fitting LDA and QDA classifiers

The simplest classifiers we could apply are Linear and Quadratic Discriminant analysis.

### Results from fitting a Linear Discriminant Analysis



### Results from fitting a Quadratic Discriminant Analysis


You should comment on these results. You may wish to add an interpretation of the coefficients of these classifiers.

## ROC curve (and AUC) for simple classifiers

We can examine the AUC for these classifiers to compare their performance across various thresholds.

{{LDA_TABLE}}

![ROC Curve Comparison](artefacts/supervised/lab/lda_roc.jpg)


{{QDA_TABLE}}

![ROC Curve Comparison](artefacts/supervised/lab/qda_roc.jpg)

You should comment on the performance of the classifier.

## Additional credit

For additional credit you should consider extending the pipeline and trying out other classifiers.

## Record of AI use for MTHM503 supervised coursework

| **Date** | **AI tool used** | **Purpose** | **Prompt** | **Section of work used for** |
|:---|:---|:---|:---|:---|
|    |    |    |    |    |
