# knewstimek/gorchera

⭐ 16 · Go · 推送 2026-04-05 · [GitHub](https://github.com/knewstimek/gorchera) · 个人维护

**Go 多智能体编排引擎：让 AI 监督者通过任务制完成软件工作**

Go 编写的有状态多智能体编排引擎，按 director->executor->evaluator 三段流水线协调 GPT/Claude 等 AI 完成软件的规划、实现、评审与测试；监督 agent 通过 MCP（17+ 工具）下发任务、注入指令并轮询状态，自身不直接写代码。提供 3 档严格度、5 档野心度、3 种流水线模式、任务链、机械化 automated_checks 与工作区变更检测；支持自改进（通过编排任务修改自身代码库）。内嵌 Web 仪表盘，从源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三角色流水线：规划->执行->评估，带 fix 循环重试
- MCP server 提供 17+ 工具供 Claude 等监督 agent 集成
- 机械化 automated_checks（grep/file_exists/file_unchanged/no_new_deps）
- 支持 GPT/Codex、Claude、Mock 提供方适配器与按角色覆盖模型

## 适用场景

- 让 AI 监督者以任务制完成代码实现与评审
- 多目标任务链的顺序执行与中途干预
- 需要可审计、产物留痕的 AI 编码工作流

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: Go stateful multi-agent orchestration engine / harness engineering with self-improvement capabilities.
> L29: - **MCP server**: 17+ tools for supervisor agent integration (stdio JSON-RPC 2.0)

## 星数曲线

```mermaid
xychart-beta
    title "knewstimek/gorchera 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4fdc118fd573` · [字段定义](../../DATASET.md)*
