# Text Mining
Here You can find my projects which are connected to Text Mining.

### Lab1
- Using the `re` library
- Working with regex (regular expressions)
- Removing numbers, html characters, punctuation from text 
- Extracting hashtags, emoticons

### Lab2
- Creation of a function that cleans up text (pulling out emoticons, converting letters to lower case, removing numbers, html tags, punctuation, removing excessive spaces)
- Library `stopwords`.
- Implementation of a function that removes unnecessary words
- Library `nltk`.
- Implementation of the stemming process, based on Porter's algorithm

### Lab3
- Working on cleared text using previously created functions
- Creation of a bag of words `bow`
- Generation of a word cloud using `WordCloud` (graphical visualisation of words from the text, together with their frequency of occurrence)

### Lab4:
- Library `sklern` (`scikit-learn`)
- Measures for assessing word importance (count, binary, TF-IDF)
- Creation of a `text-tokenizer` function that accepts cleaned, steamed text, word length is longer than 3
- Create an instance of the vectorizer `vectorizer= TfidfVectorizer(tokenizer=text_tokenizer)`
- Vectorise the text to be processed `X_transform = vectorizer.fit_transform(X)`
- Print the resulting matrix `X_transform`
- Extracting terms using `vectorizer.get_feature_names_out()`.
- Extraction of the top 10 most frequently occurring tokens
- Extraction of the top 10 most frequent tokens
- Finding the top 10 documents that contain the most tokens

