# raiyanyahya/ensemble

⭐ 13 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/raiyanyahya/ensemble) · 个人维护

**多模型共识辩论工具：多个 LLM 提案、互审、反驳、投票、合成**

让 OpenAI、Anthropic、DeepSeek 三家模型通过文件系统进行多轮辩论：各模型独立提案、匿名互审（Participant A/B/C）、反驳针对自己提案的批评、投票（FINALIZE/REVISE/SPLIT），多数达成一致后由胜出作者起草合成答案并经全组批准；僵局时用 Borda 排名打破平局。全程每一步以 Markdown 文件落盘，可恢复、可审计，支持按模型统计 token 与费用并设预算上限。提供 CLI（ensemble）与 stdio MCP 服务器（ensemble-mcp），可接入 Claude Code、Cursor、Cline 等编辑器。需至少两家提供商的 API key，Python ≥3.10，暂不在 PyPI，从 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轮辩论流程：提案→互审→反驳→投票→合成→确认，每步落盘可恢复
- 参与者匿名化（Participant A/B/C），仅凭论点评判
- Borda 排名仅在僵局平票时决定结果，多数决路径不受影响
- 按模型统计 token/USD 费用，支持 --budget 预算上限与可选网页检索引证

## 适用场景

- 对高风险技术决策征求多模型交叉审查后的共识意见
- 在 Claude Code / Cursor 等编辑器中通过 MCP 调用多模型辩论
- 比较不同 LLM 对同一问题的推理并留存完整审计记录

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: Multi-model consensus debate via the filesystem. Several top LLMs (OpenAI,
> L18: the critiques of their own proposal, and **vote** — and, once a majority agrees,
> L57: - 🔌 **CLI + MCP** — a rich terminal UI *and* a one-tool MCP server for Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "raiyanyahya/ensemble 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `981712d387ac` · [字段定义](../../DATASET.md)*
