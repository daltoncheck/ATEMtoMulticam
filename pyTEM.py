#!usr/bin/env python

import sys
import os
import pprint
sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/")


import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
currentProj = projectManager.GetCurrentProject()
mediaPool = currentProj.GetMediaPool()
currentTL = currentProj.GetCurrentTimeline()
## pprint.pp(dir(resolve))

## pprint.pp(mediaPool.GetRootFolder().GetClipList()[2].GetClipProperty())

## pprint.pp(currentTL.GetItemListInTrack('video', 2)[0].GetProperty())
## I can't change Multicam angle from this object

multicamClip = mediaPool.GetRootFolder().GetClipList()[2]
subfolders = mediaPool.GetRootFolder().GetSubFolderList()
mediaPlayerFolder = subfolders[1].GetSubFolderList()[4]
mediaPlayerClip = mediaPlayerFolder.GetClipList()[1]

print(currentTL.GetItemListInTrack('video', 1)[0].GetStart())
print(currentTL.GetItemListInTrack('video', 1)[0].GetEnd())

clipInfo = {
    "mediaPoolItem" : multicamClip,
    "startFrame" : 100,
    "endFrame" : 300
}

mediaPool.CreateTimelineFromClips('targetTimeline', [clipInfo, {"mediaPoolItem": mediaPlayerClip, "startFrame": 200, "endFrame": 400}])
mediaPool.AppendToTimeline([{"mediaPoolItem": multicamClip, "startFrame": 400, "endFrame": 600}, {"mediaPoolItem": multicamClip, "startFrame": 800, "endFrame": 1000}])