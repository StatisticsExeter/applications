---
title: "Olive Oil Composition Analysis"
author: "Student Name"
date: "2026-04-10"
---

# Introduction
This report examines the chemical composition of olive oils. Below are the exploratory data analysis artifacts.

## Data Summary
The following table provides the descriptive statistics for the numeric variables in the dataset (mean, standard deviation, and range).

```text
{{summary_table}}
```


Exploratory Data Analysis
Distribution of Raw Variables


![Figure 1: Distribution of fatty acids in raw format.](artefacts/stage_demo/lab_olive_oil_raw_boxplot.jpg){width=80%}


The boxplot below shows the distribution of the chemical components. Note the differences in scale between variables like Palmitic and Eicosenoic acids.
Scaled Distributions

![Figure 2: Pairwise relationships between variables.](artefacts/stage_demo/lab_olive_oil_scaled_boxplot.jpg){width=100%}


To compare distributions on a uniform scale, we applied a Standard Scaler (mean=0, variance=1).
Variable Relationships


![Figure 2: Pairwise relationships between variables.](artefacts/stage_demo/lab_olive_oil_scatterplot.jpg){width=100%}


The scatter matrix below illustrates the correlations and pairwise relationships between the various fatty acids.


When applying kmeans we get the following: 

![Figure 2a: Results](artefacts/stage_demo/dendrogram.jpg){width=100%}

![Figure 3: Results.](artefacts/stage_demo/kmeans_1.jpg){width=100%}

![Figure 4: Results.](artefacts/stage_demo/kmeans_2.jpg){width=100%}

![Figure 5: Results.](artefacts/stage_demo/kmeans_scatter.jpg){width=100%}
