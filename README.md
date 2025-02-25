<div align="center">

# 해달 입부테스트 안내

</div>

2025년 상반기 해달의 입부 테스트 페이지입니다.
`

> [!IMPORTANT]
>
> fork한 후, README 페이지를 자유롭게 수정해서 사용하셔도 됩니다.
>
> 문제는 [여기서](./docs/problems.md) 확인하실 수 있습니다.

## ⚙️ 진행과정

1. 상단의 [`Fork`](https://github.com/KNU-HAEDAL/2025-SS-welcome-test/fork) 버튼을 클릭해 repository를 생성합니다.
   - Owner : 개인 계정
   - Repository name: 원하는 이름
1. **git bash**를 열어서 방금 생성한 repository를 **clone**합니다.

   ```bash
   git clone https://github.com/{{Owner}}/{{Repository name}}.git

   # 예시
   git clone https://github.com/KNU-HAEDAL/2025-SS-welcome-test.git
   ```

1. clone한 repository를 Visual Studio Code로 열어줍니다.

   ```bash
    cd {{Repository name}}

    # 예시
    cd 2025-SS-welcome-test
    code .
   ```

1. 본인이 선택한 언어 폴더([자바](./java_test/), [자바스크립트](./javaScript_test/))로 이동하여 답안지에 [문제](./docs/problems.md)들을 풉니다.
1. github repository에 작성한 코드를 업로드합니다.
   ```bash
   git add .
   git commit -m "입부테스트 문제 풀이"
   git push origin main
   ```
   - commit message는 원하는 내용으로 작성하셔도 됩니다.
1. fork 했던 원본 레포지토리로 pull request를 생성합니다. 제출 완료!

> github 사용이 어려운 분들은 [가이드](./docs/guide.md)와 함께 진행해보세요!

## [📖 문제 안내](./docs/problems.md)

`Java` 혹은 `JavaScript` 둘 중 하나를 선택해 문제를 풀면 됩니다.

**Spring** 또는 **ANS**(안드로이드 스튜디오) 수강을 원할 시 `Java`로, **React** 수강을 원할 시 `JavaScript`로 문제를 풀어야 합니다.

문제는 총 8개이며 공통문제 6개(a~f), 언어문제 2개(자바 g1&2, 자바스크립트 h1&2)로 구성되어 있습니다.

문제풀이가 완료되면 repository에 push 하신 뒤, 링크를 제출해주시면 됩니다.

오류 및 문의사항은 [오픈채팅방](https://open.kakao.com/o/sdmtYQgh)에 남겨주세요.

## 🚨 주의 사항

> [!WARNING]
>
> 1. 파일 이름을 변경하지 마세요.
> 2. `Java`의 경우, 기존에 생성된 파일 안의 `main` 함수 내용만 작성하시면 됩니다.
> 3. 결과를 출력할 때 오타 및 띄어쓰기, 들여쓰기(엔터)를 주의해주세요.
