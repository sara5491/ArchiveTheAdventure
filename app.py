import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'archivetheadventure@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_photos")
def get_photos():
    photos = list(mongo.db.photos.find())
    return render_template("photos.html", photos=photos)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    photos = list(mongo.db.photos.find({"$text": {"$search": query}}))
    return render_template("photos.html", photos=photos)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    if session["user"]:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    # get the photos uploaded by session user
        photos = list(mongo.db.photos.find(
            {"created_by": session["user"]}))

        return render_template("profile.html", username=username, photos=photos)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    categories = list(mongo.db.categories.find())
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")

        msg = Message(email,
                      sender=("email"),
                      recipients=['archivetheadventure@gmail.com'])

        msg.body = message
        mail.send(msg)
        flash("Email Sent Successfully")
        return redirect(url_for("contact"))

    return render_template("contact.html", categories=categories)


@app.route("/add_photo", methods=["GET", "POST"])
def add_photo():
    if request.method == "POST":
        photo = {
            "category_name": request.form.get("category_name"),
            "photo_name": request.form.get("photo_name"),
            "photo_description": request.form.get("photo_description"),
            "date_taken": request.form.get("date_taken"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.photos.insert_one(photo)
        flash("Photo Successfully Added")
        return redirect(url_for("get_photos"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_photo.html", categories=categories)


@app.route("/edit_photo/<photo_id>", methods=["GET", "POST"])
def edit_photo(photo_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "photo_name": request.form.get("photo_name"),
            "photo_description": request.form.get("photo_description"),
            "date_taken": request.form.get("date_taken"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.photos.update_one({"_id": ObjectId(photo_id)}, {
        "$set": submit
        })
        flash("Photo Successfully Updated")

    photo = mongo.db.photos.find_one({"_id": ObjectId(photo_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_photo.html", photo=photo, categories=categories)


@app.route("/delete_photo/<photo_id>")
def delete_photo(photo_id):
    mongo.db.photos.delete_one({"_id": ObjectId(photo_id)})
    flash("Photo Successfully Deleted")
    return redirect(url_for("get_photos"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/browse")
def browse():
    photos = list(mongo.db.photos.find())
    return render_template("browse.html", photos=photos)


@app.errorhandler(404)
def page_not_found(e):
    error = 404
    error_msg = "Page Not Found."
    return render_template('404.html', error=error, error_msg=error_msg), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)