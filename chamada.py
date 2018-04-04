#################################################################################################################

from text_color import text_color
import sys

#################################################################################################################
    
print text_color.fg_Green + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent libero magna, congue et justo et, posuere ornare ligula." + text_color.text_reset
print ' '
print text_color.fg_Bright_Green + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent libero magna, congue et justo et, posuere ornare ligula." + text_color.text_reset
print ' '
print text_color.fg_Bright_Green + text_color.text_underline + "Lorem ipsum dolor sit amet, " + text_color.text_reset + text_color.fg_Bright_Red + "consectetur adipiscing elit. " + text_color.text_reset + "Praesent libero magna, congue et justo et, posuere ornare ligula." + text_color.text_reset
print ' '
print text_color.fg_Bright_Red + text_color.bg_Bright_Green + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent libero magna, congue et justo et, posuere ornare ligula." + text_color.text_reset
print ' '
print text_color.fg_Bright_Red + text_color.bg_Green + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " + text_color.text_reset + " Praesent libero magna, congue et justo et, posuere ornare ligula." 
print ' '
print '[' + text_color.fg_Bright_Red + 'WRITING  ' + text_color.text_reset + '] File on SERVER' 
print ' '
print '[' + text_color.fg_Bright_Green + 'COMPLETED' + text_color.text_reset + '] File on SERVER' 
print ' '
#################################################################################################################
