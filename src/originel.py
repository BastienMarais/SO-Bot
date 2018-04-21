#coding: utf-8
#########################################################################################
#   Description :   Ce programme permet la traduction origine <=> normal
#   File :          originel.py
#   Usage :         python3 originel.py
#   Requirements :  python3
#   User.name :     Bastien Marais
#   User.email :    marais.bas@gmail.com                        
#########################################################################################


class Originel :
	""" cette classe permet de traduire du texte originel """
	
	def __init__(self):
		self.alphabet = { "A" : ["OhO","VHHV"],
		"B" : ["VHHHV","Voooo"],
		"C" : "VHH",
		"D" : ["Voo","VOO"],
		"E" : "VHhH",
		"F" : "VHh",
		"G" : "VHhHv",
		"H" : "VHV",
		"I" : ["v","V"],
		"J" : ["oHV","vHhV","vHV"],
		"K" : ["Voo","VOO"],
		"L" : "VH",
		"M" : "VooV",
		"N" : "VOV",
		"O" : "VHHV",
		"P" : "VHHv",
		"Q" : "VHHVo",
		"R" : "VHHvo",
		"S" : "vHHHv",
		"T" : "HV",
		"U" : "VHV",
		"V" : "OO",
		"W" : ["OOOO","OooO"],
		"X" : "OO",
		"Y" : "oO",
		"Z" : "HOH" }
		
		self.alphabet2 = { "OhO" : "A",
		"VHHV" : ["A","O"],
		"VHHHV" : "B",
		"Voooo" : "B",
		"VHH" : "C",
		"Voo" : ["D","K"],
		"VOO" : ["D","K"],
		"VHhH" : "E",
		"VHh" : "F",
		"VHhHv" : "G",
		"VHV" : ["H","U"],
		"v" : "I",
		"V" : "I",
		"oHV" : "J",
		"vHhV" : "J",
		"vHV" : "J",
		"VH" : "L",
		"VooV" : "M",
		"VOV" : "N",
		"VHHv" : "P",
		"VHHVo" : "Q",
		"VHHvo" : "R",
		"vHHHv" : "S",
		"HV" : "T",
		"OO" : ["V","X"],
		"OOOO" : "W",
		"OooO" : "W",
		"oO" : "Y",
		"HOH" : "Z" }
		
		
	def toOriginel(self,message):
	    """ traduit le message normal en message originel """
	    
	    message = message.upper()
	    new = ""
	    for mot in message.split(" ") :
	        for l in mot :
	            new += str(self.alphabet[l]) + " "
	                    
	    return new
	    
	    
	def toNormal(self,message):
	    """ traduit le message originel en message normal """
	    
	    new = ""
	    for l in message.split(" "):
	        new += str(self.alphabet2[l])
	    
	    return new
	    
