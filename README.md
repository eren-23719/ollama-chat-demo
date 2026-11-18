# 本地 Ollama 聊天助手

使用 Python、Streamlit 和 Ollama 完成的课程练习。界面使用 `st.session_state` 保存当前会话消息，每次请求向 DeepSeek-R1 1.5B 传入最近二十条消息。

## 运行

安装 Python 和 [Ollama](https://ollama.com/)，并确保 Ollama 服务已启动。Windows 上可先打开 Ollama 应用。打开仓库目录后执行：

```powershell
python -m pip install -r requirements.txt
ollama pull deepseek-r1:1.5b
python -m streamlit run Ollama_lite.py
```

打开 Streamlit 输出的本地地址，在输入框里提问。首次推理可能需要等待模型加载。

## 代码结构

- `Ollama_lite.py` 渲染聊天界面并管理会话历史。
- `chat_utils.py` 调用 Ollama 并读取回复，通过切片提取最近二十条消息。

聊天记录保存在当前浏览器会话，项目不写入聊天记录文件。

## 学习来源

参考恋恋风辰zack课程第 19 至 22 集，包括 Ollama 模型接入与 Streamlit 聊天界面。
