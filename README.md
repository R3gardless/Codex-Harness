# Codex harness

요구사항을 구체화하고, 작은 기능을 완성하고, 실행 근거와 함께 전달하기 위한
가벼운 프로젝트용 지침 모음입니다. 언어·프레임워크·특정 모델에 종속되지 않습니다.

## 구성

| 경로 | 역할 |
| --- | --- |
| `AGENTS.md` | 범위, 구현, 검증, 환경, Git에 관한 공통 원칙 |
| `.agents/skills/harness-discover` | 모호한 업무 요청을 요구사항과 검증 기준으로 변환 |
| `.agents/skills/harness-build` | 기존 스택에서 작은 종단 기능 구현 |
| `.agents/skills/harness-debug` | 재현 → 가설 → 수정 → 회귀 확인 |
| `.agents/skills/harness-data-check` | 데이터 계약, 기준선, 누수, 지표 검증 |
| `.agents/skills/harness-verify` | 통합 결과와 실행·전달 조건 확인 |
| `.agents/skills/harness-explain` | 실제 코드와 선택 이유를 설명 |
| `.agents/skills/harness-frontend` | 모던한 톤앤매너, UX, 접근성, 반응형 UI |
| `.agents/skills/harness-backend` | 보안, API 계약, 호환성, 확장 경계 |
| `.agents/skills/harness-test` | 단위·계약·통합 테스트와 재현 가능한 테스트 하네스 |
| `.agents/skills/harness-ideate` | 공개 API·OSS·enterprise 기능 조사와 아이디어 설계 |
| `.agents/skills/harness-design-rationale` | AI 대화에서 확정된 설계와 실제로 언급된 이유만 기록 |
| `.agents/skills/harness-context` | 필요한 문맥만 사용하고 작업 체크포인트 유지 |
| `mcp/codex.toml` | FE 문서·컴포넌트 및 AWS·Azure 선택형 연결 |
| `docs/CODEX_GUIDE.md` | Claude CLI 사용자용 Codex 안내 |
| `docs/DECISIONS.md` | 사용자 요구와 설계 결정의 근거 |
| `templates/work-notes.md` | 필요할 때만 쓰는 짧은 작업 기록 양식 |
| `scripts/install_harness.py` | 기존 프로젝트에 충돌 없이 설치 |

## 다른 프로젝트에서 사용

Python 3.9 이상이면 추가 패키지 없이 설치할 수 있습니다. 공개 저장소에서 받은
사본을 작업 프로젝트 **바깥**에 두고 설치 스크립트를 실행하세요. 다운로드는 현재
환경에서 허용된 경로만 사용합니다. 저장소 URL과 고정할 커밋은 실제 공개본을 확인합니다.

공개 원본: [R3gardless/Codex-Harness](https://github.com/R3gardless/Codex-Harness).

```sh
git clone --depth 1 https://github.com/R3gardless/Codex-Harness.git /tmp/codex-harness
```

`/tmp/codex-harness`가 이미 있으면 덮어쓰지 말고 다른 비어 있는 경로를 선택하세요.
재현성이 필요하면 검토한 커밋을 사용합니다.

```sh
python3 /path/to/Codex-harness/scripts/install_harness.py --target /path/to/project
python3 /path/to/Codex-harness/scripts/install_harness.py --target /path/to/project --apply
```

첫 명령은 변경 예정 목록만 보여 줍니다. 두 번째 명령이 설치합니다.

- `.agents/skills/`에 12개 스킬을 복사합니다.
- `AGENTS.md`가 없으면 생성합니다. 기존 파일이 있으면 원문을 보존하고 하단에
  하네스 블록을 추가합니다. 기존 프로젝트 지침이 충돌 시 우선합니다.
- 기존 스킬이나 설치 블록의 내용이 다르면 전체 적용을 시작하지 않고 중단합니다.
  변경 내용을 비교해 수동으로 합치세요. 동일한 내용의 재설치는 아무것도 바꾸지 않습니다.
- `AGENTS.override.md`가 있으면 먼저 알립니다. 이 파일은 같은 위치의 `AGENTS.md`를
  가릴 수 있으므로 적용 여부를 직접 확인해야 합니다.
- 전역 설정, 모델, MCP, 네트워크 권한, Git 사용자·서명 설정을 변경하지 않습니다.
- 템플릿, README, 개발용 스크립트와 테스트는 대상 프로젝트에 복사하지 않습니다.
  필요한 작업 양식은 이 저장소에서 확인하거나 복사하세요.

프로젝트 루트에서 새 Codex 세션을 시작하고 적용 지침을 요약하게 한 뒤, `/skills` 또는
`$harness-discover`로 발견 여부를 확인하세요. 목록에 없으면 제공된 환경의 안내를
확인하세요. 이전 세션에 자동 반영됐다고 가정하지 않습니다.

## 시작 요청 예시

> README와 기존 코드, 테스트를 읽고 목표·필수조건·제출물·불확실한 점을 정리해 줘.
> 중요한 질문만 제안하고, 확인된 범위에서 가장 작은 동작을 먼저 완성하자.
> 구조 선택은 이유와 한계를 설명하고, 실행한 검증 결과를 남겨 줘.

필요한 단계만 명시할 수도 있습니다.

```text
$harness-discover 이 요청에서 구현 전에 확인할 업무 맥락과 성공 조건을 찾아 줘.
$harness-build 확정한 핵심 흐름 하나를 기존 스택에서 끝까지 연결해 줘.
$harness-debug 이 오류를 재현하고 원인을 확인한 뒤 최소 수정으로 고쳐 줘.
$harness-data-check 이 데이터 처리의 기준선과 누수 가능성을 점검해 줘.
$harness-verify 필수조건별 구현 위치와 실제 검증 결과를 대조해 줘.
$harness-explain 실제 코드 흐름과 구조 선택 이유, 실패 조건을 설명해 줘.
```

## 작업 방식

모든 스킬을 한꺼번에 읽거나 매번 문서를 생성할 필요는 없습니다. 요구사항이 이미
명확하면 바로 구현하고, 데이터 처리가 없다면 데이터 스킬을 생략합니다. 제한 시간이
있으면 핵심 흐름을 먼저 실행하고 마무리 검증·설명에 시간을 남깁니다.

자동 브라우저 조작이나 외부 API 연결 없이 터미널 중심으로 사용할 수 있습니다.
화면은 허용된 미리보기에서 사용자가 직접 확인하며, 확인하지 않은 부분은 미검증으로
남깁니다. 호스트 환경의 도구·자료·전송 제한은 이 지침보다 우선합니다.

MCP는 [설정 안내](docs/MCP.md)를 보고 필요한 서버만 선택하세요. 모두 비활성 상태로
제공하며 전역 설정이나 클라우드 계정에 자동 연결하지 않습니다. 주요 Codex 기능은
[빠른 안내](docs/CODEX_GUIDE.md), 이 구성의 설계 이유는
[결정 기록](docs/DECISIONS.md)에 있습니다.
최상위 모델 없이 진행할 때의 선택 기준·요청 형식·단계별 완료 기준은
[모델 운영 전략](docs/MODEL_STRATEGY.md)을 참고하세요.
단일·서브 에이전트의 토큰 비용과 위임 기준은
[토큰·에이전트 운영](docs/TOKEN_AND_AGENTS.md), Base UI·HeroUI 선택과 톤앤매너는
[UI 방향](docs/UI_DIRECTION.md)에 정리했습니다.

Git 커밋이 허용된 작업에서는 기존 사용자 작성자와 서명 설정을 사용합니다.
AI 공동 작성자 표기는 자동 추가하지 않습니다. 실제 AI 사용과 검증 기록은 사실대로
작성합니다. Git의 작성자 정보와 GPG/SSH 암호학적 서명은 서로 다른 설정입니다.

## 이 저장소 검증

```sh
python3 scripts/check_harness.py
python3 -m unittest discover -s tests -v
```

스킬 형식·참조와 설치 도구의 보존·충돌·재설치 동작을 검사합니다. 이 검사는 모델의
행동 품질이나 특정 호스트에서의 실제 스킬 로딩을 보증하지 않습니다.

## 형식 참고

- [OpenAI: 프로젝트 AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI: 로컬 스킬 구조와 검색 경로](https://learn.chatgpt.com/docs/build-skills)

지침과 스크립트는 이 저장소용으로 작성했습니다. 외부 스킬 팩이나 서비스 코드를
복제하지 않았습니다. MIT License.
