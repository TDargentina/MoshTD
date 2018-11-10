import maya.cmds as cmds

# Get all cameras first
cameras = cmds.ls(type=('camera'), l=True)

# Let's filter all startup / default cameras
startup_cameras = [camera for camera in cameras if cmds.camera(cmds.listRelatives(camera, parent=True)[0], startupCamera=True, q=True)]

# non-default cameras are easy to find now.
non_startup_cameras = list(set(cameras) - set(startup_cameras))

# Let's get their respective transform names, just in-case
non_startup_cameras_transforms = map(lambda x: cmds.listRelatives(x, parent=True)[0], non_startup_cameras)

#print non_startup_cameras_transforms

for x in non_startup_cameras_transforms:
    print x.split("_f",3)[0]



