import sys

sys.path.append('../')
from app.models import User, Post
from app import create_app, db


def run():
    db.create_all()
    user = User(username='ddxygq', email='ddxygq@gmail.com')
    user2 = User(username='cj318.cn', email='hbzegkg@126.com')
    user.set_password('123456')
    db.session.add(user)
    user2.set_password('123456')
    db.session.add(user2)
    db.session.commit()

    u = User.query.get(1)
    # post有一个动态属性，post.author，将返回发出动态的user
    for i in range(5):
        body = '%s post %s' % (u.username, str(i))
        print(body)
        p = Post(body=body, author=u)
        db.session.add(p)
        db.session.commit()

    posts = Post.query.all()
    for post in posts:
        print(post.id, post.body, post.timestamp, post.user_id, post.author)


def show_user():
    create_app()
    users = User.query.all()
    for u in users:
        posts = Post.query.filter_by(user_id=u.id).all()
        print(u.id, u.username, u.email, u.password_hash, posts)


if __name__ == '__main__':
    # run()
    show_user()
