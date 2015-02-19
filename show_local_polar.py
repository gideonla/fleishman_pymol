#!/usr/bin/python

#This script focuses on a certain residues and shows polar contacts around 
def show_local():
	#spli selection into two objects	
	cmd.hide("sticks")
	objects=cmd.get_object_list("sele")
	util.cba(33,objects[0],_self=cmd)
	cmd.select("sele_around","%s and (br. sele around 4 or sele)"%(objects[0]),enable=1)
	cmd.show("sticks"    ,"sele_around")
	cmd.dist("sele_polar_conts","sele_around","sele_around",quiet=1,mode=2,label=0,reset=1);cmd.enable("sele_polar_conts")
	cmd.orient("sele_around",animate=-1)
	myspace = {'names': []}
	util.cba(13,"sele",_self=cmd)
#	cmd.scene('message', 'store', "rms value is: "+str(rms))
#	cmd.scene("message","recall")
	return  
cmd.set_key( 'CTRL-E' ,show_local)


