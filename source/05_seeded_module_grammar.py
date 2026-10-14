
import hou, random
n=hou.pwd(); g=n.geometry(); g.clear(); g.merge(n.inputs()[0].geometry()); a=n.parent()
rng=random.Random(a.evalParm('seed')); prob=a.evalParm('blindprob') if a.evalParm('randomize') else 0
front=[p for p in g.points() if p.intAttribValue('floor')==0 and p.attribValue('N')[2]>.5]
door=min(front,key=lambda p:abs(p.position()[0])).number() if front else -1
for p in g.points():
    name='blind' if rng.random()<prob else 'window'
    if a.evalParm('storefront') and p.intAttribValue('floor')==0: name='storefront'
    if a.evalParm('entrance') and p.number()==door: name='door'
    p.setAttribValue('name',name)
