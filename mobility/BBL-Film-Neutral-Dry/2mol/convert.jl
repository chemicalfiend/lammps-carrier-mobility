function convert()
    
    f = open("alt.xyz", "r")
    f2 = open("data.xyz", "w")

    lines = readlines(f)
    
    numAtoms = parse(Int64, lines[1])
    popfirst!(lines)
    popfirst!(lines)
    
    write(f2, "$numAtoms \n\n")
    for line in lines
        tokens = split(line)
        id = parse(Int64, tokens[1])
        x = parse(Float64, tokens[2])
        y = parse(Float64, tokens[3])
        z = parse(Float64, tokens[4])
        
        sym = ""
        if(id == 1|| id == 5 || id == 8 || id == 9)
            sym = "C"
        end

        if(id == 24|| id == 26)
            sym = "H"
        end

        if(id == 36|| id == 38 || id == 43 || id == 44)
            sym = "N"
        end

        if(id == 49)
            sym = "O"
        end

        write(f2, "$sym $x $y $z \n")
    end

end


convert()
