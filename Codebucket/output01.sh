#!/bin/bash
increase=0
decrease=0

while IFS= read -r line;
do
    if [ -z ${previous+x} ]
    then
        echo "setting"
    else
        if [[ $previous -le $line ]]
        then
            increase=$(($increase + 1))
        else
            decrease=$(($decrease + 1))
        fi
    fi

    previous=$line
done < input01.txt

echo  "increase is $increase"
echo  "decrease is $decrease"
