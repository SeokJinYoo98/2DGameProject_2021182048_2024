# 2DGameProgramming - ZomBoogie
- 2021182048 게임공학과 유석진
- 2024.10.04 - 2024.12.
- 언어: Python
- 엔진/라이브러리: Pygame
- IDE: VSCode
- 운영체제: Windows
- 버전 관리: Git / Source Tree

# ZomBoogie 
![Title](https://github.com/user-attachments/assets/fce170cd-ead1-45c2-a79a-91e9081a3bc0)

# 1.게임에 대한 간단한 소개 [수정 필요]
### [컨셉 소개]
- 참고 게임: Vampire Survivors
- 차이점: 플레이어가 직접 사격하여 적을 처치한다는 점
- 장르: 탑다운 슈팅 로그라이트
- 목표: 끝없이 몰려오는 좀비를 피하고, 쓰러뜨리며 최대한 오래 살아남는다.
- 성장 요소: 좀비를 처치해 자원을 얻고, 캐릭터를 점점 더 강하게 성장시킨다.
- 특징: 빠르고 간단한 조작으로 누구나 쉽게 즐길 수 있는 캐주얼한 게임플레이.

## [게임 흐름]
1. 사방에서 몰려오는 좀비로부터 생존한다.
2. 플레이어는 직접 사격하여 좀비를 물리친다.
3. 플레이어는 좀비와 충돌시 Hp가 감소한다.
4. Hp가 0이하가 되면 게임 오버가 된다.
5. 남은 시간이 0이되면 게임을 승리한다.

# 2. 개발 계획/일정/실제 진행 [수정 필요]
### [개발 계획]
2.1 [랜덤 타일 생성 시스템]
- infiniteScrollBackground를 상속 받은 RandomTileBackground 구현.
- ![bg](https://github.com/user-attachments/assets/0ba7b9e9-5e56-4bc8-9464-dec7f6dc2d1e)

2.2 [캐릭터 컨트롤]
- wasd: 8방향 이동 지원.
- 좌클릭: 마우스 위치로 사격.
- 회전: 마우스 방향으로 회전.
- ![Player](https://github.com/user-attachments/assets/46b7b2e0-555e-4904-9677-f9beb20fcb81)

2.3 [좀비]
- 기본 타입: 플레이어에 다가가며 공격을 한다.
- ![ZombieD](https://github.com/user-attachments/assets/cb0fd9c0-e683-4e14-8fad-e2e7d2a47021)
- 원거리 타입: 
   - 플레이어와 거리를 유지한다. 
   - 원거리 공격을 한다.
- ![ZombieR](https://github.com/user-attachments/assets/29c40d2b-46bc-4387-aaf7-ee518b2e9d02)
- 탱커 타입: 
   - 총알을 세 번 맞으면 죽는다.
   - 달리기 기능이 있다.
- ![ZombieT](https://github.com/user-attachments/assets/05d8c70b-b145-42c8-9350-a68a6299bae8)
- 랜덤한 위치에서 스테이지 레벨에 맞게 소환된다.

2.4 [아이템]
- 코인: 좀비를 처치하면 경험치 구슬 드랍.
- ![Coin](https://github.com/user-attachments/assets/4a62f2e2-7701-4ffd-af8d-2ce7e2dc20dc)
- 백신: 좀비를 처치하면 낮은 확률로 백신 드랍.
- ![Vaccine](https://github.com/user-attachments/assets/7e2a9efb-ae82-441e-90c3-9eb54f9959a8)
- 자석: 플레이어의 아이템 획득 범위가 3초동안 제한이 없어진다.
- ![Magnetic](https://github.com/user-attachments/assets/30bae69c-012f-4f66-86d4-49b895bf4506)

2.5 [레벨업 시스템]
- 능력치 선택: 레벨업 시 랜덤한 3개의 능력치 중 1개를 선택하여 강화.
   1. 신의 축복   - Hp 회복
   2. 신의 은총   - 최대 Hp 증가
   3. 스팀팩      - 공격속도 증가
   4. 아드레날린  - 이동속도 증가.
   5. 무기 개조   - 멀티샷(세로)
   6. 총열 개조   - 멀티샷(가로)
   7. 탄환 개조   - 탄환의 관통 횟수 증가.
   8. 조준경 개조 - 사거리 증가.
- ![BulletLevelUp](https://github.com/user-attachments/assets/48ac14c0-d603-4aa0-83e7-1a853973043c)

2.6 [스테이지 레벨]
- 10 레벨로 구성
- 각 레벨은 1.0초 ~ 0.1초의 생성 시간을 가짐
   - 스테이지 1: 1.0초 간격으로 기본 좀비만 생성
   - 스테이지 2 ~ 7: 레벨 모든 좀비 랜덤하게 1마리 생성
   - 스테이지 8: 기본 좀비와 원거리 또는 탱커 좀비 2마리 생성
   - 스테이지 9: 모든 좀비 3마리 생성

2.7 [UI 시스템]
   1. Aim UI 구현
   2. Hp UI 구현
   3. Xp UI 구현
   4. Time UI 구현
   5. Magnetic UI 구현

2.8 [게임 기능]
- Hp: 플레이어의 Hp가 0이 되면 게임 오버
- 백신: 백신을 통해 감염 디버프를 0으로 초기화.
- 약 10분의 시간을 버티면 게임 승리.

### [Commit Insights] - 발표전 최종 수정 필요.
![Commit](https://github.com/user-attachments/assets/73ea86ab-6c93-46b3-b25d-d9ff3d87f399)
![CommitGraph](https://github.com/user-attachments/assets/a856b9d3-db1a-42c7-a7b3-89dce3f95e96)

### [수정]
1. 좀비 행동 관리 방식 변경
   - 변경 전: 좀비는 행동 트리를 가지고 각자 행동을 결정
   - 변경 후: ZombieManager에서 모든 좀비의 상태를 update()메서드를 통해 행동을 결정
   - 변경 이유: 
      - 좀비의 행동이 복잡하지 않음.
      - 중앙에서 좀비들을 관리하는 방식이 더 효율적이라 판단.
2. 레벨업 씬 제거
   - 변경 전: 레벨업 씬이 Push되었을때 배경이 사라지는 문제 발생.
   - 변경 후: 메인 씬에서 레벨업을 관리하는 방향으로 수정.
      - Pause, Resume 메서드의 기능 확대.
   - 변경 이유:
      - 배경을 사라지지 않게 씬을 푸쉬하는 해결 방법을 찾지 못함.
3. Magnetic 추가
   - 변경 이유:
      - 쌓여있는 아이템을 제거하기 위한 수단이 필요함.
4. HP UI 수정
   - 변경 전: 물병 모양의 Hp UI
   - 변경 후: progress 이미지
   - 변경 이유:
      - 유동적으로 Hp바를 생성 및 관리 하기가 생각보다 까다롭다고 판단.
      - 직관적으로 Hp를 보기 어렵다고 판단.
      - 만약 Hp가 100 이상이 되어버린다면 화면을 전부 가려버릴 수 있다고 판단.
      - 이러한 이유로 Hp를 progress 이미지 형태로 관리하기로 결정.
5. 감염 디버프 컨셉
   - 변경 전: 플레이어가 좀비와 충돌시 감염 디버프가 증가하는 개념
   - 변경 후: 기존 Hp 시스템을 도입
   - 변경 이유:
      - 직관적으로 플레이어의 Hp를 알아보는데 어려움이 있다 판단.
      - 기존의 Hp 시스템으로 변경해 플레이어의 현재 상태를 직관적으로 알아볼 수 있게 변경.
6. 플레이 시간 단축
   - 변경 전: 약 30분의 플레이 시간
   - 변경 후: 약 10분의 플레이 시간
   - 변경 이유:
      - 개발을 하며 테스트를 진행한 결과 30분은 너무 게임이 루즈해진다 판단.
   
# 3. 다음 사항을 구체적으로 나열한다. [수정 필요]
### [사용된 기술]
1. OOP
- 클래스와 객체를 활용해 코드의 재사용성과 유지보수성을 높히는 기법.
2. Event Driven Programming
- 사용자의 입력이나 게임 내 이벤트에 반응해 로직을 실행하는 기법.
3. State Machines
- 게임 또는 오브젝트를 상태로 관리하는 기법.
4. Mediator Pattern
- 게임 오브젝트끼리의 직접적인 소통을 피하고 Mediator(중재자-Manager)를 통해 소통하는 기법.

### [참고]
1. SDL_GetKeyboardState를 교수님에게 힌트를 얻고 StackOverflow 참고.

### [수업내용에서 차용한 것]
1. UI 및 버튼.
2. 딕셔너리 해싱.
3. 게임 오브젝트의 움직임.
4. 충돌 처리.
5. 공통 변수 분리.
6. InfinityBackground Scroll.
7. button class
8. 이외에도 대부분의 기능 및 함수들이 수업내용을 차용해 작성되었다 생각.

### [직접 작성한 것]
1. RandomTileBackground
   - 일정량 스크롤되면 새로운 타일들을 생성하고 딕셔너리 요소들을 밀고 당기는 기능.
2. LevelUp
   - 플레이어의 스킬 작성.
3. Special_Function
   - 각 오브젝트가 가진 고유 기능 작성.
   - Special_Range를 통해 유효 사거리 계산.
4. Mediator(Manager)
   - 오브젝트들이 중재자를 통해 소통하도록 작성.

# 4. 개선 및 보완 사항 [완성]
### [Git 부분]
1. 커밋 관리 개선:
   - 세분화된 커밋 대신, 기능 단위로 묶어서 커밋하여 관리.
2. README 수정 관리:
   - GitHub에서 직접 수정하지 않고, 로컬에서 업데이트 후 커밋하여 불필요한 커밋을 방지.
3. .gitignore 파일 점검:
   - 오타와 같은 사소한 문제를 예방하기 위해 파일을 꼼꼼히 점검.

### [코드 부분]
1. 코드 스타일 및 함수명 통일:
   - 변수명과 함수명을 일관되게 정리해, 코드 가독성과 유지보수성 향상.
2. 근본적 문제 해결:
   - 시간 부족으로 우회했던 문제를 분석하고 근본적인 원인을 해결.
3. 하드코딩 개선:
   - 데이터를 외부 파일로 분리해 관리 용이성 확보.
   - 분리된 외부 파일로 수정 및 밸런싱 작업을 간편화.

### [게임 매커니즘 부분]
1. 좀비의 다양화:
   - 스킬 기반 좀비(폭발형, 진화형 등)를 추가하여 전략적 플레이 요소를 강화.
2. 레벨업 선택지 다양화:
   - 능력치 강화 외에도 즉시 발동형(폭발, 무적 등)을 추가.
   - 특수 탄환 효과(폭발, 스플래쉬 등)를 추가.
3. 능력치의 다양화:
   - 공격 속성, 방어력, 방어구 관통력 등을 추가해 성장 경로 확장.
   - 플레이어가 다양한 전략적 선택을 할 수 있도록 설계.
4. 게임 난이도 조정:
   - 난이도가 증가할수록 좀비의 속도와 Hp, 방어력이 변화하도록 설계.
5. 스테이지별 보스 추가:
   - 각 스테이지 마지막에 보스를 추가해 긴장감과 보상을 제공.
6. 다양한 캐릭터 및 무기 추가:
   - 새로운 캐릭터와 무기를 통해 플레이어의 선택지를 확대.
   - 캐릭터별 고유 능력과 무기의 특수 효과를 추가하여 플레이 스타일의 다양화.

### [구현 부분]
1. LevelUpScene 분리:
   - 레벨업 씬과 메인 씬의 로직 분리를 통해 관리 용이성을 증대.
   - Commit 'pause_scene 추가' 부분을 참고해 분리 진행.
2. 사격 이펙트 추가:
   - 공격 시 시각적 효과를 추가하여 타격감을 향상.
3. 게임 매니저 추가:
   - 중앙 관리 시스템을 통해 게임 상태를 효율적으로 관리
   - 씬 종료 및 전환 로직을 통일.
4. 상태 관리 통일:
   - 좀비 플레이어, 아이템의 상태를 일관되게 관리하는 로직 설계.
   - 구현 예상:
      - StateManager 설계해 공통된 상태는 중앙에서 관리. (걷기, 공격, 죽음 등)
      - 세부 동작 상태는 각자의 상태 관리 로직으로 처리. (공격: 사격, 공격: 달리기 등)
5. 밸런스 조정:
   - 플레이 테스트를 통해 적절한 난이도와 진행 시간을 조정.
6. 엔딩씬 개선:
   - 레벨 정보와 좀비 처치 수 등의 정보를 엔딩씬에서 표시.
7. 중재자의 역할 명확화:
   - 각 중재자의 역할을 하나의 기능만 처리하도록 조정.
8. 옵션 메뉴 추가:
   - 사운드 조절, 화면 해상도 설정 등 옵션 메뉴 구현.

### [해결하지 못한 문제]
1. 레벨업 씬 분리.
2. 좀비 생성 제한.
   - 좀비의 생성 가능 숫자를 제한하지 않고 싶었지만, 프레임 드랍 문제로 제한을 걸게 되었음.

### [어려웠던 점]
1. 씬이 전환될 때 입력의 동기화.
2. 밸런스 조절.
3. 프로젝트의 규모 설정.
4. 충돌 처리의 최적화.

# 5. 수업에 대한 내용 [수정 필요]
### [기대한 점]
1. 게임 개발 전반에 대한 이해.
2. 2D 오브젝트의 애니메이션 구현에 대한 이해.

### [얻은 것]
1. 게임 개발 전반에 대한 이해.
2. GFW의 개념 및 분리.
3. git 활용 방법.
4. 컴그 텀 프로젝트에도 GFW의 개념을 적용해본 점.
5. 항상 최적화를 생각하며 개발을 해야한다는 점.

### [변화할 점]
1. 프로젝트의 규모에 대해서 피드백이 있으면 좋겠음.
   - 개발을 진행하다보면 예상보다 큰 프로젝트 규모에 게임을 축소 하는 경우가 발생.
   - 게임이 축소되었을때 이유가 합당하지 않으면 감점되기 때문에 프로젝트 규모에 피드백이 있다면 좋겠음.

## [메인 씬 - 게임 오브젝트]
### bg
![bg](https://github.com/user-attachments/assets/0ba7b9e9-5e56-4bc8-9464-dec7f6dc2d1e)
- Class: RandomTileBackground
- Is a: InfiniteScrollBackground class
- 역할: 랜덤 타일 생성 및 무한 스크롤 배경
- 핵심 메서드:
   1. Get_Random_Tile(): 랜덤한 타일 생성 및 리턴
   2. Generate_Visible_Tiles(): 랜덤한 타일을 조합해 배경 구현
   3. Check_Update_BG(): 스크롤 양 계산, 필요 시 Shift()호출
   4. Shift(): 타일의 이동 및 새로운 타일 생성
### Player 
![Player](https://github.com/user-attachments/assets/46b7b2e0-555e-4904-9677-f9beb20fcb81)
- Class: Actor
- Is a: Sprite class
- Has a:
   1. Gun Class
      - 특징: Actor의 회전 및 좌표를 상속
      - 생김새: 샷건
- 역할: 플레이어 캐릭터 조작 및 아이템 수집, 공격 수행
- 핵심 메서드:
   1. coolTime(): 공격 쿨타임 계산
   2. anim(): 애니메이션 프레임 전환
   3. rotate(): Aim을 향해 회전 Filp
   4. fire(): 레벨에 맞는 개수의 Bullet을 생성
   5. check_state(): 상태에 따라 애니메이션 변경
- 상호작용: 
   - PlayerController
   - LevelUpManager
   - CollisionManager
   - RandomTileBG
### Zombie
- Class: Zombie
- Is a: Sprite class
- Inheritance:
   1. ZombieD
      - Hp: 1, Speed: 150
      - Special_Function: None
      - ![ZombieD](https://github.com/user-attachments/assets/cb0fd9c0-e683-4e14-8fad-e2e7d2a47021)
   2. ZombieR
      - Hp: 1, Speed: 100
      - Special_Function: 일정 거리 유지 및 원거리 공격
      - ![ZombieR](https://github.com/user-attachments/assets/29c40d2b-46bc-4387-aaf7-ee518b2e9d02)
   3. ZombieT
      - Hp: 3, Speed: 110, mag: 2
      - Special_Function: 달리기
      - ![ZombieT](https://github.com/user-attachments/assets/05d8c70b-b145-42c8-9350-a68a6299bae8)
- 역할: 플레이어와 전투
- 핵심 메서드:
   1. to_Target(): 플레이어에게 접근
   2. anim(): 애니메이션 계산
   3. change_anim_info(): 상태 변경 시 프레임 갱신
   4. special_function(): 각 좀비의 특별 기능
- 상호작용:
   - ZombieManager
   - ItemManager
   - CollisionManager
### Item
- Class: Item
- Is a: Sprite class
- Inheritance:
   1. Coin
      - Special_Function(): Player의 Xp를 1증가
      - ![Coin](https://github.com/user-attachments/assets/4a62f2e2-7701-4ffd-af8d-2ce7e2dc20dc)
   2. Vaccine
      - Special_Function(): Player의 Hp를 1회복
      - ![Vaccine](https://github.com/user-attachments/assets/7e2a9efb-ae82-441e-90c3-9eb54f9959a8)
   3. Magnetic
      - Special_Function(): Player의 아이템 획득 범위 3초간 증가.
      - ![Magnetic](https://github.com/user-attachments/assets/30bae69c-012f-4f66-86d4-49b895bf4506)
- 역할: 플레이어에게 이로운 효과 제공
- 핵심 메서드:
   1. set_target(): Target을 설정
   2. to_Target(): Target에게 이동 
   3. special_function(): 특별한 기능 발동(Player.Xp+, Player.Hp+)
- 상호작용:
   - CollisionManager
### Bullet & ZBullet
![Bullet](https://github.com/user-attachments/assets/d4989d81-325a-4dcd-96e8-f2d01a34f0e1)
- class Bullet
- Is a: Sprite Class
- 역할: Player, ZombieR의 공격 수행
- 핵심 메서드:
   - __init__(): 총알의 방향, 관통, 속도 등 초기 정보 설정
   - update(): 정해진 방향으로 이동하는 역할
- 상호작용:
   1. CollisionManager
### Cards
![BulletLevelUp](https://github.com/user-attachments/assets/48ac14c0-d603-4aa0-83e7-1a853973043c)
- class: Card
- Is a: Sprite Class
- Inheritance: 
   - 레벨업을 위한 8가지 카드 class
- 역할: Player의 능력치 증가
- 핵심 메서드:
   - is_mouse_in_card(): 마우스 위치 판단, 이미지 프레임 변경
   - levelUp(): Card의 자식 클래스에 맞는 플레이어의 능력치 상승 기능을 수행
- 상호작용:
   1. LevelUpManager: Player의 능력치 상승
### UI
- Class: Aim UI
- Is a: Sprite Class
- 역할: 마우스의 위치 좌표를 저장
- Class: Hp UI
- Has a: Gauge Class
- 역할: 플레이어의 Hp를 시각적으로 표현
- Class: Xp UI
- Has a: Gauge Class
- 역할: 플레이어의 Xp를 시각적으로 표현
- Class: Time UI
- Has a: Font Class
- 역할: 게임의 남은 시간을 시각적으로 표현
- Class: MagneticUI
- Has a: Gauge Class
- 역할: 마그네틱 효과의 남은 시간을 시각적으로 표현
- Class: Info UI
- Has a: Font class
- 역할: 스테이지 레벨을 시각적으로 표현


## [로딩 씬 - 게임 오브젝트]
![LoadingScene](https://github.com/user-attachments/assets/ca71c2f1-e395-489c-8597-9f4dda8b4f08)
### bg
- sprite class
- 한국공학대 로고
### Gauge
- Gauge class
- 파일 로딩 정보

## [메뉴 씬 - 게임 오브젝트]
![MenuScene](https://github.com/user-attachments/assets/03d33656-6bed-4721-b5b7-1bc78b4a9754)
### bg
- HorzFillBackground
- Zomboogie Title 이미지
### cards
- b class
- 플레이어의 마우스 이벤트를 처리

## [엔딩 씬 - 게임 오브젝트]
![EndingScene](https://github.com/user-attachments/assets/3314e9f4-03e7-4413-ad44-c8a547222232)
### bg
- HorzFillBackground
- Zomboogie Title 이미지
### cards
- b class
- 플레이어의 마우스 이벤트를 처리

## [정량적 개발 요소]
### 레벨업
- 경험치 요구량: 5, 레벨업시 요구량 1씩 증가.
- 레벨업:
   - 게임이 정지되고, 3장의 카드를 제시한다.

### 능력
- 능력: 레벨 제한 없음
   1. 신의 축복: 최대 Hp +1
   2. 신의 은총: Hp 모두 회복
   3. 스팀팩: 사격 속도 0.008 감소
   4. 아드레날린: 이동속도 10 증가
   5. 무기 개조: 점사 형식으로 발사되는 탄환 증가.
   6. 총열 개조: 부채꼴 모양으로 퍼지는 탄환 증가.
   7. 탄환 개조: 탄환의 관통 횟수 증가.
   8. 조준경 개조: 총알의 사거리 증가.

### 맵
- 크기: 제한 없음
   - 맵은 무한히 확장되며, 플레이어의 이동에 따라 새로운 타일이 생성된다.
   - 타일 제너레이터를 통해 랜덤한 맵이 동적으로 구성된다.
   - 타일 하나의 사이즈는 19x19 픽셀

### 아이템
- 경험치 코인: 94%
   - 플레이어의 Xp가 +1 증가한다.
- 백신: 5%
   - 플레이어의 Hp가 +1 증가한다.
- 자석: 1%
   - 플레이어의 아이템 획득 범위가 증가한다.

### 적
- 타입: 기본, 원거리, 탱커
- ZombieManager를 통해 좀비의 상태를 설정한다.
- 원거리, 탱커 좀비는 Special_Function을 소유한다.

# [일정]
### 10/28일 이전 준비
- 리소스 수집
- 기본 프레임 워크 구상
- 맵 및 UI 구상

### 1주차: 
1. RandomTileBackground 구현
2. 캐릭터 컨트롤러 구현
### 2주차: 
2. 좀비 및 아이템 구현
3. 충돌 처리 구현
### 3주차: 
1. 좀비 SpecialFucntion 구현
2. 플레이어 능력치 구현, 레벨업 구현
### 4주차: 
1. 플레이어 레벨업 구현
2. UI 구현
### 5주차: 
1. 로딩 씬 구현
2. 메인 메뉴 씬 구현
### 6주차: 
1. 사운드 구현
2. 게임 종료 로직 구현
3. 부족한 기능 구현
### 7주차:
1. 밸런스 조절 및 최종 점검
2. 릴리즈


# [성과]
### 10/28일 이전
- 게임 리소스 수집 완료
  - 출처: https://goldmetal.co.kr/
  - 기타: 유니티 스토어
  - Aim: 자체 제작
  - 카드: 리소스 조합
  - 프로그레스 바: 김기용 교수님
- 기본 프레임 워크 구상 완료
- 맵 및 UI 구상 완료

### 1주차
1. 캐릭터 애니메이션 추가
2. 플레이어 컨트롤러 추가: 이동 및 회전
3. Gun class, Aim class, Bullet class 추가: 
- Aim - 마우스 포인터 위치 조준점 위치
- Gun: 불릿이 생성되는 위치 마우스 포인터를 바라본다.
- Bullet: 좌클릭시 Aim의 방향으로 발사된다.
4. RandomTileBackground 추가
- 무제한으로 스크롤 되며, 랜덤한 타일이 추가되는 클래스

### 2주차
1. 기본적인 좀비 class 및 하위 zombie 클래스 생성
2. CollisionManager 생성 및 콜리전 발생시 이벤트 처리
3. ZombieManager를 통한 좀비 State 관리
4. 생각보다 좀비의 행동이 한정되어, 행동 트리는 사용하지 않는 방향으로 수정

문제점:
1. 클래스에서 함수명에 _를 붙이면 private처럼 접근하지 한다고 착각
   - _가 붙은 함수명을 __으로 변경해야함.
2. Item Class의 구체적인 구현 누락.
   - 생각보다 바쁜 일정으로 Item Class의 구현 누락.
   - 빠른 시일내에 구현 해야함.

### 3주차
1. Item class 구현
2. Item의 magnetic 효과 구현
3. Zombie들의 Special Function 구현
4. Coin, Vaccine의 Special Function 구현
5. Player의 능력치 세분화 완료

### 4주차
1. SkillCardHp 추가 완료
2. SkillCardMaxHp 추가 완료
3. SkillCardSpeed 추가 완료
4. SkillCardBaseBullet2 추가 완료
5. SkillCardBullet1 추가 완료
6. SkillCardRange 추가 완료
7. SkillCardAttackSpeed 추가 완료
8. SKillCardGun 추가 완료
9. LevelUpManager 추가 완료
10. Loading, Ending, Menu Scene 구현 완료

### 5주차
1. Sound 추가 완료
2. 씬 전환시 키보드 문제 해결
3. Hp UI 추가
4. Xp UI 추가
5. Time UI 추가

### 6주차
1. 패키징 및 테스트 진행
2. 버그 패치
3. Magnetic 구현
4. MagneticUI 구현

### 7주차


# [Youtube]
- 1차 발표: https://youtu.be/JN8lkWoDTZI
- 2차 발표: https://youtu.be/XQFYz2O36p8
