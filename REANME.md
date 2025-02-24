# screenshot_in_otree
- 在otree中每5秒钟截取一次屏幕（仅是浏览器的截图），并以Base64的格式保存到数据库中
- 使用了Extramodel、live method、custom export等功能，可以保存图片并导出
- script文件夹中提供了一个将csv文件中的Base64图片数据转换为图片的脚本
- 截图功能使用了[html2canvas](https://github.com/niklasvh/html2canvas)（MIT协议）