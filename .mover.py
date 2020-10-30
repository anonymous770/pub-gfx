import os
import subprocess as sub
con = ('/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android')
os.system(f'cd Graphics/files && cp -r UserCustom.ini {con}')
os.system('cd Graphics/files && rm -rf UserCustom.ini && cd ../backup && cp -r clasic.ini ../files')