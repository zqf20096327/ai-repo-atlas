# wiki3-ai/agent-client-kernel

⭐ 35 · Jupyter Notebook · BSD-3-Clause · 推送 2026-05-16 · [GitHub](https://github.com/wiki3-ai/agent-client-kernel) · [官网](https://wiki3-ai.github.io/agent-client-kernel/) · 组织维护

**Jupyter Kernel：作为 ACP 客户端在笔记本中接入编码 agent**

基于 MetaKernel 实现的 Jupyter 内核，充当 Agent Client Protocol (ACP) 的客户端：通过 stdio 启动并连接外部 ACP 编码 agent（如 codex-acp），使用户在 JupyterLab/Jupyter Notebook 单元格中直接与 AI 编码助手对话，获取代码编写、调试、重构等协助。为 Codex、Gemini、Goose、Kimi、Docker cagent 预配置 devcontainer；支持环境变量切换 agent、MCP 服务器管理、权限与会话控制（%agent magic）。也可从源码用 uv 手动安装，需自备 ACP 兼容 agent 二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 客户端侧完整 ACP 协议实现，可连接任意 ACP 兼容 agent
- 为 Codex/Gemini/Goose/Kimi/Docker cagent 预配置 5 种 devcontainer
- %agent magic 统一管理 MCP 服务器、权限、会话与 agent 配置
- 基于 MetaKernel，内置 magics 与 shell 命令

## 适用场景

- 在 Jupyter 笔记本单元格中直接调用 Codex 等编码 agent
- 通过 GitHub Codespaces 一键启动带 agent 的 JupyterLab 环境
- 在同一 notebook 前端之间切换不同 ACP 兼容 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: This kernel allows you to interact with external ACP agents directly from Jupyter notebooks. It acts as an ACP clien
> L20: The kernel spawns and communicates with external ACP agents (such as codex-acp) via stdio, allowing you to interact
> L24: - **ACP Client Implementation**: Full client-side ACP protocol support

## 星数曲线

```mermaid
xychart-beta
    title "wiki3-ai/agent-client-kernel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bb672ba57855` · [字段定义](../../DATASET.md)*
