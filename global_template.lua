imageList = 
{

}

imageNames = 
{

}

spawnParams = 
{
    type = "Custom_Token" -- or Figurine_Custom
    -- Everything else can be default
}

customParams = 
{
    -- image is set below, everything else can be default
}


function onScriptingButtonUp(index, color)
    print("Print ", index)
    
    if index == 4 then
        for i, fileName in ipairs(imageList) do
            print(fileName)
            customParams.image = imageList[i]
            local spawnObj = spawnObject(spawnParams)
            spawnObj.setCustomObject(customParams)
            spawnObj.setName(imageNames[i])
        end
    end
end


 -- https://www.reddit.com/r/tabletopsimulator/comments/a9tsbi/spawning_custom_object_problem_with_script/