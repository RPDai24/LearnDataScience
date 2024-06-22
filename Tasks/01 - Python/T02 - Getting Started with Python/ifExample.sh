#!/bin/bash
#This is a practical task of commands terminal

#Create if_folder if new_folder is exist.
if [ -d new_folder ]
then 
	echo "new_folder is exist"
	mkdir if_folder
else 	
	echo "new_folder isn't exist"
fi

#Create a new folder, hyperionDev, if if_folder is exist, or else make a new folder, new-projects.
if [ -d if_folder ]
then
	echo "if_folder is exist"
	mkdir hyperionDev

else	
	echo "if_folder isn't exist"
	mkdir new-projects
fi


