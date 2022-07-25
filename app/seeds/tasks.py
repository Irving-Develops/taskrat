from app.models import db, Task
from datetime import datetime

def seed_tasks():

    task1 = Task(
    title='Clearing Swamprats Out Me Lawn',
    description = "Well I knew it from the get-go, got me a big ol' infestation, not pretty I tell you hwut. Lookin' for a steady hand to help me e-'rat'icate them heh heh",
    city='New Vegas',
    state='Nevada',
    country='U.S.A.',
    price=500,
    poster_id=1,
    danger_level=1,
    )

    task2 = Task(
    title='Finding Me Lost Keys',
    description = "Done did myself dirty this time, dropped my keys at the far edge of the badlands, like a damn fool. Now this t'aint wouldn't be such a big deal, cept for that band o' mercenaries what lives out there. I need a stealthy hand attached to a stealthy man (or wo-man) to help me sneak past them lawless suckers. A little familiarity with explosives t'wouldn't hurt neither.",
    city='Oklahoma City',
    state='Oklahoma',
    country='U.S.A.',
    price=800,
    poster_id=2,
    danger_level=3,
    )
    
    task3 = Task(
    title='Got a whole heap of mines around my property',
    description = "Just moved into my house and the paranoid tenants that used to live there left dang ol' MINES all over the place! Help me clear them out before any more of my chickens blow up!",
    city='New Seattle',
    state='Washington',
    country='U.S.A.',
    price=600,
    poster_id=3,
    danger_level=4,
    )

    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)

    db.session.commit()


def undo_tasks():
    db.session.execute('TRUNCATE tasks RESTART IDENTITY CASCADE;')
    db.session.commit()

