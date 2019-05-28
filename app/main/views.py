from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,login_user,logout_user,current_user
from ..models import Pitch,Comments,User
from .forms import PitchForm,CommentForm,UpdateProfile
from ..import db,photos
import markdown2


@main.route('/')
def index():
    title = 'Home'

    pitch = Pitch.query.all()

    if pitch is None:
        abort (404)
    
    print(pitch)
    return render_template( 'index.html' ,title = title)


@main.route('/pitch/new',methods=['GET','POST'])
@login_required
def pitch():
    form= PitchForm()
    if form.validate_on_submit():
        title=form.title.data
        description=form.description.data
        upvote=0
        downvote=0
        new_pitch=Pitch(title=title,description=description,upvote=upvote,downvote=downvote)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title= 'Pitches'
    return render_template('new_pitch.html',pitch_form=form,pitch =pitch)

@main.route('/comment/new/', methods=['GET','POST'])
@login_required
def new_comment():

    '''
    View new comment route function that returns a page with a form to create a pitch for the specified category
    '''
    comments = Comments.query.all()
    form =CommentForm()
    if form.validate_on_submit():
        name=form.name.data
        new_comment=Comments(name=name)
        new_comment.save_comment()

        return redirect(url_for('.index'))

    title = "New Comment"
    return render_template('new_comment.html', title=title, form=form,comments=comments)

@main.route('/pitch_comments/<int:id>',methods=['GET','POST'])

def pitch_comments(id):
    pitch =Pitch.query.get_or_404(id)
    comment= Comments.query.all()
    form=CommentForm()
    if request.args.get("upvote"):
        pitch.upvote = pitch.upvote+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_comments/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("downvote"):
        pitch.downvote=pitch.downvote+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_comments/{pitch_id}".format(pitch_id=pitch.id))

    if form.validate_on_submit():
        comment = form.comments.data

        new_comment = Comments(id=id,review=review,user_id=current_user.id)

        new_review.save_comment()
        return redirect(url_for('main.pitch_comments',id=id))
    reviews = Comments.query.all()
    return render_template('new_comment.html',comment=comment,pitch=pitch,review_form=form)

    title= 'Pitches'
    return render_template('new_comment.html',pitch=pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/review/<int:id>')
# def single_review(id):
#     review=Review.query.get(id)
#     if review is None:
#         abort(404)
#     format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('review.html',review = review,format_review=format_review)

 