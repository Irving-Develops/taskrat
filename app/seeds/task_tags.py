from app.models import db, task_tags


def seed_task_tags():
    task_tag1 = task_tags(tag_id=1,task_id=1)
    task_tag2 = task_tags(tag_id=2,task_id=1)
    task_tag3 = task_tags(tag_id=6,task_id=2)
    task_tag4 = task_tags(tag_id=2,task_id=2)
    task_tag5 = task_tags(tag_id=2,task_id=3)
    task_tag6 = task_tags(tag_id=5,task_id=3)

    db.session.add(task_tag1)
    db.session.add(task_tag2)
    db.session.add(task_tag3)
    db.session.add(task_tag4)
    db.session.add(task_tag5)
    db.session.add(task_tag6)

    db.session.commit()

def undo_task_tags():
    db.session.execute('TRUNCATE task_tags RESTART IDENTITY CASCADE;')
    db.session.commit()