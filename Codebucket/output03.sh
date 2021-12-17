#!/bin/bash
increase=0
decrease=0

while IFS= read -r line;
do
    if [ -z ${previous3+x} ]
    then
        echo "setting"
    else
        prevav=$(($previous3+$previous2+$previous1))
        nowav=$(($previous2+$previous1+$line))
        if [[ $prevav -ge $nowav ]]
        then
            decrease=$(($decrease + 1))
        else
            increase=$(($increase + 1))
        fi
        echo "$prevav $nowav"
        echo  "increase is $increase"
        echo  "decrease is $decrease"
    fi

    if [ ! -z ${previous2+x} ]
    then
        previous3=$previous2
    else
        echo "skip 3 setting"
    fi

    if [ ! -z ${previous1+x} ]
    then
        previous2=$previous1
    fi
    previous1=$line
done < input01.txt
#done < inputex.txt

echo  "increase is $increase"
echo  "decrease is $decrease"
