# Projet noté

### By Kévin Michoud and Pierre Pelletier.

By group of 3.

A data analysis project followed by a live presentation of your work

The main goal is to :
- find an interesting question/idea that you would like to answer or explore, 
- find data related to your question (mostly textual data, but we are flexible), 
- exploit the data in order to shed light on your question/idea, we would like you to use an "AI" model. 
- finally present the process and the results. 

It can be an "academic" research question, a business idea or even something more personal.  
  

**For example**:
### **Academic Question: Public Perception of Bitcoin During High Volatility Spikes**

You might be interested in studying the relationship between public opinion and the Bitcoin exchange rate during periods of high volatility, such as significant surges or drops. How do people react when Bitcoin is skyrocketing or plummeting? For instance, individuals skeptical of Bitcoin might feel validated when it’s dropping, while those already invested might express anger or frustration. Conversely, during a surge, some people may get excited about the potential gains, while others might caution against an impending downfall.

To explore this, you could use Bitcoin price data to identify *bull runs* (periods of rapid price increases) or *bear crashes* (periods of rapid price drops). Then, gather social media data (from platforms like Twitter or Reddit) and press coverage where people discuss Bitcoin at the time of the volatility. These texts can be analyzed using [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) to gauge public sentiment during these volatility spikes.

- **Data**: Bitcoin price data though an API, social media posts, news articles, and forum discussions through <u>scraping</u>.
- **AI**: Emotion analysis models to categorize public reactions (anger, frustraion, happiness etc.) and identify trends in sentiment during periods of high volatility. Some multimodal AI can be used to interpret images such as memes.

### **Personal Idea: Analyzing Sexism in a YouTube Genre**

For a personal project, you could analyze the presence and trends of sexism within a specific YouTube genre. This project would involve collecting data from YouTube, such as the number of views, likes, comments, and the frequency of certain types of content being uploaded in this genre. By tracking these metrics and analyzing the content of comments, you could identify patterns and trends related to sexist behavior or language over time.

The analysis could also include identifying and categorizing sexist language or sentiments in the comments of popular videos within the genre. Additionally, you could compare the level of sexism in this genre to other YouTube genres to understand how it stands in the broader context of online content.

- **Data**: YouTube video statistics (views, likes, comments), upload frequency, and audience engagement metrics through <u>scraping</u>. 
- **AI**: Use of a large language model (LLM), such as LLaMA or ChatGPT via an API, for detecting and analyzing sexist language in comments, as well as trend analysis to evaluate the prevalence of sexism in the genre over time.


### **Business Idea: Book Recommendation Based on Content Similarity**

Another idea would be to develop a small app that suggests books similar to the ones a reader already likes. For example, a user could enter the name of a book, and the app would offer tailored suggestions.

You would start by gathering book-related data from sources like Amazon, Goodreads, or Project Gutenberg, including metadata such as author, publication year, genre, summary, themes, and ratings. Then, you could build an AI model that suggests books based on content similarity, focusing on the book's description or summary rather than just genre or user ratings.

The app could provide a list of recommended books with brief explanations of why they were chosen. The user interface could also allow filtering by genre, length, or publication date to make the recommendations even more personalized.

- **Data**: Book metadata including title, author, genre, summary, publication year, and user ratings. (<u>scrapping + public dataset</u>).
- **AI**: Natural language processing (NLP) models to analyze content similarity and generate book recommendations.


## How is the project graded: 

### 1. Data acquisition
- **Quality of the data acquired** 
- **Relevance of the data to your idea/research question** 
- **Process of acquisition**: Finding data from a public dataset can be pretty easy, scrapping data from a modern dynamic website can be extremely challenging on the other hand. We expect you to scrap at least some of your data. If not, we expect the other aspect of your project to be more developped/ ambitious.


### 2. Data Cleaning
- **Thoroughness of Data Cleaning**: Ensure your dataset is free from inconsistencies, missing values, duplicates, and errors.

- **Handling Missing Data**: Explain your approach to dealing with missing values, whether through imputation, removal, or other methods. Justify your choices based on your research objectives.

- **Data Transformation**: Prepare your data for analysis by normalizing, encoding, or transforming it as needed. Effective preparation is crucial for accurate results. Choose the right format to store your data: Pandas, SQL, NoSQL, Json?  

- **Documentation**: Clearly document your data cleaning steps, including decisions made and tools used. Proper documentation is essential for reproducibility and understanding the impact on your final analysis.

### 3. Data Transformation and Analysis
- **Model Selection and Application**: Which model did you choose?  Is the model well-suited to address your research question or business problem? Justify your choice of model and explain why it’s relevant to the data and the goals of your project.

- **Correctness of Implementation**: How is your model implemented ? Does it yield results?

- **Deriving Insights from the Model**: How do you interpret the model's outputs? We evaluate how effectively you use the model’s results to generate meaningful insights or actionable recommendations. The derived insights should be directly linked to your original research question or business objective.

#### Communication
- **Organisation of your files**: How well-organised is your work? Is it easy to navigate through your code files and data, to understand and read your code ? We expect you to hand over a project to us, preferably we would like that project to be available online though GitHub or Gitlab. Keep in mind that this can be a showcase of your abilities to potential recruiters.
- **Live presentation of your work** Can you explain your project clearly to others? Present your idea, the data, the model and the results and all the steps in between that you find interesting and relevant.

