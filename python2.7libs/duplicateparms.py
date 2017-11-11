assetdef = assetnode.type().definition()
parmtemplates = assetdef.parmTemplateGroup()
parmtemplates.append(interfacefolder)
assetdef.setParmTemplateGroup(parmtemplates)


# make the parmTemplateGroup
ptg = asset.parmTemplateGroup()

# get a copy of the original folder
larm = ptg.findFolder("L Arm")

# make a copy of the original folder as new folder
rarm = ptg.findFolder("L Arm")

# rename/relabel new folder
rarm.setName("rarmfolder")
rarm.setLabel("R Arm")


# rename all the entries in
# the new folder

entries = rarm.parmTemplates()

