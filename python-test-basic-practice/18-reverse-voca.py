# 태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다. 하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해 보고 싶습니다.
# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요. reverse_dict는 파라미터로 사전 dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.

def reverse_dict(dict):
    new_dict = {}
    
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}


# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

reverse_vocab = reverse_dict(vocab)

print("한-영 단어장\n{}\n".format(reverse_vocab))