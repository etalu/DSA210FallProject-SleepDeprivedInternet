# The Sleep-Deprived Internet: How Posting Time Affects Online Behavior

## Motivation
Most people have noticed that the internet feels different late at night — the posts are more emotional, random, or honest.  
I’ve always been curious if this is just a feeling or if it can actually be seen in the data.  
In this project, I’ll look at Reddit posts to see whether posts written during the night differ from daytime posts in tone, emotion, or engagement.

## Data Sources
- **Main Data:** Public posts on X collected via the X API.
Focus will be on:

Major public accounts or communities
Trending topics and hashtags
Regional or interest-based clusters
Each post includes: text, timestamp, likes/retweets (engagement), and topic/account  

  Each post includes: text, timestamp

- **Extra Data:**  
  - Sentiment scores from tools like VADER or TextBlob.  
  - Local time conversion.  
  - (Optional) Typical sleep hours by region, to compare posting time with common sleep patterns.

## Project Plan
| Stage | Goal | Due Date |
|--------|------|-----------|
| **1. Proposal** | Create GitHub repo and outline the project | **Oct 31** |
| **2. Data & EDA** | Collect X posts and analyze patterns by posting time | **Nov 28** |
| **3. Machine Learning** | Train a simple model to tell if a post was written at night or day | **Jan 2** |
| **4. Final Submission** | Complete visuals, write-up, and presentation | **Jan 9** |

### Steps in Detail
1. **Collect Data** – Gather X posts with timestamps. Separate “night” posts (00:00–06:00) from “day” posts (08:00–22:00).  
2. **Clean Data** – Remove spam, bots, and very short posts.  
3. **EDA** – Compare things like average sentiment, word count, and engagement between day and night.  
4. **Statistical Tests** – Check if differences are statistically significant (for example, using a t-test).  
5. **Machine Learning (later stage)** – Use NLP features (TF-IDF, sentiment values, etc.) to see if a model can predict posting time from text alone.  
6. **Visuals** – Heatmaps of emotion over hours, and word clouds for night vs. day vocabulary.

## Expected Results
I expect to see that late-night posts have stronger emotional language or different engagement patterns.  
The results might show that the “internet at 3 AM” really is a different place; possibly more open, tired, or creative.

## Tools
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- X API  
- TextBlob / VADER for sentiment analysis  
- scikit-learn for ML  
- Jupyter Notebook  
- GitHub for version tracking

## Ethics
Only public X data will be used.  
No usernames or personal information will appear anywhere in the analysis.  
Everything will be analyzed in groups or averages — never on an individual level.

## Notes on AI Tools
ChatGPT was used as a idea opener, for nothing else.
All coding, analysis, and interpretation of data will be done by me.

30 November 23:20 Update: Changed from Reddit to X for data collecting due to the nature of the platforms and X being a better one to see everything inside out.
