# coding: utf-8
#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Jan 20 17:05:09 2022
#========================================
import re
import os
import logging
import maya.cmds as mc
import pymel.core as pm
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
logger = logging.getLogger()


def load_plugin(plugin_name):
    '''
    '''
    if not mc.pluginInfo(plugin_name, q=True, l=True):
        try:
            mc.loadPlugin(plugin_name)
        except:
            pass




def bake_cameras(camera_name, start_frame, end_frame):
    '''
    '''
    cam = pm.PyNode(camera_name)
    temp_loc = pm.spaceLocator()
    cons_node = pm.parentConstraint(cam, temp_loc)
    pm.bakeResults(temp_loc, t=(start_frame, end_frame), hi='below', simulation=True)
    pm.delete(cons_node)

    try:
        for attr in ('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz'):
            cam.attr(attr).setLocked(False)
        pm.parent(cam, w=True)
    except:
        return
    pm.parentConstraint(temp_loc, cam)
    pm.bakeResults(cam, t=(start_frame, end_frame), hi='below', simulation=True)




def export_camera(filePath, start_frame, end_frame):
    '''
    '''
    load_plugin('fbxmaya.mll')

    cameras = pm.listRelatives(pm.ls(ca=True), p=True, fullPath=True)
    cameras = [cam for cam in cameras if cam.name() not in ('|front', '|persp', '|side', '|top')]
    if not cameras:
        logger.info('Can not find cameras.')
        return

    for cam in cameras:
        bake_cameras(cam, start_frame, end_frame)

    file_name = os.path.splitext(filePath)[0]
    output_path = u'{0}_export_cam.{1}-{2}.fbx'.format(file_name, start_frame, end_frame)

    pm.select(cameras, r=True)
    mc.file(output_path, options='v=0;', typ='FBX export', pr=True, es=True, force=True)





def export_assets(filePath, start_frame, end_frame):
    '''
    '''
    load_plugin('fbxmaya.mll')

    file_name = os.path.splitext(filePath)[0]
    for asset_grp in mc.ls('*::UE4', typ='transform'):
        if not mc.referenceQuery(asset_grp, inr=True):
            continue

        asset_path = mc.referenceQuery(asset_grp, f=True)

        count_number = re.search('{\d+}', asset_path)
        if count_number:
            asset_name = os.path.splitext(os.path.basename(asset_path))[0] + count_number.group()[1:-1]
        else:
            asset_name = os.path.splitext(os.path.basename(asset_path))[0]

        output_path = u'{0}_export_{1}.{2}-{3}.fbx'.format(file_name, asset_name, start_frame, end_frame)
        mc.select(asset_grp, r=True)
        pm.mel.eval('FBXExportBakeComplexAnimation -v true;')
        mc.file(output_path, options='v=0;', typ='FBX export', pr=True, es=True, force=True)




def export(filePath):
    '''
    '''
    if not os.path.isfile(filePath):
        return

    logger.info(filePath)
    try:
        mc.file(filePath, o=True, f=True)
    except RuntimeError as e:
        logger.info('Exception occurred', exc_info=True)

    start_frame = int(mc.playbackOptions(q=True, ast=True))
    end_frame   = int(mc.playbackOptions(q=True, aet=True))

    export_camera(filePath, start_frame, end_frame)
    export_assets(filePath, start_frame, end_frame)




if __name__ == '__main__':
    main()
