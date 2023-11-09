import pickle

# 'state_rwd_action.pkl' 파일의 경로를 정확하게 지정해야 합니다.
file_path = r'C:\Users\User\Documents\GitHub\SC2RL\base=state_rwd_action.pkl'
  # 예시 경로

# 파일을 읽고 내용을 출력합니다.
try:
    with open(file_path, 'rb') as file:
        content = pickle.load(file)
        print(content)
        print(content['action'])
except Exception as e:
    print(f"파일을 읽는 중 에러가 발생했습니다: {e}")
