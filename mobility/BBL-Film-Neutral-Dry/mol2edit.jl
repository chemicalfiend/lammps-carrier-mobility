# Convert mol2 atoms appropriately

function convert()
    f = open("att3.mol2", "r")
    f2 = open("data.mol2", "w")

    lines = readlines(f)

    numAtoms = parse(Int64, split(lines[3])[1])
    
    lineCount = 10

    for i in 1:9
        write(f2, lines[i])
        write(f2, "\n")
    end

    for i in 1:(numAtoms)
        tokens = split(lines[lineCount])
        id = parse(Int64, tokens[2])
        x = parse(Float64, tokens[3])
        y = parse(Float64, tokens[4])
        z = parse(Float64, tokens[5])
        mol = parse(Int64, tokens[7])
        charge = parse(Float64, tokens[8])

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
        write(f2, "\t $i \t $sym \t $x $y $z \t $sym \t $mol \t RES \n")
        
        lineCount += 1
    end

    for i in lineCount:length(lines)
        write(f2, lines[i])
        write(f2, "\n")
    end

end


convert()











