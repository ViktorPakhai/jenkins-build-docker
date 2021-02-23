from flask import Flask, render_template, url_for, request, redirect
import data

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Error 404: Page Not Found</h1>"

@app.errorhandler(500)
def server_error(e):
    return "<h1>Internal Server Error</h1>"

@app.route('/')
@app.route('/main')
def index():
    keys = sorted(data.books, key=lambda x: (data.books[x]['autor']))[:8]
    return render_template('index.html',books=data.books,
                            keys=keys)
 
@app.route('/books/', defaults={'id': 1})
@app.route('/books/<int:id>')
def book(id):
    book=data.books[id]
    title=book["title"]
    year=book["year"]
    autor=book["autor"]
    description=book["description"]
    picture=book["picture"]
    isdn=book["isdn"]
    form=book["format"]
    picture=book["picture"]
    return render_template('book.html', title=title, autor = autor, description=description, picture=picture,year=year, isdn=isdn, form=form )


if __name__=='__main__':
    app.run(debug =True,host='0.0.0.0')
       
