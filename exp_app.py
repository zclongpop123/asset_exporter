#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Jan 20 17:05:09 2022
#========================================
import os
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def main(file_list):
    '''
    '''
    os.environ['MAYA_SKIP_USERSETUP_PY'] = str()

    try:
        import maya.standalone
        maya.standalone.initialize(name='python')
    except: 			
        return


    import exp_core
    for filePath in file_list:
        exp_core.export(filePath)


    maya.standalone.uninitialize()


if __name__ == '__main__':
    main(['D:/work/asset_exporter/example/test_scene.ma'])
