from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from textblob import TextBlob

app = Flask(__name__)

# Home page - Input text for sentiment analysis
@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    input_text = None
    if request.method == 'POST':
        input_text = request.form['text']
        blob = TextBlob(input_text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        # Save to database
        conn = sqlite3.connect('sentiment.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO analyses (text, sentiment) VALUES (?, ?)', (input_text, sentiment))
        conn.commit()
        conn.close()
    return render_template('index.html', sentiment=sentiment, input_text=input_text)

# History page - View all analyses
@app.route('/history')
def history():
    conn = sqlite3.connect('sentiment.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM analyses')
    analyses = cursor.fetchall()
    conn.close()
    return render_template('history.html', analyses=analyses)

# Delete analysis
@app.route('/delete/<int:id>')
def delete_analysis(id):
    conn = sqlite3.connect('sentiment.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM analyses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)