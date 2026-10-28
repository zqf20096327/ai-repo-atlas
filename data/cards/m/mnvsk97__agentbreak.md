# mnvsk97/agentbreak

⭐ 20 · Python · MIT · 推送 2026-05-24 · [GitHub](https://github.com/mnvsk97/agentbreak) · 个人维护

**面向 AI agent 的基础设施混沌测试工具：注入故障测韧性**

AgentBreak 由代理/故障注入层、MCP 巡检与评分体系构成：将 agent 的 LLM/MCP 流量指向本地 5005 端口的 chaos proxy，按 YAML 场景注入 10 种内置故障（HTTP 错误、延迟、超时、无效 JSON、tool poisoning、rug pull 等），并评分故障后 agent 的恢复与安全行为（重试、泄露数据等），支持 mock 与 proxy 两种模式和 CI 流水线运行。提供 Python CLI（pip 安装）及 coding agent 技能入口（npx skills add），通过自然语言指令即可生成场景并产出报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- chaos proxy 代理 LLM/MCP 流量，10 种内置故障注入（可靠性与安全两类）
- 评分聚焦故障后 agent 行为：恢复重试得分、循环与泄露数据扣分
- 支持 7 种预设场景与 YAML 自定义，新故障只需文件夹+manifest.yaml
- mock 模式无需 API key，可在 GitHub Actions 等 CI 中运行

## 适用场景

- 在 CI 中对 LLM agent 做混沌测试与韧性回归
- 检测 agent 是否会遵循被投毒的 MCP 工具指令或泄露数据
- 通过自然语言让 coding agent 自动生成并执行韧性测试

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L30: The skill uses the Python CLI as the reliable engine for proxying, fault injection, MCP inspection, scorecards, and
> L51: curl localhost:5005/_agentbreak/scorecard

## 星数曲线

```mermaid
xychart-beta
    title "mnvsk97/agentbreak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `550ffa5286d1` · [字段定义](../../DATASET.md)*
