
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

def footprint(w,d):
    ww=min(w-3.,max(3.,a.evalParm('wingwidth'))); ext=max(3.,a.evalParm('wingdepth'))
    return [(-w/2,-d/2),(w/2,-d/2),(w/2,d/2),(-w/2+ww,d/2),(-w/2+ww,d/2+ext),(-w/2,d/2+ext)]
def lshape(w,d,h,y,color,part,name='',block=0,storeys=1):
    plan=footprint(w,d); lower=[];upper=[]
    for x,z in plan:
        p=g.createPoint();p.setPosition((x,y-h/2,z));lower.append(p)
        p=g.createPoint();p.setPosition((x,y+h/2,z));upper.append(p)
    polys=[lower,list(reversed(upper))]
    for j in range(len(plan)):k=(j+1)%len(plan);polys.append([lower[j],upper[j],upper[k],lower[k]])
    for vertices in polys:
        pr=g.createPolygon()
        for p in vertices:pr.addVertex(p)
        for attr,val in [('Cd',color),('name',name),('part',part),('block',block),('storeys',storeys)]:pr.setAttribValue(attr,val)

y=0.;fh=a.evalParm('floorheight')
for i in range(1,a.evalParm('blocks')+1):
    w=max(8.,a.evalParm('width%d'%i));d=max(6.,a.evalParm('depth%d'%i));count=max(1,a.evalParm('levels%d'%i));h=count*fh;plan=footprint(w,d)
    # Each slab follows the concave L footprint and leaves the courtyard open.
    for level in range(1,count+1):
        yy=y+level*fh
        lshape(w,d,.14,yy,roof,'floor_slab')
        if a.evalParm('borders'):
            for j,(x,z) in enumerate(plan):
                nx,nz=plan[(j+1)%len(plan)];dx=nx-x;dz=nz-z;length=math.hypot(dx,dz);out=(dz/length,-dx/length)
                c=((x+nx)/2+out[0]*.17,yy,(z+nz)/2+out[1]*.17)
                s=(length+.25,.18,.68) if abs(dx)>.1 else (.68,.18,length+.25)
                box(c,s,trim,'continuous_shade')
    y+=h
# Continuous charcoal parapet on the flat L-shaped roof.
w=max(8.,a.evalParm('width%d'%a.evalParm('blocks')));d=max(6.,a.evalParm('depth%d'%a.evalParm('blocks')));plan=footprint(w,d)
for j,(x,z) in enumerate(plan):
    nx,nz=plan[(j+1)%len(plan)];length=math.hypot(nx-x,nz-z)
    s=(length+.15,.42,.16) if abs(nx-x)>.1 else (.16,.42,length+.15)
    box(((x+nx)/2,y+.22,(z+nz)/2),s,bronze,'parapet')
# A simple flat entry canopy with two supports.
if a.evalParm('entrance'):
    w=a.evalParm('width1');d=a.evalParm('depth1');ww=min(w-3.,a.evalParm('wingwidth'))
    cx=ww/2;front=d/2
    box((cx,2.72,front+.90),(5.2,.14,2.2),bronze,'canopy')
    for x in [cx-2.25,cx+2.25]:box((x,1.34,front+1.70),(.10,2.68,.10),bronze,'canopy_post')
    box((cx,.055,front+1.1),(5.6,.11,2.5),trim,'entry_step')
w=a.evalParm('width1');d=a.evalParm('depth1');ext=a.evalParm('wingdepth')
box((0,-.18,ext/2),(w+6,.36,d+ext+6),(.36,.39,.38),'plaza')
