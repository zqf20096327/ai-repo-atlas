# Katagiri-Hoshino-Lab/VibeCodeHPC

⭐ 43 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/Katagiri-Hoshino-Lab/VibeCodeHPC) · 组织维护

**多 AI 编程 CLI 协同的 HPC 代码自动调优框架**

通过 tmux 让多个 AI 编程 CLI（Claude Code、Codex CLI、Gemini CLI、Qwen Code、Kimi Code CLI 等 8 种）协同工作的多智能体框架，无需外部编排框架。内置默认 HPC 自动调优工作流：PM→SE↔PG×N→CD 的层级结构，支持可插拔策略（HPC 并行化、本地 LLM 部署、GPU 优化）、进化式并行搜索与 4 层 SOTA 跟踪。用户需准备需求定义文档、站点信息与待优化代码，其余由 agent 运行时生成。快速上手见 docs/quickstart.md。

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

- 层级多智能体结构 PM → SE ↔ PG × N → CD
- tmux IPC 实现智能体间通信，无需专用运行时
- 支持 8 种 AI 编程 CLI 同时运行
- 内置按 PG 的性能时间线与按 agent 的上下文用量监控

## 适用场景

- HPC/CFD 代码的并行化与性能自动调优
- 让多个 AI 编程 CLI 分工协作完成代码优化迭代
- 跟踪调优过程中的最优结果（本地/家族/硬件/项目 4 层）

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: Multiple AI coding CLIs coordinate via tmux — no external orchestration framework required. Pluggable strategies ada
> L17: - **Hierarchical Multi-Agent**: PM → SE ↔ PG × N → CD
> L64: Claude Code, Codex CLI, Cline CLI, Gemini CLI, OpenCode, vibe-local, Qwen Code, Kimi Code CLI

## 星数曲线

```mermaid
xychart-beta
    title "Katagiri-Hoshino-Lab/VibeCodeHPC 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-31 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b48c353917d9` · [字段定义](../../DATASET.md)*
