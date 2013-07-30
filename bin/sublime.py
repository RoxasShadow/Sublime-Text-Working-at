import subprocess as sub
import os

__module_name__ = "Sublime Text - Working at" 
__module_version__ = "0.1"
__module_description__ = "Say in chan at what you're working for"

import xchat as XC

def sublime(word, word_eol, userdata):
  p = sub.Popen(os.getenv('APPDATA') + "\\HexChat\\addons\\sublime.exe", stdout=sub.PIPE, stderr=sub.PIPE)
  output, errors = p.communicate()
  if output == "Error":
    XC.command("me " + "isn't working.")
  else:
   XC.command("me " + "is working at " + output.split("- Sublime Text")[0].split("\\")[-1].strip() + ".")

XC.hook_command("sublime", sublime, help="/sublime Say in chan at what you're working for")

XC.prnt(__module_name__ + " version " + __module_version__ + " loaded.")
