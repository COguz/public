#!/bin/bash

usage="usage: bash cpu_manage.sh monitor | get | getonlymode | set <mode>\
	\nmodes:\
	\n\tschedutil | default\tdefault mode
	\n\tpowersave\t\trun CPU at minimum frequency\
	\n\tperformance\t\trun CPU at maximum frequency\
	\n\tondemand\t\tdynamically scales frequency\
	\n\tconservative\t\tmore gradually than ondemand scaling\
	"

# my_bar () {} add a bar like /usr/bin/watch

my_monitor () {

	while test 1;
	do
		myresult=$(my_mode_get)
		clear
		echo -e $myresult
		sleep 2
	done

}

my_mode_set () {
	echo "Setting mode to: $1"
	echo $1 | sudo tee /sys/devices/system/cpu/cpufreq/policy*/scaling_governor
	sudo -k
}

my_mode_get () {
	my_path="/sys/devices/system/cpu/cpufreq/policy"
	my_var1="scaling_cur_freq"
	my_var2="scaling_governor"
	my_mode=""
	for i in $(seq 0 100);
	do
		my_tmp_mode="\
			cpu: "$i"\t\
			khz: "$(cat $my_path$i/$my_var1 2>/dev/null)"\t\
			mode: "$(cat $my_path$i/$my_var2 2>/dev/null)\
		       	|| break
		my_mode=$my_mode$(echo $my_tmp_mode | tr '\n' ' ')"\n"
	done
	echo $my_mode
}


case $1 in
	monitor)
		my_monitor
		exit 0
		;;
	get)
		echo -e $(my_mode_get)
		;;
	getonlymode)
		echo -e $(my_mode_get) | head -n1 | cut -d':' -f4
		;;
	set)
		case $2 in

			conservative | ondemand | userspace | powersave | performance | schedutil)
				my_mode_set $2	
				exit 0
				;;
			default)
				my_mode_set "schedutil"
				;;
			*)
				echo -e $usage
				exit 1
				;;
		esac
		;;
	*)
		echo -e $usage
		exit 1
		;;
esac



#watch cat /sys/devices/system/cpu/cpufreq/policy*/scaling_cur_freq /sys/devices/system/cpu/cpufreq/policy*/scaling_governor 
#echo powersave | sudo tee /sys/devices/system/cpu/cpufreq/policy*/scaling_governor 
sudo -k
