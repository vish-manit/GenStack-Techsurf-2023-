from flask import Flask, render_template, request, session
from flask_session import Session
import config
import openai
import aicontent

def page_not_found(e):
  return render_template('404.html'), 40

app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        
        query = f"Generate a detailed Product Description for: {submission}"
        query += "\n\nPlease provide a compelling and engaging description that highlights the unique features and benefits of the product." 
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
     
    return render_template('product-description.html', **locals())


@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a detailed Job Description for: {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('job-description.html', **locals())


@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():
    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Generate a robust tweet on the subject: {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('tweet-ideas.html', **locals())
        
@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():
    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a cold email to potential clients about: {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('cold-emails.html', **locals())


@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Generate a facebook or instagram Advertisement copy of our product: {}".format(submission)
        openAIAnswer= aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
       
    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Generate a business idea pitch for: {}".format(submission)
        openAIAnswer= aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
       
    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():
    prompt = ''
    openAIAnswer = ''

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate YouTube video topic ideas on: {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():
    prompt = ''
    openAIAnswer = ''

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Generate YouTube video topic description on: {}".format(submission)
        openAIAnswer = aicontent.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-description.html', prompt=prompt, openAIAnswer=openAIAnswer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
