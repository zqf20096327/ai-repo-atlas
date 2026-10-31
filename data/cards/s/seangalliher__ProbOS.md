# seangalliher/ProbOS

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/seangalliher/ProbOS) · [官网](https://probos.dev) · 个人维护

**以自主 agent 为组件的实验性操作系统运行时**

用概率性多 agent 网格替代传统 OS 机制：自然语言替代 syscalls，agent 通过能力匹配、Hebbian 路由与 Bayesian 信任自选任务，重要操作由多 agent 共识与指挥链审批把关。包含 15 个船员 agent（六个部门）、意图总线、ChromaDB 情景记忆与离线"做梦"整合、共识投票、DID 身份与实验性联邦、React+Three.js 的 HXI 界面及 Discord/Slack 等渠道适配。定位为 Alpha 阶段，API 会变化；需要 Python 3.12+、git，核心安装含 PyTorch 与 ChromaDB，LLM 端点可选启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言分解为意图 DAG，多 agent 共识治理重要操作
- 15 个船员 agent + 基础设施 agent，默认启动 81 个 agent（51 个池）
- ChromaDB 情景记忆与空闲期记忆整合（dream cycle）
- 支持 MCP 服务器接入与逐 agent/逐工具授权

## 适用场景

- 以对话方式让一组受治理的 agent 长期执行任务
- 研究多 agent 共识、信任与自组织协调机制
- 在无人值守时通过 Night Orders 委托 agent 持续工作

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: ProbOS reimagines the OS as a mesh of probabilistic agents rather than deterministic processes. Instead of syscalls
> L68: - **Cognitive.** The Ship's Computer decomposes natural language into a DAG of typed intents and executes it. The d

## 星数曲线

```mermaid
xychart-beta
    title "seangalliher/ProbOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `57e24b5f1636` · [字段定义](../../DATASET.md)*
