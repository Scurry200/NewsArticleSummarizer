import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import article



def summarize():
    url2 = urlText.get('1.0',"end").strip()
    nltk.download('punkt')
    url =  # insert url here 'url'

    # summarizer here
    newsArticle = Article(url)
    article.download()
    article.parse()
    article.nlp()
    title.config(state='normal')
    author.config(state='normal')
    date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    date.delete('1.0', 'end')
    date.insert('1.0', date.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', article.sentiment)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'polarity: {analysis.polarity} Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}))






    title.config(state='disabled')
    author.config(state='disabled')
    date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')




    print('Title of article: {article.title}')
    print('author/s: {article.authors}')
    print('Date: {article.publish_date}')
    print('summary: {article.summary}')

    # sentiment and polarity analysis









root = tk.tk()
root.title("news summarizer")
root.geometry('1200x600')#number of pixels

titleLabel = tk.label(root, text="Title")
titleLabel.pack()
title = tk.text(root,height=1,width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()


authorLabel = tk.label(root, text="Author")
authorLabel.pack()
author = tk.text(root,height=1,width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()


dateLabel = tk.label(root, text="Date")
dateLabel.pack()
date = tk.text(root,height=1,width=140)
date.config(state='disabled', bg='#dddddd')
date.pack()

summaryLabel = tk.label(root, text="summary")
summaryLabel.pack()
summary = tk.text(root,height=20,width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

sentimentLabel = tk.label(root, text="sentimnt")
sentimentLabel.pack()
sentiment = tk.text(root,height=1,width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

urlLabel = tk.label(root, text="insert url")
urlLabel.pack()
urltext = tk.text(root,height=1,width=140)
urltext.config(state='disabled', bg='#dddddd')
urltext.pack()

button = tk.button(root, text="summary", command=summarize)




root.mainloop()
