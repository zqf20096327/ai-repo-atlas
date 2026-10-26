# RealDealCPA-VR/Iron-Jarvis

⭐ 64 · Python · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/RealDealCPA-VR/Iron-Jarvis) · [官网](https://www.realdealcpa.ai) · 个人维护

**本地优先的桌面 AI 控制台：统一编排模型、Agent、工具与本机**

面向个人用户的桌面应用（Electron + Next.js 仪表盘 + FastAPI 守护进程），把聊天、多 Agent 任务（Missions）、运行 Claude Code/Codex 的终端、定时与工作流自动化、多层记忆和文档读写整合在一处。可接入 API key、Claude/Codex 订阅登录或本地 Ollama/vLLM/LM Studio 服务，默认本地模型故障时拒绝回答而不回退云端；操作留痕、风险动作需批准、代码改动不自动合并。Windows 提供安装包，macOS/Linux 需从源码构建（Python 3.12+/Node 20+），可离线运行内置演示模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天/Agent/终端/自动化/记忆统一在一个桌面应用中编排
- 接入 API key、订阅登录或本地 Ollama/vLLM/LM Studio/OpenAI 兼容服务
- 本地优先：SQLite 本地存储、密钥加密、默认拒绝云端回退（local_primary_policy=refuse）
- 操作留痕与审批：未授权工具拒用并记录，代码改动落 git 分支不自动合并

## 适用场景

- 在一个桌面应用里统一使用多个模型和 Agent 处理日常工作
- 给一组专职 Agent 下达一个目标并追踪交付结果
- 在本机离线或本地模型环境下运行带工具调用的 AI 助手

## 场景标签

`AI 助手` `多智能体` `编码 Agent` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L14: Iron Jarvis is a desktop app that turns AI models into a working system: **a chat that answers in seconds and quiet
> L30: ### 💬 Chat that keeps up with you
> L40: - **Missions.** Give the team one objective. Jarvis splits it among specialist agents (planner, builder, reviewer, 

## 星数曲线

```mermaid
xychart-beta
    title "RealDealCPA-VR/Iron-Jarvis 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-25", "2026-10-26"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-19 63 → 2026-10-26 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `47faca7c23ce` · [字段定义](../../DATASET.md)*
