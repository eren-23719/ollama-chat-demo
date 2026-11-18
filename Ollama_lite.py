import streamlit as st
import chat_utils
#页面配置
st.set_page_config(
    page_title='Streamlit 聊天机器人教学版本',
    page_icon='☀',
    layout='wide'
)
#页面标题(标题，三级标题，分隔栏)
st.title('☀Streamlit 聊天机器人演示')
st.markdown('### 核心功能:各类用户输入控件+标准聊天界面')
st.divider()

#聊天窗口
st.header('☁ AI 聊天对话窗口')
# 如果输入框，text_input, number_input,chat_input里面的内容有变化，则代码从上到下重新执行
#导致变量被清空，不能用普通变量存储消息记录
#可以使用session_state 记录消息，不会随着每次页面更新导致代码失效
if 'messages' not in st.session_state:
    welcome_msg={'role':"assistant",'content':"你好,我是eren的助手，有什么可以帮您的吗？"}
    st.session_state['messages'] = [welcome_msg]

for msg in st.session_state['messages']:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])
user_input = st.chat_input('请在这里输入您想问的问题...')
#使用st中提供的消息缓存机制session_state 存储记录
if user_input:
    st.session_state['messages'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    #ai 回复
    response = chat_utils.get_response_list(st.session_state['messages'])
    with st.chat_message('assistant'):
        st.markdown(response)
    st.session_state['messages'].append({'role': 'assistant', 'content': response})
