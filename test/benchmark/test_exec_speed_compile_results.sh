#!/bin/bash

arrVar=()

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

    count=`cat ${foldername}/time_test_results.csv | wc -l`

    echo $count

    if [[ $count -lt 3 ]]; then
      echo "Not enough results for a comparison."
      continue
    fi

    tail -n +2 ${foldername}/time_test_results.csv >> final_time_test_results.csv

done

