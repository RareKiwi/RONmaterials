# Ready or Not Editor Material Proxies
![](/readme_imageheader.jpg)  
Ready or Not placeholder material interfaces generated with [EUW_MaterialTools](https://github.com/RareKiwi/RON_material_tools)
> Terminology: Material Interface is the base class of Materials and Instances  


## Super basic install:  
0. Import the textures using [EUW_MaterialTools](https://github.com/RareKiwi/RON_material_tools) or some other method that retains the texture settings from the game.  
1. Download this repo as a .zip   
> Code - Download Zip  
2. Copy the contents of `Content` to your projects `...\ReadyOrNotYOURPROJECT\Content\`  
> For example you'd end up with `...\ReadyOrNotYOURPROJECT\Content\36_Decals_Crack_se0pahg_2K_inst2.uasset` etc  
  
## Or to sync between a git and your project:  
0. Import the textures using [EUW_MaterialTools](https://github.com/RareKiwi/RON_material_tools) or some other method that retains the texture settings from the game.  
0. Ensure [Python 3.2+](https://www.python.org/downloads/windows/) is installed and can be run from the PATH  
1. Clone this repo or your fork to disk  
> Using Github Desktop for example.  
2. Open `sync_files.py` with a text editor and change `destination_project_content` to your project content folder path, with the correct forward slashes `/`  
> Save `sync_files.py`  
3. Run `sync_files.bat` to create hardlinks.  
> Hardlinks use no extra space until git or UE4 changes the file
  
Use `sync_files.bat` whenever you update the files with git or UE4 and want to push to the other.


### Other files:  
`BPW_MaterialsListAndLink.uasset` is used to create a full list of material interfaces included with this git.  
You don't need it if your just copying the materials into your project.  
`MaterialInterfaces.txt` is created in `...\ReadyOrNotYOURPROJECT\Saved\` folder.  
A pre-made copy is included if you want to use the sync python script  