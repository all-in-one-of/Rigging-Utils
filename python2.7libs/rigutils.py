import hou

def makeRctrl():
    nodes = hou.selectedNodes()
    for node in nodes:
        # Lock parameters so unexpected behavior isn't allowed
        value = 1
        node.parm('tx').lock(value)
        node.parm('ty').lock(value)
        node.parm('tz').lock(value)
        node.parm('sx').lock(value)
        node.parm('sy').lock(value)
        node.parm('sz').lock(value)
        node.parm('px').lock(value)
        node.parm('py').lock(value)
        node.parm('pz').lock(value)
        node.parm('scale').lock(value)
