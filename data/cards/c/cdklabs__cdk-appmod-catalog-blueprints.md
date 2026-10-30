# cdklabs/cdk-appmod-catalog-blueprints

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/cdklabs/cdk-appmod-catalog-blueprints) · [官网](https://cdklabs.github.io/cdk-appmod-catalog-blueprints/) · 组织维护

**面向 AWS 的用例驱动 CDK 蓝图库：AI 聊天/文档处理等方案快速部署**

cdklabs 维护的应用现代化蓝图库，以可组合的 CDK L3 construct 形式提供基础设施模板：InteractiveAgent/BatchAgent 等智能体构造、Bedrock 驱动的文档处理与 RAG 知识库、前端托管及网络/可观测性基础组件，覆盖客服聊天机器人、保险理赔、欺诈检测等场景。支持 TypeScript/Python/Java/.NET（JSII），可整方案 3 条命令部署，也可引用单个 construct 定制；另提供 MCP Server 供 AI 编码助手（Kiro、Claude Code、Codex 等）辅助搭建。默认内置 KMS 加密、最小权限 IAM 与 CDK Nag 合规检查，声明为示例而非受支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个核心 construct：InteractiveAgent、AgenticDocumentProcessing、BedrockKnowledgeBase、Frontend 等
- 三层设计：抽象基类→通用实现→行业方案（银行/保险/电商示例）
- 多语言发布：npm/PyPI/NuGet/Maven（JSII）
- MCP Server + Agent Skills 支持用 genAI 编码助手搭建方案

## 适用场景

- 在 AWS 上快速部署客服聊天机器人或 RAG 问答方案
- 在自有 CDK 项目中引用单个 construct 定制 AI 应用
- 用 AI 编码助手按 MCP 工具生成正确的 construct 组合

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L16: Application Modernization (AppMod) Catalog Blueprints is a comprehensive library of **use case-driven infrastructur
> L82: |**InteractiveAgent**|Real-time chatbots with SSE streaming, sessions, and auth|

## 星数曲线

```mermaid
xychart-beta
    title "cdklabs/cdk-appmod-catalog-blueprints 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `494db34c8d47` · [字段定义](../../DATASET.md)*
