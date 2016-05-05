python os.path模块常用方法详解
1.os.path.abspath(path) 
返回path规范化的绝对路径。 
 
>>> os.path.abspath('test.csv') 
'C:\\Python25\\test.csv' 
 
>>> os.path.abspath('c:\\test.csv') 
'c:\\test.csv' 
 
>>> os.path.abspath('../csv\\test.csv') 
'C:\\csv\\test.csv' 
 
2.os.path.split(path) 
将path分割成目录和文件名二元组返回。 
 
>>> os.path.split('c:\\csv\\test.csv') 
('c:\\csv', 'test.csv') 
>>> os.path.split('c:\\csv\\') 
('c:\\csv', '') 
 
3.os.path.dirname(path) 
返回path的目录。其实就是os.path.split(path)的第一个元素。 
 
>>> os.path.dirname('c:\\csv\test.csv') 
'c:\\' 
>>> os.path.dirname('c:\\csv') 
'c:\\' 
 
4.os.path.basename(path) 
返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。 
 
>>> os.path.basename('c:\\test.csv') 
'test.csv' 
>>> os.path.basename('c:\\csv') 
'csv' （这里csv被当作文件名处理了） 
>>> os.path.basename('c:\\csv\\') 
'' 
 
5.os.path.commonprefix(list) 
返回list中，所有path共有的最长的路径。 
 
如： 
>>> os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff']) 
'/home/td' 
 
6.os.path.exists(path) 
如果path存在，返回True；如果path不存在，返回False。 
 
>>> os.path.exists('c:\\') 
True 
>>> os.path.exists('c:\\csv\\test.csv') 
False 
 
7.os.path.isabs(path) 
如果path是绝对路径，返回True。 
 
8.os.path.isfile(path) 
如果path是一个存在的文件，返回True。否则返回False。 
 
>>> os.path.isfile('c:\\boot.ini') 
True 
>>> os.path.isfile('c:\\csv\\test.csv') 
False 
>>> os.path.isfile('c:\\csv\\') 
False 
 
9.os.path.isdir(path) 
如果path是一个存在的目录，则返回True。否则返回False。 
 
>>> os.path.isdir('c:\\') 
True 
>>> os.path.isdir('c:\\csv\\') 
False 
>>> os.path.isdir('c:\\windows\\test.csv') 
False 
 
10.os.path.join(path1[, path2[, ...]]) 
将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。 
 
>>> os.path.join('c:\\', 'csv', 'test.csv') 
'c:\\csv\\test.csv' 
>>> os.path.join('windows\temp', 'c:\\', 'csv', 'test.csv') 
'c:\\csv\\test.csv' 
>>> os.path.join('/home/aa','/home/aa/bb','/home/aa/bb/c') 
'/home/aa/bb/c' 
 
11.os.path.normcase(path) 
在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。 
 
>>> os.path.normcase('c:/windows\\system32\\') 
'c:\\windows\\system32\\' 
 
12.os.path.normpath(path) 
规范化路径。 
 
>>> os.path.normpath('c://windows\\System32\\../Temp/') 
'c:\\windows\\Temp' 
 
12.os.path.splitdrive(path) 
返回（drivername，fpath）元组 
 
>>> os.path.splitdrive('c:\\windows') 
('c:', '\\windows') 
 
13.os.path.splitext(path) 
分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作 
 
>>> os.path.splitext('c:\\csv\\test.csv') 
('c:\\csv\\test', '.csv') 
 
14.os.path.getsize(path) 
返回path的文件的大小（字节）。 
 
>>> os.path.getsize('c:\\boot.ini') 
299L 
 
15.os.path.getatime(path) 
返回path所指向的文件或者目录的最后存取时间。 
 
16.os.path.getmtime(path) 
返回path所指向的文件或者目录的最后修改时间 