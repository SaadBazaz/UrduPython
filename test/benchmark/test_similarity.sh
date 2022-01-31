#!/bin/bash

for fullfilename in ./*.py; do

    echo $fullfilename

    filename=$(basename -- "$fullfilename")
    extension="${filename##*.}"
    filename="${filename%.*}"

    if [[ "$filename" == "__init__" ]] || [[ "$filename" == "compiled" ]] ; then
      continue
    fi

    foldername=${filename}

    # Make a folder with the same name of the file with "_test" appended
    mkdir ${foldername}

    # Generate an UrduPython version of the Python file (Eng -> Urdu)
    urdupython $fullfilename --reverse --keep-only

    # Save a copy of the compiled UrduPython file in the folder
    cp compiled.en.py ${foldername}/${filename}.ur.py   

    # Run UrduPython again on the compiled file (Urdu -> Eng)
    urdupython compiled.en.py --keep-only

    # Rename the original file temporarily
    cp $fullfilename ${fullfilename}.tmp

    # Rename the compiled file to the other filename (Will hopefully prevent filename errors)
    cp compiled.en.py ${fullfilename}

    # Run the compiled file, save output in folder
    python ${fullfilename} >> ./${foldername}/urdupython_result.txt

    # Rename the original file back to its original name (remove the .tmp file and the compiled.en.py file)
    cp ${fullfilename}.tmp $fullfilename
    rm ${fullfilename}.tmp
    rm compiled.en.py

    # Run the original file, save output in folder
    python ${fullfilename} >> ./${foldername}/original_result.txt


    file1="./${foldername}/urdupython_result.txt"
    file2="./${foldername}/original_result.txt"

    if cmp -s "$file1" "$file2"; then
        printf 'The file "%s" is the same as "%s"\n' "$file1" "$file2"
        echo "$filename,PASS" >> results.csv
    else
        printf 'The file "%s" is different from "%s"\n' "$file1" "$file2"
        echo "$filename,FAIL" >> results.csv
    fi



done
