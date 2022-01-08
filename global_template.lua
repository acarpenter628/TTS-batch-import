-- Assign Hotkeys
NUMPAD_TILE_KEY = 4
NUMPAD_FIGURE_KEY = 6

imageList = 
{
    -- Copy values here
}

imageNames = 
{
    -- Copy values here
}

spawnParams = { } -- type is set below, everything else can be default
customParams = { } -- image is set below, everything else can be default


function onScriptingButtonUp(index, color)
    
    if index == NUMPAD_TILE_KEY then  -- Import images as tiles
        for i, fileName in ipairs(imageList) do
            spawnParams.type = "Custom_Token"
            customParams.image = imageList[i]
            local spawnObj = spawnObject(spawnParams) -- Spawn custom tile
            spawnObj.setCustomObject(customParams) -- Import image
            spawnObj.setName(imageNames[i])  -- Set Name
        end
    elseif index == NUMPAD_FIGURE_KEY then  -- Import images as figures
        for i, fileName in ipairs(imageList) do
            spawnParams.type = "Figurine_Custom"
            customParams.image = imageList[i]
            local spawnObj = spawnObject(spawnParams) -- Spawn custom figure
            spawnObj.setCustomObject(customParams) -- Import image
            spawnObj.setName(imageNames[i]) -- Set Name
        end    end
end
