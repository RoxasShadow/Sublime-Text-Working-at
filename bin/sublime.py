import subprocess as sub
import os

__module_name__ = "Sublime Text - Working at" 
__module_version__ = "0.1"
__module_description__ = "Say in chan at what you're working for"

import xchat as XC

def sublime(word, word_eol, userdata):
	p = sub.Popen(os.getcwd() + '\\plugins\\sublime.exe', stdout=sub.PIPE, stderr=sub.PIPE)
	output, errors = p.communicate()
	XC.command('me ' + 'working at ' + output.split("- Sublime Text")[0].split("\\")[-1])
	
XC.hook_command("sublime", sublime, help="/sublime Say in chan at what you're working for")

XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')