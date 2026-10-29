# Wh1isper/ya-mono

⭐ 19 · Python · BSD-3-Clause · 推送 2026-10-27 · [GitHub](https://github.com/Wh1isper/ya-mono) · 个人维护

**多包 monorepo：基于 Pydantic AI 的 Agent SDK/CLI/运行时服务**

由多个 workspace 包组成的 Agent 开发工具集：ya-agent-sdk 提供 Python SDK 构建代理，yaacli 是 TUI 参考实现，ya-claw 是单节点运行时 Web 服务（SQLite 优先存储、bridge、schedule），另含 OAuth 订阅登录组件（如通过 ChatGPT 订阅运行 Codex）、流协议适配器与 Vite+React Web 壳。通过 make install 从源码安装，或用 uv tool install 安装发布包；提供多个 Dockerfile 构建 YA Claw 与 Platform 镜像。ya-agent-platform 标注为 WIP、范围 TBD。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Python SDK（Pydantic AI）+ TUI CLI + 单节点运行时服务（ya-claw）
- OAuth 登录/令牌存储支持订阅制模型访问（oauth@codex:gpt-5.5）
- SQLite 优先存储、bridge 命令（如 lark）与 Web 壳
- 提供 Docker 镜像构建（ya-claw / workspace / platform）

## 适用场景

- 用 Python SDK 与 capability 插件机制构建自定义 Agent
- 通过订阅账号 OAuth 凭据访问 Codex 等模型
- 自托管单节点 Agent 运行时并对接桥接通道

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: - `packages/ya-agent-sdk` — Python SDK for building AI agents with Pydantic AI
> L17: - `packages/yaacli` — TUI reference implementation built on top of `ya-agent-sdk`
> L18: - `packages/ya-claw` — workspace-native single-node runtime web service with `WorkspaceProvider`, in-process runtim

## 星数曲线

```mermaid
xychart-beta
    title "Wh1isper/ya-mono 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5db2eafe02b7` · [字段定义](../../DATASET.md)*
