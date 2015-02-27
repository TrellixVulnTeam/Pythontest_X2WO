#!/usr/bin/env Python

def speed(dis, time):
	'''dis denotes distance, the unity is kilometer;
	unity of time minute;
	compute the average time per mile and average speed in miles per hour'''
	dis_mile = dis / 1.61 # convert the distance from kilometer to mile
	ever_time = (time/60)/dis_mile
	print('the average time per mile is ', round(aver_time, 6))
	speed = dis_mile/(time/60)
	print('the average speed in miles per hour is', round(speed, 6))

	
