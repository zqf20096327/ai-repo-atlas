# deepfates/cantrip

⭐ 128 · Elixir · MIT · 推送 2026-07-24 · [GitHub](https://github.com/deepfates/cantrip) · [官网](https://deepwiki.com/deepfates/cantrip) · 个人维护

**Elixir 多智能体运行时：以受限循环构建可复用的 LLM 智能体**

基于 Elixir/BEAM 的智能体运行时与库。核心概念为 Circle（环境）、Medium（对话/Elixir/Bash 三种思维介质）、Gates（文件读取等边界能力）、Wards（回合数等运行时约束）、Loom（可分叉重放的执行记录树）。cantrip 是绑定 LLM、身份与环境的可复用值，通过 cast/summon/cast_batch 调用；预装配的 Familiar 协调器面向代码库工作，支持子智能体扇出、Mnesia 分布式存储、多 seed 评测，并经 ACP 接入 Zed/JetBrains 等编辑器。LLM 接入经 ReqLLM 配置 OpenAI 兼容端点。默认沙箱为 Dune 子进程端口隔离，Familiar 默认 unrestricted。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Circle/Medium/Gates/Wards/Loom 五元原语构建智能体循环
- 对话、Elixir 代码、Bash 三种 Medium，代码介质经 Dune 端口隔离沙箱执行
- 预装配 Familiar 协调器：代码库工作、子智能体委派、Mnesia loom
- 经 agent_client_protocol 提供 ACP stdio 接入编辑器

## 适用场景

- 在 Elixir 代码库中运行本地编码智能体（Familiar）
- 将智能体挂载到 Zed/JetBrains 等支持 ACP 的编辑器
- 跨多 seed 运行提示词场景并按评分标准做回归评测
- 在 BEAM 集群上分布式运行子智能体并复制 loom

## 场景标签

`多智能体` `编码 Agent` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L14: An agent is the same shape. The model predicts a token; put it in a loop
> L28: A **cantrip** is the reusable value that binds an LLM, an identity, and a
> L71: - **Protocol surface** — expose the same runtime through library calls, Mix

## 星数曲线

```mermaid
xychart-beta
    title "deepfates/cantrip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 127 --> 129
    line [128, 128]
```

2026-10-18 128 → 2026-10-25 128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b5d795495771` · [字段定义](../../DATASET.md)*
