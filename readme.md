

脚本：crypt_util.py

```text
使用方法：
	1. 选择需要加密的文件夹
	2. 命令行执行 python crypt_util.py 文件夹1 文件夹2 ...
	3. 执行完毕，文件夹下原有python文件会替换为加密文件
	4. 备份在同级目录

注意：
	1. 如果存在备份文件（文件名=py文件.bak），则跳过执行
	2. 如果文件夹下存在__pycache__,则删除__pycache__
	3. 如果python文件带BOM头，加密后自动去掉BOM头
```

