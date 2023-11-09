import pickle

# 'state_rwd_action.pkl' 파일의 경로를 정확하게 지정해야 합니다.
file_path = r'C:\Users\User\Documents\GitHub\SC2RL\state_rwd_action.pkl'  # 수정된 경로

# 파일을 읽고 내용을 출력합니다.
try:
    with open(file_path, 'rb') as file:
        content = pickle.load(file)
        # 파일에서 로드된 객체의 타입, 클래스, 길이(가능한 경우) 및 속성을 출력합니다.
        print(f"Type: {type(content)}")
        if hasattr(content, '__dict__'):
            print(f"Class: {content.__class__}")
            print(f"Attributes: {content.__dict__.keys()}")
        elif isinstance(content, dict):
            print(f"Keys: {content.keys()}")
        else:
            print(f"Length: {len(content)}" if hasattr(content, '__len__') else "No length")
        
        # 'action' 키의 값을 출력합니다.
        if 'action' in content:
            print(f"Action value: {content['action']}")
        else:
            print("There is no 'action' key in the content.")
except Exception as e:
    print(f"파일을 읽는 중 에러가 발생했습니다: {e}")
