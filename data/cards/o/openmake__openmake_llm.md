# openmake/openmake_llm

⭐ 43 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/openmake/openmake_llm) · [官网](https://openmake.cc/en/) · 组织维护 · 中文 README

**自托管 AI 工作台：编排多模型、agent 与 MCP 工具完成通用任务**

面向自托管用户的开源 AI 工作台与 agent 运行时：通过 LiteLLM 网关接入 vLLM、Ollama 或任意 OpenAI 兼容端点，BYOK 密钥 AES-256-GCM 加密存储。Planner 将请求拆分为搜索、推理、图像生成等任务，由按角色/能力分配的模型并行执行；agent 可在 Docker 沙箱执行代码、浏览器容器内抓取网页，支持审批策略、MCP 目录、23 个内置工具与 Deep Research 生成带引用报告。一键脚本安装，Linux/macOS 原生、Windows 需 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Planner 拆分任务到按角色/能力分配的模型并行执行
- agent 运行时：Docker 沙箱代码执行、子 agent、审批策略、任务持久化与恢复
- MCP 目录与 23 个内置工具，兼容 Claude Code 插件/技能约定
- Deep Research 生成带引用报告，可导出 HTML/PDF/DOCX

## 适用场景

- 在我自己的服务器上用本地模型做研究、聊天和图像等多模态任务
- 让 agent 在沙箱里规划并执行多步骤工作，关键步骤需我审批
- 自建一个多模型编排、带审计日志的团队 AI 工作台

## 场景标签

`模型网关` `多智能体` `AI 助手` `多模态` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Open-source AI workspace and agent runtime for local, open-weight, and OpenAI-compatible models.
> L42: Most self-hosted AI interfaces help you **talk to a model**. OpenMake is designed to **coordinate models, tools, an
> L50: |**OpenMake**|**Orchestrate models, agents, and tools for general AI work**|

## 星数曲线

```mermaid
xychart-beta
    title "openmake/openmake_llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5e2cb84528f3` · [字段定义](../../DATASET.md)*
