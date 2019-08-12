{"filter":false,"title":"write1.py","tooltip":"/write1.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":23},"action":"insert","lines":["# The r+ file mode opens a file for reading and writing. The file is not","# truncated, but the file pointer (or cursor) is placed at the start of the","# file, so contents will begin to be overwritten.","# In our example, we overwrite the first line with 'Line 0'","# We store the current position in a variable and skip over 'Line 2' (the value","# is 8 because we have a newline character at the end of the new Line 0 and","# Line 2)","# We then use the second parameter of seek() to move the pointer to the end of","# the file. The second argument of seek() is optional. Normally, we just supply","# an offset from the start of the file, but seek() can take the following","# parameters:","# seek(offset, from_where)","# The offset, we are already familiar with. from_where is: 0 (default) offset","# from the beginning of the file; 1 offset from the current file pointer or","# 2 offset from the end of the file. So seek(0,2) moves us to the end of the file","","with open('myfile.txt', 'r+') as f:","    f.write('Line 0')","    current_position = f.tell()","    f.seek(current_position + 8)","    f.write('Line 6')","    f.seek(0, 2)","    f.write('\\nLine 5')"],"id":1}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["1"],"id":2}]]},"ace":{"folds":[],"scrolltop":39,"scrollleft":0,"selection":{"start":{"row":16,"column":18},"end":{"row":16,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1564667798909,"hash":"53ff564c1ba1eb991b271309ce26cafa94a5a8ea"}