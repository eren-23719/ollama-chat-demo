#这是一个聊天的工具类，用来调用ollama大模型
#1.导模块
import ollama
#2.定义函数，给大模型发送请求，并获取处理结果
def get_response(prompt):
    response = ollama.chat(model="deepseek-r1:1.5b",messages=[
        {'role':'user',
         'content':prompt
        }
    ])
    #获取模型处理的结果
    return response['message']['content']
#记忆功能(用列表提问）
def get_response_list(prompt_list):
    '''
    根据历史提示词纪录列表，选出最近的20条，作为本次请求的上下文
    :param prompt_list:提示词列表，[{'role':'user','content':...},
                                 {'role':'assistant','content':'..'}
                                 ]
    :return:大模型的回答文本
    '''
    response = ollama.chat(model="deepseek-r1:1.5b",messages=prompt_list[-20:])
    return response['message']['content']
#只自己运行才运行
if __name__ == '__main__':
    prompt_list=[{'role':'user','content':'如何学习ai'}]
    print(get_response_list(prompt_list))
