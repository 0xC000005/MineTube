# MineTube🐇
Download subtitles from Youtube and organize them into articles。

從油管上下載字幕文件，並通過語義識別整理成通順的文章。

![Usage](https://raw.githubusercontent.com/0xC000005/image-hosting/master/20190827130742.PNG)

## 開發計劃

- 代理池，用於提供大陸地區訪問Youtube的API
- 語義識別，目前打算用科大訊飛的Deep Learning Model，[玻森Bosonnlp]([https://bosonnlp.com](https://bosonnlp.com/))後期可能會添加支持
- 字幕文件下載，使用get_youtube_subtitle提供的API，我用輪子我自豪，[介紹](https://github.com/qwertyuiop6/get_youtube_subtitle) 
- 自動中文翻譯，使用Googletrans庫，我用輪子我自豪 *2 [介紹](https://www.jianshu.com/p/2f9a2b4c3aa3)
- 想到了再寫😜，你們給我提需求啊？？？