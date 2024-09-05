# Projet noté

### By Kévin Michoud and Pierre Pelletier.

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


## How is the project graded: 

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



## Possible AI models to use: 
go to [HuggingFace](https://huggingface.co/models), You can create a free account and try most models on their servers.

#### Natural Language Processing (NLP) Models:
- [Language Identification](https://huggingface.co/facebook/fasttext-language-identification)
- [Named entity recognition (NER)](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english?text=My+name+is+Sarah+and+I+live+in+London) : can be used to identify people, organizations, locations, dates, products, countries, currencies, etc.
- [Question answering](https://huggingface.co/deepset/roberta-base-squad2?context=A+witch+is+a+figure+often+depicted+as+possessing+magical+powers%2C+typically+associated+with+casting+spells%2C+brewing+potions%2C+and+communing+with+the+supernatural.+Depending+on+the+tale%2C+witches+can+be+benevolent+healers+or+malevolent+beings%2C+embodying+the+mysterious+and+enigmatic+forces+of+nature+and+the+unknown.&text=Who+is+the+main+character+%3F): Given a text, answers questions
- [Sentence similarity](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) Can be used to compare sentence and compute their similarities.
- [Classification](https://huggingface.co/tasksource/deberta-small-long-nli?candidate_labels=IT%2C+slavery%2C+hypnosis&multi_class=true&text=Neo%2C+a+computer+hacker%2C+discovers+that+the+world+he+lives+in+is+a+simulated+reality+created+by+machines+to+control+humanity%2C+leading+him+to+join+a+rebellion+against+the+system.+As+he+learns+to+manipulate+the+Matrix%2C+Neo+becomes+central+to+the+fight+for+human+freedom%2C+challenging+the+very+nature+of+reality.): Given a list of categories and a text, compute a simalarity score for the text in relation with each category.
- [Sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) Compute the polarity of a given text (Positive, neutral and negative)
- [Summarization](https://huggingface.co/facebook/bart-large-cnn) Given a text and a length, summarize the text to the requested length
- Text generation: the newest open-source models, such as LLama 3.1, or Mistral are (probably) too big to run on your machine. You could either run them on the cloud via an API (see [groqcloud](https://console.groq.com/playground)) or run older models like GPT2.

#### Other models, for example:
- [Speech-to-text](https://huggingface.co/openai/whisper-large-v3): To convert audio to text
- Image analysis: To categorize or describe image. 

## Possible ways to acquire data:
- **Public datasets**:
  - **[Kaggle](https://www.kaggle.com/datasets)**: A vast platform offering datasets across various domains, along with tools for data exploration and analysis.
    - See this [dataset](https://www.kaggle.com/datasets/sayankr007/cyber-bullying-data-for-multi-label-classification) and <u>[code](https://www.kaggle.com/code/marcelooa/cyberbullying-classification-using-bert/notebook)</u> about hate speech detection
  - **[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)**: A well-known repository providing a wide range of datasets for different machine learning tasks.
  - **[European Union Open Data Portal](https://data.europa.eu/euodp/en/data)**: A portal offering datasets from the European Union on diverse topics like economics, environment, and education.
  - **[World Bank Open Data](https://data.worldbank.org/)**: Provides access to global development data, including economic, social, and environmental statistics.
- **Public APIs**:
  - **[Data.gouv.fr API](https://www.data.gouv.fr/en/apidoc/)**: Offers access to a vast collection of datasets provided by the French government, covering various sectors such as healthcare, education, and public services.
  - **[List of free API](https://github.com/public-apis/public-apis)**
- **Web scraping** is the process of automatically extracting data from websites. We'll explore the libraries f BeautifulSoup, Scrapy, and Selenium. It's important to be aware of the legal and ethical considerations.

