# 2DGameProgramming - ZomBoogie
- 2021182048 게임공학과 유석진
- 2024.10.04 ~ 2024.12.~
- 언어: Python
- 엔진/라이브러리: Pygame
- IDE: VSCode
- 운영체제: Windows
- 버전 관리: Git / Source Tree

# ZomBoogie 
![Title](https://github.com/user-attachments/assets/fce170cd-ead1-45c2-a79a-91e9081a3bc0)

## [컨셉 소개]
- 참고 게임: Vampire Survivors
- 장르: 탑다운 슈팅 로그라이트
- 목표: 끝없이 몰려오는 좀비를 피하고, 쓰러뜨리며 최대한 오래 살아남는다.
- 성장 요소: 좀비를 처치해 자원을 얻고, 캐릭터를 점점 더 강하게 성장시킨다.
- 특징: 빠르고 간단한 조작으로 누구나 쉽게 즐길 수 있는 캐주얼한 게임플레이.

## [핵심 메카닉]
### 캐릭터 컨트롤 - 100%
- wasd: 8방향 이동 지원.
- 좌클릭: 마우스 위치로 사격.
- 회전: 마우스 방향으로 회전.
### 좀비 - 100%
- 기본 타입: 플레이어에 다가가며 공격을 한다.
- 원거리 타입: 기본적으로 플레이어와 거리를 유지하며, 원거리 공격을 한다.
- 탱커 타입: 총알을 세 번 맞으면 죽는다.
### 아이템 - 100%
- 경험치: 좀비를 처치하면 경험치 구슬 드랍.
- 백신: 좀비를 처치하면 낮은 확률로 백신 드랍.
### 레벨업 시스템 - 100%
- 능력치 선택: 레벨업 시 랜덤한 3개의 능력치 중 1개를 선택하여 강화.
   1. 신의 축복   - Hp 회복
   2. 신의 은총   - 최대 Hp 증가
   3. 스팀팩      - 공격속도 증가
   4. 아드레날린  - 이동속도 증가.
   5. 무기 개조   - 멀티샷(세로)
   6. 총열 개조   - 멀티샷(가로)
   7. 탄환 개조   - 탄환의 관통 횟수 증가.
   8. 조준경 개조 - 사거리 증가.
### 랜덤 타일 생성 시스템 - 100%
- infiniteScrollBackground를 상속 받은 RandomTileBackground 구현.
### UI 시스템 - 25%
   1. Aim 클래스 구현
   2. Hp UI 구현
   3. Xp UI 구현
   4. Time UI 구현
- Aim 클래스를 제외한 모든 UI 미구현
### 게임 기능 - 90%
- 감염 디버프:
    - Hp의 개념.
    - 플레이어는 피격 시 감염 디버프 추가.
    - 감염 디버프 중첩 횟수가 특정 횟수 이상이면 게임 오버.
- 백신: 백신을 통해 감염 디버프를 0으로 초기화.
- 일정 게임 레벨(20)을 버티면 게임 클리어
### ToDo:
   - 사운드 및 이펙트 추가
   - 메인 게임 UI 및 종료 로직 구현
   - 로딩, 메뉴, 종료 씬 구현
   
## [Commit Insights]
![Commit](https://github.com/user-attachments/assets/73ea86ab-6c93-46b3-b25d-d9ff3d87f399)
![CommitGraph](https://github.com/user-attachments/assets/a856b9d3-db1a-42c7-a7b3-89dce3f95e96)

## [수정]
1. 좀비 행동 관리 방식 변경
   - 변경 전: 좀비는 행동 트리를 가지고 각자 행동을 결정
   - 변경 후: ZombieManager에서 모든 좀비의 상태를 update()메서드를 통해 행동을 결정
   - 변경 이유: 
      - 좀비의 행동이 복잡하지 않음.
      - 중앙에서 좀비들을 관리하는 방식이 더 효율적이라 판단.
2. 좀비들의 공격 컨셉 추가
   - 원거리형 좀비: 플레이어와 일정 거리를 유지하는 기능 추가.
   - 탱커형 좀비: 달리기 기능 추가.
3. 레벨업 씬 제거
   - 변경 전: 레벨업 씬이 Push되었을때 배경이 사라지는 문제 발생.
   - 변경 후: 메인 씬에서 레벨을 관리하는 방향으로 수정.
      - Pause, Resume 메서드의 기능 확대.
   - 변경 이유:
      - 배경을 사라지지 않게 씬을 푸쉬하는 해결방법 찾지 못함.
4. 밸런스 관련 문제 보류
   - StageLevel: 좀비 생성 관련 레벨을 밸런스적인 문제로 적용을 보류.
5. 각종 스킬 이름 변경
   - 변경사항: 게임 컨셉에 맞게 능력치 이름 변경, 수치 구체화

## [문제점 및 어려운점]
1. 게임의 코드가 오직 Zomboogie를 위한 코드로 제작되고 있음.
2. 레벨업 씬을 분리하지 못한 점
   - LevelScene으로 전환되는 경우 MainScene의 배경이 없어지는 문제 발생
   - LevelScene에서도 MainScene의 화면 정보를 담고싶지만, 해결 방향을 찾지 못했음.
   - MainScene에서 Pause, Resume 메서드를 수정해 LevelUp을 관리하게 되었음.
3. 플레이어와 좀비의 상태 관리가 일관되지 않음.

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
- 진행도: 100%
### Zombie
- Class: Zombie
- Is a: Sprite class
- Inheritance:
   1. ZombieD
      - Hp: 1, Speed: 100
      - Special_Function: None
      - ![ZombieD](https://github.com/user-attachments/assets/cb0fd9c0-e683-4e14-8fad-e2e7d2a47021)
   2. ZombieR
      - gif
      - Hp: 1, Speed: 80
      - Special_Function: 일정 거리 유지 및 원거리 공격
      - ![ZombieR](https://github.com/user-attachments/assets/29c40d2b-46bc-4387-aaf7-ee518b2e9d02)
   3. ZombieT
      - gif
      - Hp: 3, Speed: 110
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
- 진행도: 100%
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
- Class: Aim
- Is a: Sprite Class
- 역할: 마우스의 위치 좌표를 저장
- 핵심 메서드: X
- 상호작용:
   - PlayerController

## [게임 흐름]
1. 사방에서 몰려오는 좀비로부터 생존한다.
2. 플레이어는 직접 사격하여 좀비를 물리친다.
3. 플레이어는 좀비와 충돌시 감염 디버프가 증가한다. (Hp 개념)
4. 감염 디버프가 특정 횟수 이상이 되면 게임 오버가 된다.
5. 남은 시간이 0이되면 게임을 승리한다.
    - 스테이지 레벨은 20레벨로 구성되었으며, 30초마다 레벨이 증가한다.

### 게임 화면
![메인 씬](https://github.com/user-attachments/assets/b731f682-0586-45d1-8182-2ace79fb81dd)
### 레벨업
![Zombogie레벨업](https://github.com/user-attachments/assets/d14f12c0-18a4-4833-a170-a6181321e693)

## [개발 요소]
### 레벨업
- 경험치 요구량:
   - 레벨에 비례해 10씩 선형적으로 증가한다.
   - 예시)
      - 레벨1: 필요 경험치 10
      - 레벨2: 필요 경험치 20

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
- 경험치 코인: 99%
   - 좀비를 처치하면 100% 확률로 경험치 구슬을 드랍한다.
   - 이를 획득하면 경험치가 증가한다.
- 백신: 1%
   - 좀비를 처치하면 1% 확률로 드랍한다.
   - 감염 디버프를 초기화하는 아이템이다.

### 적
- 타입: 기본, 원거리, 탱커
- ZombieManager를 통해 좀비의 상태를 설정한다.
- 원거리, 탱커 좀비는 Special_Function을 소유한다.

## [사용한/사용할 개발 기법]
### OOP
- 클래스와 객체를 활용해 코드의 재사용성과 유지보수성을 높히는 기법.
### Event Driven Programming
- 사용자의 입력이나 게임 내 이벤트에 반응해 로직을 실행하는 기법.
### State Machines
- 게임 상태나 오브젝트의 상태를 상태 기계로 관리하는 기법.

## [게임 프레임워크]
### gfw
- 각 씬을 스택 구조로 관리하여 게임의 흐름을 제어.
### world
- 각 씬별 필요한 오브젝트들을 업데이트, 드로우, 이벤트처리.
### image 
- 게임에서 사용하는 이미지를 딕셔너리에 캐시 및 관리.
### scoreSprite
- 기타 정보를 화면에 시각적으로 렌더링.
### guage
- 로딩 정보나 상태를 시각적으로 표시하는 게이지를 렌더링.
### infiniteScrollBackground
- 무한이 이어지는 배경을 구현
### RandomTileBackground
- 랜덤한 타일을 생성하여 동적으로 변하는 맵을 구성.

## [일정]
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


## [성과]
### 10/28일 이전
- 게임 리소스 수집 완료
  - 출처: https://goldmetal.co.kr/
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
2. Item Class의 구체적인 구현 누락. -> 해결
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

- ToDo
   - UI 구현

### 5주차
### 6주차
### 7주차


## [Youtube]
- 1차 발표: https://youtu.be/JN8lkWoDTZI
- 2차 발표: https://youtu.be/XQFYz2O36p8
