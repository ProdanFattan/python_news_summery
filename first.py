import tkinter as tk
import nltk
from newspaper import Article
from textblob import TextBlob


def summarize():
    link = utext.get('1.0','end').strip()

    news = Article(link)

    news.download()
    news.parse()

    news.nlp()

    title.config(state='normal')
    summary.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    feedback.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0',news.title)
    
    summary.delete('1.0', 'end')
    summary.insert('1.0',news.summary)

    author.delete('1.0', 'end')
    author.insert('1.0',news.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0',news.publish_date)

    feed_back = TextBlob(news.text)
    if feed_back.polarity > 0:
        feedback.delete('1.0', 'end')
        feedback.insert('1.0', 'Positive News')
    elif feed_back.polarity < 0:
        feedback.delete('1.0', 'end')
        feedback.insert('1.0', 'Negative News')
    else:
        feedback.delete('1.0', 'end')
        feedback.insert('1.0', 'Neutral News')
    


    title.config(state='disabled')
    summary.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    feedback.config(state='disabled')

    


#GUI
root = tk.Tk()
root.title("News Summarizer.")
root.geometry('800x600')


#URL
ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1,width=140)
utext.pack()
btn = tk.Button(root,text = 'Summarize',command=summarize)
btn.pack()

#title label
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1,width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

#Summary
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=18,width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

#author label
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1,width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()


#publication date
plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1,width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()


#feedback
selabel = tk.Label(root, text="Feedback")
selabel.pack()

feedback = tk.Text(root, height=1,width=140)
feedback.config(state='disabled', bg='#dddddd')
feedback.pack()



root.mainloop()
