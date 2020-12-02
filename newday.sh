#! /bin/bash

year=2020
day=1

while [[ -d "$(($year+1))" ]] ; do
    year=$(($year+1))
done

if [[ ! -d "./${year}" ]]
then
    mkdir "${year}/"
fi

while [[ -d "${year}/day${day}" ]] ; do
    if [[ $day -lt 25 ]]
    then
        day=$(($day+1))
    else
        year=$(($year+1))
        day=1
        mkdir "${year}/"
    fi
done

mkdir "${year}/day${day}/"
mkdir "${year}/day${day}/input"
mkdir "${year}/day${day}/src"