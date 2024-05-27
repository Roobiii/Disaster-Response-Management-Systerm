import json
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from flask import Flask, render_template, request, jsonify 
from plotly.graph_objs import Bar
import plotly
import joblib
from sqlalchemy import create_engine

app = Flask(__name__)

def tokenize(text):
    """
    Tokenizes and lemmatizes the input text.

    Args:
    text: str. Input text.

    Returns:
    clean_tokens: list. List of cleaned tokens.
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = [lemmatizer.lemmatize(tok).lower().strip() for tok in tokens]
    return clean_tokens

# Load data
engine = create_engine('sqlite:///C:/Users/ROOBIKA/Downloads/Disaster-Response-ML-Project-master/Disaster-Response-ML-Project-master/data/DisasterResponse.db')
df = pd.read_sql_table('Disasters', engine)

# Load model
model = joblib.load(r"C:\Users\ROOBIKA\Downloads\Disaster-Response-ML-Project-master\Disaster-Response-ML-Project-master\models\classifier.pkl")

@app.route('/')
@app.route('/index')
def index():
    """
    Index webpage that displays cool visuals and receives user input text for the model.
    """
    # Extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    cats = df[df.columns[5:]]
    cats_counts = cats.mean() * cats.shape[0]
    cats_names = list(cats_counts.index)
    nlarge_counts = cats_counts.nlargest(5)
    nlarge_names = list(nlarge_counts.index)

    # Create visuals
    graphs = [
        {
            'data': [
                Bar(x=genre_names, y=genre_counts)
            ],
            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {'title': "Count"},
                'xaxis': {'title': "Genre"}
            }
        },
        {
            'data': [
                Bar(x=nlarge_names, y=nlarge_counts)
            ],
            'layout': {
                'title': 'Top Message Categories',
                'yaxis': {'title': "Count"},
                'xaxis': {'title': "Category"}
            }
        },
        {
            'data': [
                Bar(x=cats_names, y=cats_counts)
            ],
            'layout': {
                'title': 'Distribution of Message Categories',
                'yaxis': {'title': "Count"},
                'xaxis': {'title': "Category"}
            }
        }
    ]

    # Encode plotly graphs in JSON
    ids = [f"graph-{i}" for i, _ in enumerate(graphs)]
    graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # Render web page with plotly graphs
    return render_template('master.html', ids=ids, graph_json=graph_json)

@app.route('/go')
def go():
    """
    Web page that handles user query and displays model results.
    """
    # Save user input in query
    query = request.args.get('query', '')

    # Use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html. Please see that file.
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )

@app.route('/contact')
def contact():
    """
    Web page for the contact form.
    """
    return render_template('contact.html')

def main():
    """
    Main function to run the Flask app.
    """
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()
