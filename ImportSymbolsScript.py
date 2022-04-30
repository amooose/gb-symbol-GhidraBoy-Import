#  IP: GHIDRA
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#       http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from ghidra.program.model.symbol.SourceType import *
import string
import re
functionManager = currentProgram.getFunctionManager()

f = askFile("Open symbol file", "Load GBA .sym")

for line in file(f.absolutePath):  # note, cannot use open(), since that is in GhidraScript
    find_sym = re.compile(r"[A-Za-z0-9]{2}\:[A-Za-z0-9]{4}\s[^;\s]+").match(line)
    if(find_sym):
        line = find_sym.group(0)
        pieces = line.split()
        (segm,offset) = pieces[0].split(":")
        if(segm != "00"):
            segm = "rom"+str(int("0x"+segm,0))+":"+offset
            address = toAddr(segm)
        else:
            address = toAddr(long(segm + offset, 16))

        print "Created symbol:", pieces[1], "at:", address
        createLabel(address, pieces[1], False)
