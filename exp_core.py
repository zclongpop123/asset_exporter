#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Jan 20 17:05:09 2022
#========================================
import os
import maya.cmds as mc
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def do_export_fbx(output_path):
    '''
    '''
    if not mc.pluginInfo('fbxmaya.mll', q=True, l=True):
        try:
            mc.loadPlugin('fbxmaya.mll')
        except:
            pass

    cameras = mc.listRelatives(mc.ls(ca=True), p=True, fullPath=True)
    cameras = [cam for cam in cameras if cam not in ('|front', '|persp', '|side', '|top')]
    if not cameras:
        cameras.append(mc.camera()[0])

    mc.select(cameras, r=True)
    mc.file(output_path, options='v=0;', typ='FBX export', pr=True, es=True, force=True)
    


def export(filePath):
    '''
    '''
    if not os.path.isfile(filePath):
        return
    
    mc.file(filePath, o=True, f=True)
    
    output_path = os.path.join(os.path.dirname(filePath), 'cameras.fbx')
    do_export_fbx(output_path)
    
    
    


if __name__ == '__main__':
    main()
