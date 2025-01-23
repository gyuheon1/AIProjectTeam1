
#파일에서 정보 읽어오기
def read_info():
    f = open("tfapi.txt", 'r')
    texts = f.readlines()
    api = texts[0].strip()
    project_id = texts[1].strip()
    model_version=texts[2].strip()
    return api, project_id, model_version

# 모델 연결
def connect_model():
    from roboflow import Roboflow
    api, project_id, model_version = read_info()
    rf = Roboflow(api_key=api)
    project = rf.workspace().project(project_id)
    model = project.version(model_version).model
    return model



