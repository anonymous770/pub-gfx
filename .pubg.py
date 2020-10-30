import os, shutil
import subprocess as sub

con = ('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android')

dis_file = ('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Active.sav')

raw_file = ('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved')

sub.call(['cp','-r', 'Graphics/files/Active.sav', dis_file])
sub.call(['cp', '-r', 'Graphics/rawdata', raw_file])

wo = open('/sdcard/gfx/Graphics/files/clasic.ini', 'a+')
ro = open('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini', 'r+')
lines = ro.readlines()
wo.write('\n\n')
for i in lines:
	wo.write(i)

os.remove('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini')
os.system('cd Graphics/files && mv clasic.ini UserCustom.ini')