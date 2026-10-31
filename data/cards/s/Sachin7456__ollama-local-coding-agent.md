# Sachin7456/ollama-local-coding-agent

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/Sachin7456/ollama-local-coding-agent) · 个人维护

**面向本地 Qwen 模型的离线终端编码 Agent（经 Ollama 运行）**

纯 TypeScript 编写的命令行编码 Agent，零依赖、无构建步骤，通过本地 Ollama 服务调用 Qwen 模型（如 qwen2.5-coder/qwen3-coder），在 read→decide→act→observe 循环中使用 read/write/edit/bash 等 10 种工具，支持最多 2 个并行子 Agent、跨会话长期记忆、会话恢复与上下文自动压缩。所有动作经权限门控，文件工具限制在工作区内，可选 Docker/WSL 隔离运行。面向需要私有、离线编码 Agent 的开发者，无云服务与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零依赖、无构建步骤，克隆后直接 npm start 运行
- 10 种工具 + 权限门控的 read→decide→act→observe Agent 循环
- 最多 2 个并行子 Agent、长期记忆、可恢复会话
- 针对小模型做参数校验修复与工具调用恢复，697 个自动化测试

## 适用场景

- 在离线环境用本地 Qwen 模型完成读写文件、执行命令的编码任务
- 团队避免云 AI 成本与代码外泄，自托管私有编码助手
- 学习一个可读的 Agent 架构实现

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: ### Turn a model running on your own machine into a real, tool-using software agent.
> L39:  runs commands in a permission-gated **read → decide → act → observe** loop —
> L50: 🧩 Use real tools (`read` · `find-files` · `grep` · `write` · `edit` · `multi-edit` · `bash` · `powershell` · `todo`

## 星数曲线

```mermaid
xychart-beta
    title "Sachin7456/ollama-local-coding-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8cbe799e112f` · [字段定义](../../DATASET.md)*
