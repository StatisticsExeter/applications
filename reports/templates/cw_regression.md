---
title: "Understanding Housing Carbon Emissions within a Local Authority"
author: "Anonymous"
---

## The problem

Energy Performance Certificate (EPC) data were obtained from the UK government’s open EPC dataset in March 2025
(<https://epc.opendatacommunities.org/>).
In this analysis, we focus on a single local authority and examine variation in current residential carbon emissions at the level of individual dwellings.
Rather than comparing local authorities, the aim here is to understand how carbon emissions vary within an authority, and to assess whether part of this variation can be attributed to differences in built form (e.g. detached houses, flats, terraced housing), after accounting for dwelling size.
Only the most recent EPC per dwelling is retained, ensuring that each observation corresponds to a unique property.

## The data

The dataset consists of individual EPC records for dwellings within the selected local authority. For each dwelling, the following variables are used:

- `co2_emissions_current` (response variable)
- `total_floor_area`
- `built_form`

The data are not aggregated: each row represents a single dwelling.

## Modelling approach

A linear mixed effects regression model is fitted to account for the hierarchical structure of the data.
Dwellings are grouped by built form, which is treated as a random effect. This reflects the idea that different built forms may have systematically higher or lower carbon emissions, but that these categories are not of primary interest as fixed coefficients.

The model can be written as:

$Y_{ij}=\beta_0+\beta_1 floor\_area_{ij} + u_j +\epsilon_{ij}$


where:

- $Y_{ij}$ is the current CO₂ emissions of dwelling $i$ in built form $j$
- $\beta_0$​ and $\beta_1$​ are fixed effects
- $u_j$​ is a random intercept for built form
- $\epsilon_{ij}$​ is the error

This structure allows for partial pooling across built forms and avoids estimating a separate fixed coefficient for each category.

## Model summary
Below are the estimated fixed effects and variance components from the fitted mixed‑effects model:


```text
{{MODEL_SUMMARY}}
```

You should comment on:

- the relationship between floor area and carbon emissions
- the estimated variability associated with built form
- whether including a random effect for built form appears justified


## Model diagnostics and interpretation
The following figures are provided to support interpretation of the model.

![Residual plots](artefacts/regression/cw/residuals.png){width=80%}


You should comment briefly on whether the residuals suggest any major violations of model assumptions.
![Caterpillar plot](artefacts/regression/cw/caterpillar.png){width=80%}

You should explain what this plot represents and how it relates to the concept of partial pooling.

### Notes and limitations

This analysis is observational and descriptive.
The model describes associations between dwelling characteristics and carbon emissions, but does not support causal claims.

Possible extensions include:

- adding further dwelling-level predictors
- comparing fixed- and mixed-effects specifications
- repeating the analysis for a different local authority


## Record of AI use for MTHM503 supervised coursework

| **Date** | **AI tool used** | **Purpose** | **Prompt** | **Section of work used for** |
|:---|:---|:---|:---|:---|
|    |    |    |    |    |
