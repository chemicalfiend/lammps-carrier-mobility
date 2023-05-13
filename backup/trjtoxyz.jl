function convert()
    f = open("last.xyz", "r")
    f2 = open("bbl.xyz", "w")
    
    lines = readlines(f)

    write(f2, lines[1])
    write(f2, "\n")
    write(f2, lines[2])
    write(f2, "\n")
    for i in 3:326
        tokens = split(lines[i])
        
        id = " "

        if tokens[1] == "5" || tokens[1] == "1" || tokens[1] == "9" || tokens[1] == "8"

            id = "C"

        elseif tokens[1] == "36" || tokens[1] == "43" || tokens[1] == "44" || tokens[1] == "38"

            id = "N"

        elseif tokens[1] == "49"
            id = "O"

        elseif tokens[1] == "24" || tokens[1] == "26"
            id = "H"

        else 
            id = "NaN"
        end
        
        x = tokens[2]
        y = tokens[3]
        z = tokens[4]

        write(f2, "$id $x $y $z \n")

    end
end

convert()





