# MindFlock/MindFlock

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/MindFlock/MindFlock) · [官网](https://mindflock.ai) · 组织维护

**本地编排多个 AI 编码 agent 的桌面工作台，由工单队列驱动**

在用户本机运行的 AI 编码 agent 并行编排工具：轮询 GitHub Issues、Jira、Linear、Shortcut、Asana 中分配给用户的工单，为每个工单创建独立 git worktree、安装依赖并启动已注入工单内容的 agent 会话；用户最终审阅 diff 并逐键完成 commit→push→PR→merge，默认不做任何自动提交。引擎绑定 127.0.0.1，不设云端与账号，代码不离开本机磁盘；可配置 Ollama/LM Studio/OpenAI 兼容本地模型实现零代码外发。提供 Windows/macOS/Linux 桌面应用与 curl 脚本安装的 CLI 两种使用方式，需 Python 3.12+。限制：依赖自动安装目前覆盖 Python/uv 仓库，其他技术栈需自行声明 setup_commands；claude 仅支持 Anthropic API、无本地模型路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工单（GitHub Issues/Jira/Linear/Shortcut/Asana）自动变为带独立 git worktree 的已启动 agent 会话
- 默认不自动 commit/push/merge，每步均为用户点击；可选 fast-track 设定自动化深度
- 无云端、无账号、无遥测，引擎绑定 127.0.0.1，代码仅存于本地磁盘
- Settings→Local model 可将 codex/aider/goose 指向 Ollama、LM Studio 或任意 OpenAI 兼容本地服务器

## 适用场景

- 把分配给自己的工单自动变成多个并行运行的 AI 编码会话，最后只做 diff 审阅与合并
- 在本地隔离的 worktree 中同时跑多个 agent CLI 处理半成品分支
- 对代码外发有要求时，用本地模型让工单从分配到提交全程不离开本机
- PR 回来的评审意见自动变成新会话，未解决行内评论进入 prompt

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L44: Work assigned to you in **GitHub Issues, Jira, Linear, Shortcut, or Asana**
> L58: You come in at the end that needs a human: **read the diff**, then drive it home

## 星数曲线

```mermaid
xychart-beta
    title "MindFlock/MindFlock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `daee4b9a6cff` · [字段定义](../../DATASET.md)*
