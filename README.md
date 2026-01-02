# The Sleep-Deprived Internet: Night vs Day Posting, Sentiment, and Quality of Life (DSA210)

**Course:** DSA210 – Introduction to Data Science (Fall 2025–2026)  

## Motivation
People often say “the internet feels different at night.”  
In this project, I test this idea by comparing **night (00:00–06:00)** vs **day (08:00–22:00)** tweets using sentiment fields that already exist in the dataset.

To satisfy the DSA210 requirement of using **two datasets**, I enrich the tweet analysis with a country-level dataset measuring **Quality of Life**. This allows me to explore whether late-night posting behavior varies with broader living conditions.

---

## Research Questions
1. Do **night** tweets differ from **day** tweets in sentiment-related behavior?
2. Is there a relationship between **posting time** and **sentiment category distribution**?
3. Can we predict whether a tweet was written at **night vs day** from the **text**?
4. (Enrichment) At the country level, does **night-posting ratio** relate to **Quality of Life** indicators?

---

## Datasets
### Dataset 1 — Tweets
File: `Tweets[1].csv`  
Source: https://www.kaggle.com/datasets/tango911/airline-sentiment-tweets

### Dataset 2 — Quality of Life Index by Country
File: `quality_of_life_indices_by_country.csv`  
Source: https://www.kaggle.com/datasets/marcelobatalhah/quality-of-life-index-by-country  

## Methods (What I did)
### 1) Preprocessing
- Parsed `tweet_created` into datetime and extracted `hour`
- Created `time_bucket`:
  - **night:** 00–06
  - **day:** 08–22
  - others removed for clean comparison
- Created ML label `is_night` (1 = night, 0 = day)

### 2) Exploratory Data Analysis (EDA)
- Night vs day counts
- Sentiment label distributions
- Confidence comparisons
- Text length distributions

### 3) Hypothesis Testing
- **Welch t-test** on `airline_sentiment_confidence` (night vs day)
- **Chi-square test** on `airline_sentiment` distribution (night vs day)

### 4) Dataset Enrichment (2nd dataset requirement)
- Mapped `user_timezone` to an **approximate country** label (e.g., US/Canada/UK/etc.)
- Aggregated behavior by country:
  - `night_ratio` = mean of `is_night`
- Merged aggregated country stats with Quality of Life dataset on country name
- Computed simple correlations and plotted relationships

### 5) Machine Learning (Text → Night/Day)
- TF-IDF vectorization of `text` (max_features=5000)
- Models:
  - Logistic Regression
  - Random Forest
  - Linear SVM
  - Multinomial Naive Bayes
- Metrics:
  - Accuracy, F1, Precision, Recall

---

## Key Results
### Statistical Tests
- **Welch t-test (confidence):** p ≈ **0.0513** → fail to reject H₀ at 0.05 (difference is small / borderline)
- **Chi-square (sentiment labels):** p ≈ **0.0104** → reject H₀ (label distributions differ by time bucket)

### Enrichment (Country-level)
- night_ratio vs Quality of Life Index ≈ **+0.35**
- night_ratio vs Pollution Index ≈ **−0.33**

---

## Machine Learning Results (with outputs)

### A) Before fixing class imbalance
Checking the target distribution showed imbalance:

- `is_night = 0` (day): **0.845704**
- `is_night = 1` (night): **0.154296**

Model results (imbalanced):

| Model | Accuracy | F1-Score | Precision | Recall |
|------|----------|----------|-----------|--------|
| Logistic Regression | 0.845704 | 0.000000 | 0.000000 | 0.000000 |
| Random Forest | 0.832907 | 0.053830 | 0.213115 | 0.030806 |
| Linear SVM | 0.828519 | 0.113422 | 0.280374 | 0.071090 |
| Multinomial Naive Bayes | 0.845338 | 0.000000 | 0.000000 | 0.000000 |

**Interpretation:**  
Accuracy looks high because the models tend to predict the majority class (“day”).  
This causes very low/zero F1 and recall for the minority class (“night”).

### B) After resampling (oversampling minority class)
I applied a simple oversampling approach using `sklearn.utils.resample` to balance classes:

Balanced distribution:

- `is_night = 0`: **0.50**
- `is_night = 1`: **0.50**

Model results (balanced):

| Model | Accuracy | F1-Score | Precision | Recall |
|------|----------|----------|-----------|--------|
| Logistic Regression | 0.765456 | 0.770078 | 0.755195 | 0.785560 |
| Random Forest | 0.962603 | 0.963464 | 0.941784 | 0.986165 |
| Linear SVM | 0.820147 | 0.826377 | 0.798709 | 0.856031 |
| Multinomial Naive Bayes | 0.757890 | 0.740621 | 0.797506 | 0.691310 |

**Interpretation:**  
After addressing imbalance, all models significantly improve on identifying night tweets.  
This indicates there is real signal in the text, but imbalance can hide it.