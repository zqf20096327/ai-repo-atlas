# jland-93/mond

⭐ 16 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/jland-93/mond) · [官网](https://github.com/jland-93/devsecops-platform) · 个人维护

**面向企业的自服务 DevSecOps 平台：AI 分诊安全发现**

以 FastAPI + React 构建的 DevSecOps 平台，将资产清单、扫描、发现管理、策略模拟、SBOM/合规报告、IAM 权限自助与韩国/国际法规映射整合到单一流程。通过适配器接入 Trivy/Semgrep/Nuclei 等扫描器，AI provider（Anthropic/OpenAI/Azure/Bedrock/Ollama/vLLM）经统一抽象层切换，用于发现项分诊、严重度重估与修复建议；未配置 AI key 时以规则 fallback 模式运行。支持 Docker Compose 30 秒演示与 Helm/K8s 生产部署，内置 MFA、SSO、RBAC 与 MCP 服务器，UI 默认韩语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 适配器机制接入 Trivy/Semgrep/Nuclei，新扫描器一个类即可扩展
- AI provider 抽象层支持 Anthropic/OpenAI/Azure/Bedrock/Ollama/vLLM，无 key 时规则 fallback
- AI Insights 自然语言查询（RAG，四源检索 + 引用）与 PII 脱敏后外调 LLM
- MCP 服务器（stdio + HTTP/SSE）与 GitHub Actions 一行 CI 集成

## 适用场景

- 统一管理多来源安全扫描结果并由 AI 做一级分诊
- 企业内按 K-PIPA/GDPR/PCI-DSS 等法规做合规映射与 SBOM 报告
- 员工自助申请云/K8s/LDAP 权限并走策略审批流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L52: - **무엇을 푸는가** — DevSecOps 도구가 너무 흩어져 있고, 발견사항이 너무 많고, 의사결정은 너무 느립니다. Mond는 **AI가 1차 분석**해서 **사람이 결정만** 하면 되는 흐름을 만듭
> L59: In English: a vendor-neutral, self-service DevSecOps platform that consolidates asset inventory, scanning, AI-triag
> L111: **Mond** (독일어로 "달")은 어떤 클라우드든 어떤 스캐너든 상관없이 동작하는, **AI 기반 셀프서비스 DevSecOps 플랫폼**입니다. 자산 / 스캔 / 발견사항 / 정책을 단일 모델로 다루고
> L273: 키를 설정하지 않으면 **기본 규칙 fallback**으로 모든 UI가 작동합니다. 응답에는 항상 `{provider}:{model}` 라벨이 함께 기록되어 출처 추적이 가능합니다.

## 星数曲线

```mermaid
xychart-beta
    title "jland-93/mond 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bb4e2dfaafc4` · [字段定义](../../DATASET.md)*
