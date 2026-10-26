# trustabl/trustabl-aws

⭐ 47 · Shell · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/trustabl/trustabl-aws) · 组织维护

**AWS CI/CD 中检测 AI agent 可靠性问题的扫描门禁**

面向 AWS CodePipeline（CodeBuild action）与 Amazon CodeCatalyst（Workflow action）的 agent 可靠性扫描集成：单个 shell 扫描脚本下载并运行上游 trustabl 发布二进制（sha256 校验），扫描基于 Claude Agent SDK、OpenAI Agents SDK、Google ADK、LangChain、LangGraph、CrewAI、AutoGen、AG2、Pydantic AI、Vercel AI SDK 和 MCP 构建的 agent 仓库，输出 readiness 报告、trustabl.json/SARIF 结果，并按风险分与严重度门禁构建。支持将 ASFF 结果导入 AWS Security Hub。规则默认经嵌入信任密钥环验证，未验证则拒绝运行。分发方式为 curl 脚本 vendor 到仓库；CodeCatalyst 自 2025-11-7 起对新客户关闭，集成仅为存量客户维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个扫描脚本接入 CodePipeline 与 CodeCatalyst 两种 CI 集成
- 输出 readiness 报告、trustabl.json、SARIF，并按风险分/严重度门禁构建
- 规则经嵌入信任密钥环验证，可设 REQUIRE_SIGNED 禁止未签名回退
- 支持将 ASFF 结果导入 AWS Security Hub

## 适用场景

- 在 AWS CodePipeline 中对 agent 仓库做发布前可靠性门禁
- 在 CI 中获取 agent 可靠性报告与 SARIF 产物
- 将扫描发现导入 AWS Security Hub 统一管理

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Catch AI-agent reliability issues before they ship, inside AWS CI/CD. Scans
> L5: LangChain, LangGraph, CrewAI, AutoGen, AG2, Pydantic AI, Vercel AI SDK, and MCP.

## 星数曲线

```mermaid
xychart-beta
    title "trustabl/trustabl-aws 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-26"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-23 47 → 2026-10-26 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f62c2cd785cf` · [字段定义](../../DATASET.md)*
