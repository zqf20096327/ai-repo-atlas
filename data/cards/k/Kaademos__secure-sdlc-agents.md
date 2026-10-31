# Kaademos/secure-sdlc-agents

⭐ 14 · JavaScript · MIT · 推送 2026-07-30 · [GitHub](https://github.com/Kaademos/secure-sdlc-agents) · [官网](https://owasp.org/www-project-application-security-verification-standard/) · 组织维护

**8 个覆盖全 SDLC 的 AI 安全 sub-agent 团队，供 Claude Code 等 IDE 使用**

面向开发团队的安全开发生命周期工具集：提供 AppSec、GRC、云平台、发布管理等 8 个专项 agent，在需求、威胁建模、代码审查、IaC 审查、合规映射到发布签-off 各阶段介入。本体不直接调用 LLM API，而是作为 MCP 服务器与提示生成引擎，向宿主 AI 工具（Claude Code、Cursor、Windsurf、Zed 等）注入安全上下文；另提供 CLI、Git hooks、GitHub Actions 门禁（Gitleaks/Checkov/CodeQL）与 8 个文档模板，支持 Next.js、FastAPI、Django 等 7 种技术栈的安全指引。安装方式含插件市场、npm 包与 git clone。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个按 SDLC 阶段分工的安全专项 agent
- MCP 服务器 + 提示生成引擎模式，不直接调用 LLM API，密钥由宿主工具管理
- GitHub Actions 门禁运行 Gitleaks/Checkov/CodeQL 等确定性检查
- 7 种技术栈（Next.js/FastAPI/Django/Express/Rails/Go/Spring Boot）框架级安全指引

## 适用场景

- 在 Claude Code 或 Cursor 中为新功能生成 ASVS 安全需求与威胁模型
- 对 PR 与 IaC（Terraform/Helm/K8s）执行安全审查
- 在发布前执行 go/no-go 安全门禁与合规映射（SOC 2/ISO 27001/GDPR/PCI DSS）

## 场景标签

`网络安全` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L191: You don't need to provide an API key to `secure-sdlc`. This project does not make LLM API calls directly. Instead,
> L37: |**MCP server**|Works in Cursor, Windsurf, Zed, Continue, and any MCP-compatible tool|

## 星数曲线

```mermaid
xychart-beta
    title "Kaademos/secure-sdlc-agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `57c8e3114273` · [字段定义](../../DATASET.md)*
