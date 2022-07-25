from app.models import db, Tag


def seed_tags():
    guns = Tag(type="Guns", description="Accuracy and damage with every kind of conventional firearm, from pistols and rifles to miniguns.")
    explosives = Tag(type="Explosives", description=" Ability of handling explosive traps and creating explosives.")
    medicine = Tag(type="Medicine", description="Knows how to perform surgery and cure illness.")
    repairs = Tag(type="Repairs", description="Know your way around a car? Can you batten down the hatches? Fix my AC unit? Then you’re just what we need!")
    survival = Tag(type="Survival", description="Just the mission for someone that knows their way through the fields without stepping on any pesky mines!")
    stealth = Tag(type="Stealth", description="Creeping and crawling around, a fly on the wall, if that sounds like you, just give a call!")
    pilot = Tag(type="Pilot", description="Plane, helicopter or anything else that flies, you’re the right person for the job.") 
    hacking = Tag(type="Hacking", description="Monster drinker who lives in your mothers basement? Can hack anything with a screen? These missions will be a piece of cake.")
    hand_to_hand = Tag(type="Hand to Hand", description="Calling all brawlers. Martial arts, Juijitsu, and your classic haymakers.") 
    charisma = Tag(type="Charisma", description="Are you a smooth talker with a slight of hand? This job is for you.") 

    db.session.add(guns)
    db.session.add(explosives)
    db.session.add(medicine)
    db.session.add(repairs)
    db.session.add(survival)
    db.session.add(stealth)
    db.session.add(pilot)
    db.session.add(hacking)
    db.session.add(hand_to_hand)
    db.session.add(charisma)

    db.session.commit()

def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()