# kayba-ai/Kyoko

⭐ 100 · Python · Apache-2.0 · 推送 2026-06-12 · [GitHub](https://github.com/kayba-ai/Kyoko) · [官网](https://kayba-ai.com) · 组织维护

**本地化 AI agent 遥测调试与修复系统：测量、定位并改进 agent**

面向 AI agent 开发者的全本地工具：接入遥测（Python/TypeScript SDK、OTLP/GenAI、导入器）采集运行轨迹，跨 run 分组重复失败为带证据的 issue，生成可审查的修复提案（上下文/技能/评估/框架），经回放、确定性检查、评估对比与人工锁的门控后才应用变更。可调用 Codex、Claude Code 等现有编码 agent CLI 起草修复，无需单独模型 API key；提供本地 SQLite、loopback 仪表盘、JSON CLI 与 stdio MCP 服务器。需 Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 run 将重复失败分组为带证据与严重度的 issue 队列
- 门控机制：回放+确定性检查+评估对比+人工锁通过后才应用修复
- 复用 Codex/Claude Code/OpenClaw 等现有 CLI 起草修复，无需独立模型 key
- Python/TypeScript SDK、OTLP/GenAI、MCP、本地仪表盘等多种接入与控制面

## 适用场景

- 调试 AI agent 重复出现的工具误用、上下文缺失或路由失败
- 在人工审查或自主模式下自动修复 agent 上下文与技能
- 本地留存 agent 轨迹、issue 与评估数据以满足数据不出机的要求

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L12: **Kyoko is a fully local system for measuring, debugging, and improving AI
> L34: - **Finds the failures that repeat across runs.** Kyoko looks across runs, groups recurring problems into evidence-
> L61: 4. **Evals:** Kyoko reruns failing traces, runs deterministic checks, and

## 星数曲线

```mermaid
xychart-beta
    title "kayba-ai/Kyoko 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 98 --> 101
    line [99, 100, 100]
```

2026-10-18 99 → 2026-10-30 100（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6577dda96d9c` · [字段定义](../../DATASET.md)*
