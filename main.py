import urllib.request
import zipfile
import shutil
import os
import time
import glob

print("\n"*99999)
modpathFile = open("GamePath.txt", 'r');
modpath = modpathFile.read();
modpathFile.close();
print("using game path " + modpath + "\n");
print("(incorrect? edit the file 'GamePath.txt')");
print("⚠ notice: this script was designed for btd6, but might work with other games\n\n")

print("⌠ keep's melonloader toolkit v1 ⌡");
print("[0] exit\n[1] install melonloader\n[2] open mod manager");

selection = input("> ");

if(selection == "0"):
    exit();
elif(selection == "1"):
    print("\n\n⌠ starting melonloader installation ⌡\n");
    print("downloaded MelonLoader.x64.zip")
    urllib.request.urlretrieve("https://github.com/LavaGang/MelonLoader/releases/latest/download/MelonLoader.x64.zip", "MelonLoader.x64.zip");
    print("downloaded")
    print("extracting")
    with zipfile.ZipFile("MelonLoader.x64.zip","r") as zipf:
        zipf.extractall("MelonLoader_Extracted")
    print("extracted")
    print("copying melonloader to game path")
    shutil.copy("MelonLoader_Extracted/version.dll", modpath+"/version.dll")
    shutil.copytree("MelonLoader_Extracted/MelonLoader", modpath+"/MelonLoader")
    print("creating mods folder")
    os.mkdir(modpath+"/Mods");
    print("\n⌠ finished melonloader installation ⌡\n\n\n")
elif(selection == "2"):
    def modMgr():
        print("\n"*99999)
        print("\n\n⌠ keep's mod manager ⌡")
        allMods = []

        print("\t[ enabled ]")
        enabledMods = glob.glob(modpath+"/Mods/*.dll")
        for i in range(len(enabledMods)):
            t = str(enabledMods[i])[len(modpath+"/Mods/"):len(str(enabledMods[i]))];
            print("[{}] 🟢 ".format(str(len(allMods))) + t[0:len(t)-4])
            allMods.append([t, True])
            time.sleep(0.01)

        print("\t[ disabled ]")
        disabledMods = glob.glob(modpath+"/Mods/*.dll.disabled")
        for i in range(len(disabledMods)):
            t = str(disabledMods[i])[len(modpath+"/Mods/"):len(str(disabledMods[i]))];
            print("[{}] 🔴 ".format(str(len(allMods))) + t[0:len(t)-13])
            allMods.append([t, False])
            time.sleep(0.01)

        print("\t[ extras ]")
        print("[D] bulk disable\n[E] bulk enable\n[I] install shared mod\n[X] exit")

        modSelection = input("> ")
        if(modSelection.lower() == "x"):
            print("\n"*99999)
            print("⌠ goodbye ⌡")
            time.sleep(2)
            exit();
        elif(modSelection.lower() == "d"):
            print("\n⌠ bulk disable ⌡")
            print("⌠ please type all mods you would like to disable seperated by a comma ⌡")
            print("⌠ or use * to select all. ⌡")
            print("⌠ e.g: 1,3,4,5,8 ⌡")
            modsToDisable = input("> ");
            if(modsToDisable == "*") :
                modsToDisable = allMods
                print("\n\n")
                for i in range(len(modsToDisable)):
                    time.sleep(0.1)
                    selectedMod = allMods[i]
                    if(selectedMod[1]):
                        os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+selectedMod[0]+".disabled")
                        print("[ disabled {} ]".format(selectedMod[0][0:len(selectedMod[0])-4]))
                        
                    else:
                        print("[ {} is already disabled ]".format(selectedMod[0][0:len(selectedMod[0])-13]))
            else:
                modsToDisable = modsToDisable.split(",")
                print("\n\n")
                for i in range(len(modsToDisable)):
                    time.sleep(0.1)
                    selectedMod = allMods[int(modsToDisable[i])]
                    if(selectedMod[1]):
                        os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+selectedMod[0]+".disabled")
                        print("[ disabled {} ]".format(selectedMod[0][0:len(selectedMod[0])-4]))
                        
                    else:
                        print("[ {} is already disabled ]".format(selectedMod[0][0:len(selectedMod[0])-13]))
        elif(modSelection.lower() == "e"):
            print("\n⌠ bulk enable ⌡")
            print("⌠ please type all mods you would like to enable seperated by a comma ⌡")
            print("⌠ or use * to select all. ⌡")
            print("⌠ e.g: 1,3,4,5,8 ⌡")
            modsToEnable = input("> ");
            if(modsToEnable == "*") :
                modsToEnable = allMods
                print("\n\n")
                for i in range(len(modsToEnable)):
                    time.sleep(0.1)
                    selectedMod = allMods[i]
                    if(not selectedMod[1]):
                        os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+(selectedMod[0][0:len(selectedMod[0])-9]))
                        print("[ enabled {} ]".format(selectedMod[0][0:len(selectedMod[0])-13]))
                        
                    else:
                        print("[ {} is already enabled ]".format(selectedMod[0][0:len(selectedMod[0])-4]))
            else:
                modsToEnable = modsToEnable.split(",")
                print("\n\n")
                for i in range(len(modsToEnable)):
                    time.sleep(0.1)
                    selectedMod = allMods[int(modsToEnable[i])]
                    if(selectedMod[1]):
                        os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+(selectedMod[0][0:len(selectedMod[0])-9]))
                        print("[ enabled{} ]".format(selectedMod[0][0:len(selectedMod[0])-13]))
                        
                    else:
                        print("[ {} is already enabled ]".format(selectedMod[0][0:len(selectedMod[0])-4]))
        elif(modSelection.lower() == "i"):
            print("[ please enter code ]")
            code = input("> ")
        else:
            selectedMod = allMods[int(modSelection)]
            print("\n\n⌠ managing file \"" + selectedMod[0] + "\" ⌡")
            print("[0] delete\n[1] enable\n[2] disable\n[3] share")
            
            operationSelection = input("> ")
            if(operationSelection == "0"):
                os.remove(modpath+"/Mods/"+ selectedMod[0])
                print("\n\n⌠ deleted file \"" + selectedMod[0] + "\" ⌡")
            
            if(operationSelection == "1"):
                if(selectedMod[1]):
                    print("\n\n⌠ mod already enabled ⌡")
                else:
                    os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+(selectedMod[0][0:len(selectedMod[0])-9]))
                    print("\n\n⌠ enabled ⌡")
            
            if(operationSelection == "2"):
                if(selectedMod[1]):
                    os.rename(modpath+"/Mods/"+ selectedMod[0], modpath+"/Mods/"+selectedMod[0]+".disabled")
                    print("\n\n⌠ disabled ⌡")
                else:
                    print("\n\n⌠ mod already disabled ⌡")
            
            if(operationSelection == "3"):
                modToUpl = {'file'}
                print("not done")
            

        time.sleep(2)
        modMgr();
    modMgr();