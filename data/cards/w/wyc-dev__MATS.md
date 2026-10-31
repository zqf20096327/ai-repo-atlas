# wyc-dev/MATS

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-09-20 · [GitHub](https://github.com/wyc-dev/MATS) · [官网](https://mats.trading/) · 个人维护 · 中文 README

**自进化加密量化交易系统：9 个 AI agent 辩论并执行每笔交易**

TypeScript 编写的自动化量化交易系统，面向 Hyperliquid 交易：LLM 读取双时间框架 K 线与世界事件给出方向判断，9 个 AI agent（含 Skeptics 审查与 System Engineer 自修复）对每笔交易辩论并加权表决；配套 60+ 层认知进化管线（Q-RL alpha 发现、PAEL 出场学习、边缘验证、反模式记忆等）。快速启动路径基于本地 Ollama（Node.js 22+），提供 npm 启动与 Web Dashboard；README 含大量未经独立验证的收益性描述，不构成业绩证据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个 AI agent 辩论每笔交易，Skeptics 行使否决权
- LLM 读取 1h×30 + 5m×60 双时间框架 K 线作为方向来源
- System Engineer 模式可自主检测并修复学习系统 bug，修复经 tsc + 测试验证后自动回滚或重启
- 60+ 层认知进化管线：Q-RL alpha 发现、PAEL、边缘验证、反模式记忆、动态信念门限

## 适用场景

- 在 Hyperliquid 上运行多 agent 辩论驱动的自动化交易
- 让 LLM 阅读图表与世界事件生成并验证交易论点
- 通过自然语言向系统设定交易偏好（如仅周一 GMT 交易）

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L3: **9 AI agents debate every trade. Skeptics stress-tests every thesis. System Engineer fixes its own bugs. A 60+-laye
> L7: - 🧠 **LLM World-Model Layer** — the LLM is the *direction source*: reads K-LINE charts (1h×30 + 5m×60, dual-timefram
> L37: ## Quick Start (Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "wyc-dev/MATS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3ca2ac207e10` · [字段定义](../../DATASET.md)*
