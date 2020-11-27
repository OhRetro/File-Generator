#File Generator

import os
import os.path
import ctypes
import time

ctypes.windll.kernel32.SetConsoleTitleW('File Generator')

#-------------------------------------------------------------------------------
#File Creation------------------------------------------------------------------
print('=======================================================================')
print('What will be the file name?')
Name = input('>')
print('')
print('What will be the file format?')
Format = input('>')
print('')
print('=======================================================================')
print('Type what you want inside:')
Text = input('>')

#-------------------------------------------------------------------------------
#File Creation Dependency-------------------------------------------------------
FileOutput = 'Output/'
FileName = Name
FileFormat = Format
FileCreation = os.path.join(FileOutput, FileName + '.' + FileFormat)
File = open(FileCreation, 'w')
FileText = Text
File.write(FileText)
File.close()

#-------------------------------------------------------------------------------
#Result-------------------------------------------------------------------------
print('')
print('=======================================================================')
print('The file have been saved, see "Output" folder.')
print('Press Enter to close.')
print('')
print('=======================================================================')
input()
