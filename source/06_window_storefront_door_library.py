
import hou, math, random
n=hou.pwd(); g=n.geometry(); g.clear(); a=n.parent()
g.addAttrib(hou.attribType.Prim, "Cd", (0.7,0.7,0.7))
g.addAttrib(hou.attribType.Prim, "name", "")
g.addAttrib(hou.attribType.Prim, "part", "")
g.addAttrib(hou.attribType.Prim, "block", 0)
g.addAttrib(hou.attribType.Prim, "storeys", 1)
stone=(0.55,0.22,0.13); trim=(0.72,0.65,0.52); bronze=(0.055,0.075,0.08)
glass=(0.08,0.20,0.24); roof=(0.21,0.25,0.26); metal=(0.18,0.22,0.23)
def box(c,s,color,part,name="",block=0,storeys=1):
    x,y,z=c; w,h,d=(v/2 for v in s)
    pts=[]
    for p in [(x-w,y-h,z-d),(x+w,y-h,z-d),(x+w,y+h,z-d),(x-w,y+h,z-d),
              (x-w,y-h,z+d),(x+w,y-h,z+d),(x+w,y+h,z+d),(x-w,y+h,z+d)]:
        pt=g.createPoint(); pt.setPosition(p); pts.append(pt)
    for inds in [(3,2,1,0),(4,5,6,7),(0,4,7,3),(1,2,6,5),(0,1,5,4),(3,7,6,2)]:
        prim=g.createPolygon()
        for i in inds: prim.addVertex(pts[i])
        for attr,val in [("Cd",color),("name",name),("part",part),("block",block),("storeys",storeys)]: prim.setAttribValue(attr,val)

for name in ['window','blind','storefront','door']:
    w=a.evalParm('windowwidth'); h=a.evalParm('windowheight')
    if name=='storefront': w=.90; h=.82
    if name=='door': w=.86; h=.94
    # Four wall strips leave a real opening around the inset glass.
    for c,s in [((-(.5+w/2)/2,0,0),((1-w)/2,1,.14)),(((.5+w/2)/2,0,0),((1-w)/2,1,.14)),
                ((0,-(.5+h/2)/2,0),(w,(1-h)/2,.14)),((0,(.5+h/2)/2,0),(w,(1-h)/2,.14))]:
        box(c,s,stone,'wall',name)
    pane=(.32,.42,.43) if name=='blind' else glass
    box((0,0,-a.evalParm('recess')),(w,h,.025),pane,'glass',name)
    t=.045
    for c,s in [((-w/2,0,.065),(t,h+.04,.13)),((w/2,0,.065),(t,h+.04,.13)),
                ((0,-h/2,.065),(w+.04,t,.13)),((0,h/2,.065),(w+.04,t,.13)),((0,0,.075),(t*.65,h,.11))]:
        box(c,s,bronze,'frame',name)
    if name in ['window','blind']:
        box((0,-h/2-.035,.16),(w+.10,.035,.32),trim,'sill',name)
        box((0,.08,.08),(w,.016,.10),bronze,'frame',name)
    if name=='blind':
        for j in range(9): box((0,h/2-.05-j*h*.065,-a.evalParm('recess')+.025),(w-.035,.018,.012),(.55,.55,.49),'blind',name)
    if name=='door':
        for x in [-.045,.045]: box((x,-.10,.16),(.009,.16,.025),trim,'handle',name)
