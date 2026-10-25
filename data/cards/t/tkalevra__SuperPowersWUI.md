# tkalevra/SuperPowersWUI

⭐ 64 · Python · MIT · 推送 2026-04-25 · [GitHub](https://github.com/tkalevra/SuperPowersWUI) · 个人维护

**Open WebUI 工具：将 Superpowers 开发工作流移植到本地/远程 LLM**

移植自 Jesse Vincent 的 Superpowers，以 Open WebUI 工具（粘贴 superpowers_tool.py 即可安装）形式提供结构化 agentic 开发工作流：brainstorm → spec → 自动审查 → TDD 计划 → 逐任务执行，每阶段由子代理审查。通过任意 OpenAI 兼容端点（LM Studio、Ollama 或远程 API）运行，需模型支持原生 Function Calling。配套 Fileshed 可持久化 spec/plan 文件；内置 SkillStack 命令校验缓存，可基于 man 页校验生成的命令。以 `cook`（自主）或 `ask`（逐步确认）两种模式控制节奏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- brainstorm→spec→plan→execute 四阶段工作流，每阶段经子代理审查
- 兼容任意 OpenAI 兼容端点（LM Studio/Ollama/远程 API）
- SkillStack 命令知识缓存：校验 flag/子命令/坏模式，回退 man 页与在线文档
- spec/plan/scratch 文档落盘，配合 Fileshed 跨会话持久化

## 适用场景

- 让本地 LLM 按规范流程产出规格文档与 TDD 实现计划
- 逐任务执行开发计划并控制推进节奏
- 在 Open WebUI 内保存并浏览各阶段的规格与计划文档

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A structured agentic development workflow for Open WebUI —
> L11: brainstorm → spec → review → plan → review → execute
> L34: - Any OpenAI-compatible LLM endpoint (LM Studio, Ollama, or remote API)

## 星数曲线

```mermaid
xychart-beta
    title "tkalevra/SuperPowersWUI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-25 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8e3f7f6d4894` · [字段定义](../../DATASET.md)*
