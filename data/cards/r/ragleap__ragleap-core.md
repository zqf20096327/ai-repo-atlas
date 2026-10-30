# ragleap/ragleap-core

⭐ 19 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/ragleap/ragleap-core) · [官网](https://ragleap.com) · 组织维护

**自托管的企业级 AI 员工系统：46 个岗位角色、审批制自主执行**

自托管的 agentic 商务系统 RagLeap 的开源引擎（MIT），提供 46 个岗位角色的 AI 员工（9 个通用角色加 37 个垂直角色），通过 Graph RAG 基于自有文档运行，支持 WhatsApp/Telegram/Discord 与语音呼入。关键机制：三级自主模式（off/semi/full）与逐动作审批门、无网络沙箱内运行 Python/shell、允许清单 MCP 客户端、跨渠道持久记忆、AI Office 仪表盘。可用 Ollama 完全本地运行，或接入 19 种提供商。安装需 Docker；部分组件（voice、agents、memory、security）标注为 alpha/pre-alpha；README 自述『对早期状态诚实』，Windows 安装仅在单机测试过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 46 个岗位角色的 AI 员工（9 通用 + 37 垂直）
- off/semi/full 三级自主模式与逐动作审批门
- 无网络沙箱执行 Python/shell，允许清单 MCP 客户端
- 可配合 Ollama 完全本地运行（对话与嵌入），文档不出服务器

## 适用场景

- 在我自己的服务器上用自有文档跑一个企业 AI 员工系统
- 通过 WhatsApp/Telegram/Discord 与审批制的 AI 员工协作处理业务
- 不想用托管云、要自持密钥与数据地部署业务 AI

## 场景标签

`工作流自动化` `RAG` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L28: RagLeap Core is the open-source engine behind RagLeap — a self-hosted, agentic system that runs your business from 
> L30: **46 role-based AI Employees:** 9 core generalist roles (AI Manager, Secretary, CEO, Sales, Support, HR, Finance, M
> L40: - Can run fully local with Ollama for chat and embeddings (small models on a CPU are slower and less accurate than 

## 星数曲线

```mermaid
xychart-beta
    title "ragleap/ragleap-core 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-19 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c13bde6528d9` · [字段定义](../../DATASET.md)*
