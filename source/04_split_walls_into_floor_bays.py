
import hou, math
n=hou.pwd(); g=n.geometry(); g.clear(); a=n.parent(); src=n.inputs()[0].geometry()
for name,default in [('N',(0.,0.,1.)),('up',(0.,1.,0.)),('scale',(1.,1.,1.))]: g.addAttrib(hou.attribType.Point,name,default)
for name in ['floor','column','block','face']: g.addAttrib(hou.attribType.Point,name,0)
g.addAttrib(hou.attribType.Point,'name','window')
fh=a.evalParm('floorheight'); bay=a.evalParm('baywidth'); face=0
for pr in src.findPrimGroup('wall').prims():
    ps=[v.point().position() for v in pr.vertices()]; lo=[min(p[j] for p in ps) for j in range(3)]; hi=[max(p[j] for p in ps) for j in range(3)]
    normal=pr.normal(); tangent=hou.Vector3(normal[2],0,-normal[0]); center=sum(ps,hou.Vector3())/len(ps)
    width=(hi[0]-lo[0]) if abs(normal[2])>.5 else (hi[2]-lo[2])
    rows=pr.intAttribValue('storeys'); cols=max(1,int(math.floor(width/bay+.5))); cw=width/cols; ch=(hi[1]-lo[1])/rows
    for row in range(rows):
        for col in range(cols):
            pos=center+tangent*((col+.5)*cw-width/2); pos[1]=lo[1]+(row+.5)*ch
            p=g.createPoint(); p.setPosition(pos)
            for k,v in [('N',tuple(normal)),('up',(0.,1.,0.)),('scale',(cw,ch,1.)),('floor',int(round(lo[1]/fh))+row),('column',col),('block',pr.intAttribValue('block')),('face',face)]: p.setAttribValue(k,v)
    face+=1
