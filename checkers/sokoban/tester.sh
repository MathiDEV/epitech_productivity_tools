#! /bin/sh
rm trace.txt 2> /dev/null
touch trace.txt
for test in tests/*; do
    echo "$(basename $test):" >> trace.txt
    python3 src/tester.py "$test"
    if [ $? = 1 ]
    then
        echo "  ERROR" >> trace.txt
    else
        echo "  PASSED" >> trace.txt
    fi
done