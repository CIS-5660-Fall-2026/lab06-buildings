
import hou
n=hou.pwd(); g=n.geometry(); g.clear(); g.merge(n.inputs()[0].geometry())
offset=g.boundingBox().minvec()[1]
for p in g.points(): p.setPosition(p.position()-hou.Vector3(0,offset,0))
for group in ['wall','roof','base']:
    if not g.findPrimGroup(group): g.createPrimGroup(group)
for pr in g.prims():
    y=pr.normal()[1]
    g.findPrimGroup('roof' if y>0.5 else 'base' if y<-.5 else 'wall').add(pr)
