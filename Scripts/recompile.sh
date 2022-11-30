#!/bin/bash
#  touch /tmp/time.file
#  
#  while test 1; do
#  	if test /tmp/time.file -ot $1 ;
#  	then
#  		$2
#  		#echo in
#  		touch /tmp/time.file
#  	fi
#  	#echo out
#  	sleep 1
#  done

echo "NOT WORKING" 


# This works 
# touch /tmp/marked.time; while test 1; do if test /tmp/marked.time -ot ~/Documents/local-lybrary/certifications/RHCSA/rhcsa8.md ; then echo change detected; marked -i ~/Documents/local-lybrary/certifications/RHCSA/rhcsa8.md -o ~/Downloads/rhcsa8.html; touch /tmp/marked.time; fi; sleep 2; done
