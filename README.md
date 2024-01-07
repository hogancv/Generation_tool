# 使用说明

Python>=3.6

```
pip install -r requirements.txt -i
```

先将标题和导读输入文本框，点击生成。

点击名称按钮，右边的输入框会填充 需要生成的文件夹名，默认为 9 个字符。

在 app.py 中修改。pypinyin 库只会对中文字符做首字母处理。

![image-20240107203556499](https://github.com/65548963/Generation_tool/blob/main/images/image-20240107203556499.png)

点击新建文件夹即可生成文件夹，生成路径和模板路径在 app.py 中修改。采用绝对路径

![image-20240107204131197](https://github.com/65548963/Generation_tool/blob/main/images/image-20240107204131197.png)

点击 HTML 按钮生成 title 和 meta，并复制到剪切板。粘贴到模板后使用 shift+alt+F 进行代码格式化

banner 按钮同上，替换 banner 组件值。

nav 生成需注意不要保留空格。

如需生成

> 阿里 东南亚、Shopee 东南亚、Temu 东南亚、Lazada 东南亚、亚马逊 东南亚、京东 东南亚、ebay 东南亚

应将代码粘贴至 vscode，选择东南亚以及前面的空格，Ctrl+D 多选后删除。将生成好后的 nav 粘贴至模板，先进行代码格式化，再使用 Alt+鼠标单击多选插入位置粘贴' 东南亚'。

> 电商快评（快手 快评）莫岱青（莫岱青 快手）庄帅（庄帅 快手）陈礼腾（陈礼腾 快手）

带括号格式可直接处理，多生成的空值删除

![image-20240107205559522](https://github.com/65548963/Generation_tool/blob/main/images/image-20240107205559522.png)
