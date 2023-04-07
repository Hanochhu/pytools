import openai

# # 设置代理
# proxies = {'http': "http://127.0.0.1:6926", 'https': "http://127.0.0.1:6926"}
# openai.proxy = proxies

openai.api_key = "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"


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text


# def generate_text():
#     response = openai.Image.create(
#         prompt="a white siamese cat",
#         n=1,
#         size="1024x1024"
#     )
#     image_url = response['data'][0]['url']

#     return image_url

if __name__ == "__main__":
    prompt = """10.美国黑人患高血压的比美国白人高两倍。把西方化的非洲黑人和非洲白人相比，情况也是如此。研究者们假设，西方化的黑人之所以会患高血压，是两个原因相互作用的结果：一个原因是西方食品含盐量高，另一个原因是黑人遗传基因中对于缺盐环境的适应机制。
    以下对当代西方化非洲黑人的断定，（ ）项如果是真的，最能支持研究者的假设？
    A.塞内加尔人和冈比亚人后裔的血压通常不高，塞内加尔和冈比亚历史一直不缺盐。
    B.非洲某些地区的不同寻常高盐摄入是危害居民健康的严重问题。
    C.考虑到保健，大多数非洲白人也注意控制盐的摄入量。
    D.西非约鲁巴人的血压不高，约鲁巴人有史以来一直居住在远离海盐的内陆，并远离非洲萨哈拉盐矿。"""
    print(generate_text(prompt))
