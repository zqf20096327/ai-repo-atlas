# matteing/opal

⭐ 62 · Elixir · MIT · 推送 2026-08-12 · [GitHub](https://github.com/matteing/opal) · 个人维护

**Elixir 编写的轻量编码 agent CLI 与可嵌入库**

基于 Erlang/OTP 构建的编码 agent：既是可运行 shell 命令、编辑文件、派生子 agent 并行工作的 CLI，也可作为 Elixir 库嵌入应用，通过 Erlang 消息传递直接交互，或经 JSON-RPC 从任意语言调用。内置 10 个工具（read_file/edit_file/shell/sub_agent/DAG 任务追踪等），支持运行中重定向指令与跨终端实时内省。唯一支持的 LLM 提供方是 GitHub Copilot。作者声明这是无沙箱、无权限系统的个人研究项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 子 agent 为 OTP 进程，由监督树管理生命周期
- JSON-RPC transport 可用于自建 UI/跨语言调用
- 10 个内置工具含 DAG 任务追踪与自我调试（debug_state）
- 可经 Opal.prompt 在工具调用间隙重定向任务

## 适用场景

- 用 CLI 让 agent 读改文件、跑构建与测试并修复问题
- 把 agent 系统作为 Elixir 依赖嵌入自己的应用
- 通过 JSON-RPC 从其他语言构建自己的 agent UI

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: - A **small coding agent CLI** you can use to build things.
> L12: - An **idiomatic Elixir library** you can drop into your app to get an agent system.
> L27: - **Parallelize work** — sub-agents are cheap OTP processes, so it can plan + split tasks up easily.

## 星数曲线

```mermaid
xychart-beta
    title "matteing/opal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-27 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `085acf910d45` · [字段定义](../../DATASET.md)*
