print("Hello World!")

resolve = Resolve()
projMan = resolve:GetProjectManager()
proj = projMan:GetCurrentProject()
mediaPool = proj:GetMediaPool()
currentTL = proj:GetCurrentTimeline()

print("Current Timeline Name: " .. currentTL:GetName())
trackOneItems = currentTL:GetItemListInTrack("video", 1)
print(trackOneItems[2]:GetMediaPoolItem())