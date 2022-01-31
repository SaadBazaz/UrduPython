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

    # Check if a folder with the same name of the file exists
    if [ ! -d "./${foldername}" ]; then
        echo "Subdirectory does not exist. Have you run the similarity test?"
        continue
    fi

    # Run hyperfine over both UrduPython and Python and save to a csv
    hyperfine  --export-csv ${foldername}/time_test_results.csv "urdupython ${foldername}/${filename}.ur.py" "python ${fullfilename}"   

done
