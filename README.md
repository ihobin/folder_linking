## 关于
这个一个非常简单的工具，主要是为了实现UNITY多开，在不需要复制一份完整的代码的情况下。
其实原理非常简单，就是用 WINDOWS 的`mklink /j`把一个文件夹下的所有内容建立链接到另一个文件夹。

## 如何使用
如果安装了 python2 可以直接运行`folder_linking_gui.cmd`；
 如果没安装也没事，你可以选择运行`folder_linking_gui.exe`程序。
运行后就看到操作界面了，“Source Folder”选择原UNITY工程目录，“New Folder”选择新工程目录，然后点“MAKE LINK”就完成了。
在复制的过程中，可能会弹出很多黑乎乎的窗口，别请不要方，那不是你电脑中毒了，那是脚本中调用了系统的命令导致的。我也不知道怎么解决，知道的大佬请教教我~

folder_linking_gui.exe 是用 pyinstaller 进行打包生成的：
```bash
pyinstaller -w -F folder_linking_gui.py
```

对于程序猿同学，可以用 python2 直接运行`folder_linking.py`脚本：
```bash
cd 新工程目录
python2 脚本目录/folder_linking.py 原UNITY工程目录
```