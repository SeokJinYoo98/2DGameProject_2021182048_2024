import json

def load_components_from_json(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    entities = {}

    for entity_name, components in data.items():
        entity_components = {}

        for component_key, value in components.items():
            # "Movement_Component.speed" -> "Movement_Component"과 "speed"로 나눔
            comp_class_name, attr_name = component_key.split('.')

            # 컴포넌트 클래스 동적 가져오기
            comp_class = globals().get(comp_class_name)
            if not comp_class:
                continue  # 클래스가 정의되지 않았다면 무시

            # 컴포넌트 인스턴스 생성
            if comp_class_name not in entity_components:
                component_instance = comp_class()
                entity_components[comp_class_name] = component_instance

            # 속성 값 설정
            setattr(entity_components[comp_class_name], attr_name, value)

        entities[entity_name] = entity_components

    return entities

# JSON 파일에서 컴포넌트를 읽고 객체를 초기화하는 예제
entities = load_components_from_json('player_data.json')
for entity_name, components in entities.items():
    print(f"Entity: {entity_name}")
    for comp_name, comp_instance in components.items():
        print(f"  Component: {comp_name}, Attributes: {comp_instance.__dict__}")