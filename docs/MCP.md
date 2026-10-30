# 선택형 MCP 설정

`mcp/codex.toml`에 실행 가능한 형식의 설정을 준비했습니다. 모두 `enabled = false`이며
인증·연결·패키지 실행은 수행하지 않습니다. 기능이 필요한 서버만 하나씩 활성화하세요.
패키지는 레지스트리에서 확인한 버전으로 고정했습니다. HeroUI MCP 1.1.3,
Azure MCP 3.0.0, AWS 프록시 1.7.0을 사용합니다. Azure의 `latest` 태그가 베타를
가리켜 안정 버전을 선택했습니다. 버전 확인은 실제 연결·인증 검증을 뜻하지 않습니다.

| 서버 | 용도 | 인증 / 조건 |
| --- | --- | --- |
| Context7 | 프런트엔드·백엔드 라이브러리 문서 검색 | 서비스의 현재 익명 한도·인증 정책 적용 |
| HeroUI React | v3 컴포넌트·테마·스타일 문서 | Node 22.22+, npx; 공개 문서 MCP |
| OpenAI Docs | Codex와 OpenAI 공개 문서 | 문서 전용 |
| AWS Knowledge | AWS 서비스·설계·API 공개 문서 | 계정 리소스 접근과 별도 |
| Microsoft Learn | Azure·Microsoft 공개 문서 | 인증 불필요 |
| AWS Resources | 허용된 AWS 계정 조회 | Python 3.10–3.14, uvx, `harness-readonly` 프로필, IAM 권한 |
| Azure Resources | 허용된 Azure 리소스 그룹 조회 | Node 22+, npx, 제공된 인증, 구독·역할 확인 |

## 적용

1. 호스트에서 MCP와 해당 네트워크·작업이 허용되는지 확인합니다.
2. `mcp/codex.toml`의 필요한 테이블을 지원되는 설정 위치에 병합합니다. 일반 Codex의
   프로젝트 설정은 `.codex/config.toml`입니다. 관리형 환경에서는 제공된 MCP 설정
   화면과 형식이 우선합니다. 기존 설정을 통째로 덮어쓰지 마세요.
3. 해당 서버만 `enabled = true`로 바꿉니다. JSON을 요구하는 화면이라면
   `python3 scripts/export_mcp.py --server aws_knowledge`로 **선택한 서버 한 개만**
   내보낼 수 있습니다. Python 3.11 이상이 필요하며 `mcpServers` 형식의 예시입니다.
   화면의 스키마가 다르면 문서를 확인해 맞추세요. Codex 전용 timeout/도구 필터는
   이 JSON에 포함되지 않으며, 가져오면 서버가 활성화될 수 있습니다.
4. 새 세션에서 `/mcp`로 도구 목록을 확인하고 공개 문서 질문 하나로 점검합니다.
   일반 로컬 CLI의 등록 상태는 `codex mcp list`로 확인합니다.

일반 로컬 환경에서 문서 서버 하나를 등록하는 예:

```sh
codex mcp add aws_knowledge --url https://knowledge-mcp.global.api.aws
codex mcp add microsoft_learn --url https://learn.microsoft.com/api/mcp
```

이 CLI 명령은 설정을 실제 변경합니다. 관리형 환경의 기존 연결을 중복 등록하지 말고
지원되는 설정 경로를 사용하세요. 하네스 설치 도구는 MCP 설정을 자동 적용하지 않습니다.

## 프런트엔드 선택

Context7은 모르는 버전별 API를 확인할 때, HeroUI MCP는 호환 스택에서 v3 컴포넌트와 테마를
찾을 때 사용합니다. 디자인 방향은 `harness-frontend`가 담당합니다. 실제 컴포넌트를
추가하기 전에 변경 파일·추가 의존성을 확인하고 기존 스타일과 맞춥니다.
브랜드를 직접 설계하려면 Base UI와 자체 토큰을 우선 검토합니다. 구체적인 선택은
[UI 방향](UI_DIRECTION.md)에 있습니다. HeroUI Pro는 별도 유료 제품이므로 공개 MCP와 혼동하지 않습니다.

Vercel의 [web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines)와
[React best practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)는
선별 참고할 공개 스킬입니다. 이 저장소에는 외부 팩 전체를 복제하지 않고 로컬 FE 스킬을
제공합니다. 배포 스킬까지 일괄 설치할 필요는 없습니다.

## AWS / Azure 리소스 연결

AWS는 공식 관리형 AWS MCP와 SigV4 프록시를 사용합니다. `harness-readonly`는 직접
준비해야 하는 프로필 이름이며 실제 계정 이름이 아닙니다. 서버 호출 권한과 조회 대상의
최소 IAM 권한이 모두 필요합니다. `--read-only`는 도구의 읽기 전용 표시를 기준으로
필터링하므로 IAM을 대신하지 않습니다. 도구가 필터링되어 보이지 않으면 문서 연결로
돌아가 원인을 확인하고, 해결하려고 읽기 제한을 해제하지 않습니다. AWS MCP와 Knowledge를
모두 켜면 문서 도구가 겹칠 수 있어 목적에 맞는 하나를 선택하세요.

Azure는 `--read-only --mode namespace --namespace group`으로 시작합니다. 사용할
계정·tenant·subscription과 권한 범위를 먼저 확인합니다. 다른 서비스가 필요할 때만
공식 목록의 namespace를 추가하고, 비밀 조회가 가능한 `keyvault` 같은 영역은 기본
범위에 넣지 않습니다. 읽기 전용은 정보 공개나 비용이 전혀 없다는 의미가 아닙니다.

개인 클라우드 인증을 허용하지 않는 환경에서는 두 리소스 서버를 비활성 상태로
유지하고 공개 문서 서버만 검토하세요. 리소스 생성, 배포, IAM 변경은 이 설정의 범위가
아닙니다. 문서 검색에도 비공개 코드·업무 내용·식별자를 보내지 않습니다.

## 공식 출처

2026-10-31 문서 확인. 연결 테스트는 별도입니다.

- [Codex MCP 설정](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Context7 설치·도구](https://github.com/upstash/context7)
- [HeroUI React MCP](https://heroui.com/en/docs/react/getting-started/mcp-server)
- [OpenAI Docs MCP](https://developers.openai.com/resources/docs-mcp)
- [AWS Knowledge](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)
- [관리형 AWS MCP 설치](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html)
- [AWS 프록시 옵션](https://github.com/aws/mcp-proxy-for-aws)
- [Microsoft Learn MCP](https://learn.microsoft.com/en-us/training/support/mcp)
- [Azure MCP 서버 옵션](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/tools/)
- [Azure MCP 공식 저장소](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server)
