from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from flask import session as login_session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
s1 = "927957155989-s6fprmbqothvla95u766aim8nk398qe1.apps.googleusercontent.com"
app.config['GOOGLE_ID'] = s1
app.config['GOOGLE_SECRET'] = 'pcAyyCHWSkmLcAfehqCTJ5L2'
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# check if user is currently logged in
def isLogged():
    if 'google_token' in login_session:
        return True
    else:
        return False


# ask google to present login page for the user
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


# remove user for the logged session
@app.route('/logout')
def logout():
    login_session.pop('google_token', None)
    return redirect(url_for('showCategory'))


# accepts google authorization for user and add the user access token to
# the session
@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    login_session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')

    login_session['user_email'] = me.data.get('email')

    return redirect(url_for('showCategory'))


@google.tokengetter
def get_google_oauth_token():
    return login_session.get('google_token')


# view one category JSON endpoint
@app.route('/category/<int:cat_id>/JSON')
def categoryJSON(cat_id):
    category = session.query(Category).filter_by(id=cat_id).one()
    return jsonify(Category=[i.serialize for i in category])


# view all category items JSON endpoint
@app.route('/category/<int:cat_id>/items/JSON')
def categoryItemsJSON(cat_id):
    items = session.query(Item).filter_by(cat_id=cat_id).all()
    return jsonify(Item=[i.serialize for i in items])


# view specific item JSON endpoint
@app.route('/category/<int:cat_id>/items/<int:item_id>/JSON')
def itemJSON(cat_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)


# view all categories JSON endpoint
@app.route('/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])


# default entry, sjow all categories in HTML
@app.route('/')
@app.route('/category/')
def showCategory():
    categories = session.query(Category).all()
    return render_template('categories.html',
                           categories=categories,
                           logged=isLogged(),
                           email=login_session['user_email'])


# show all items in chosen category in HTML
@app.route('/category/<int:cat_id>/items')
def categoryItems(cat_id):
    items = session.query(Item).filter_by(cat_id=cat_id).all()
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=cat_id).one()
    return render_template('itemsInCategory.html',
                           items=items,
                           categories=categories,
                           cat=category,
                           logged=isLogged(),
                           email=login_session['user_email'])


# show one item in HTML
@app.route('/item/<int:item_id>')
def item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item.html',
                           item=item,
                           logged=isLogged(),
                           email=login_session['user_email'])


# show edit form for item in HTML
@app.route('/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id):
    if not isLogged():
        return render_template('error403.html')
    editedItem = session.query(Item).filter_by(id=item_id).one()

    if editedItem.creator_email != login_session['user_email']:
        return render_template('error403.html')

    if request.method == 'POST':
        if request.form['title']:
            editedItem.title = request.form['title']
        if request.form['description']:
            editedItem.description = request.form['description']
        return redirect(url_for('showCategory'))
    else:
        return render_template('editItem.html',
                               item=editedItem,
                               email=login_session['user_email'])


# show delete form for item in HTML
@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(item_id):
    if not isLogged():
        return render_template('error403.html')
    itemToDelete = session.query(Item).filter_by(id=item_id).one()

    if itemToDelete.creator_email != login_session['user_email']:
        return render_template('error403.html')

    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategory'))
    else:
        return render_template(
            'deleteItem.html', item=itemToDelete,
            email=login_session['user_email'])


# show create new item form in HTML
@app.route('/category/<int:cat_id>/item/new/', methods=['GET', 'POST'])
def newItem(cat_id):
    if not isLogged():
        return render_template('error403.html')
    if request.method == 'POST':
        # print request.form
        newItem = Item(title=request.form['title'],
                       description=request.form['description'],
                       cat_id=request.form['cat_id'],
                       creator_email=login_session['user_email'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory'))
    else:
        categories = session.query(Category).all()
        category = session.query(Category).filter_by(id=cat_id).one()
        return render_template('newItem.html',
                               categories=categories,
                               cat=category,
                               email=login_session['user_email'])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
