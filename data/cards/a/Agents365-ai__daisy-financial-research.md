# Agents365-ai/daisy-financial-research

⭐ 29 · Python · 推送 2026-05-17 · [GitHub](https://github.com/Agents365-ai/daisy-financial-research) · 个人维护 · 中文 README

**面向 AI agent 的股票研究技能：计划→取数→校验→报告**

以 skill 形式安装到 Claude Code、Opencode、OpenClaw 等 agent 框架的股票研究工作流包，覆盖 A 股、港股与美股。用户向 agent 指定股票、行业或主题后，agent 按 10 步流程执行：注入历史决策记忆、写 JSONL 计划、按代码后缀路由数据源（Tushare/AKShare/yfinance）、防重复调用提示、银行股自动改用 RoTE/CET1 框架、数值校验、生成 Markdown/HTML/PDF 报告，并将评级写入跨会话决策日志，可回测已实现 alpha。需 TUSHARE_TOKEN。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 计划→取数→校验→报告的 10 步分析师工作流，落盘审计痕迹
- 跨会话决策日志：pending→resolved 生命周期，自动结算 alpha 并回测命中率/最大回撤
- 银行/保险股自动跳过 DCF，改用 RoTE/CET1/NIM/P/B 框架
- 每个脚本支持 --schema/--dry-run/JSON 信封与结构化退出码的 agent 原生 CLI

## 适用场景

- 让 agent 对个股做带出处的深度研究报告（DCF、Bull/Bear 综合）
- 跑 A 股红利/价值/动量多因子选股和港股通筛选
- 记录并回测 agent 自己的历史评级表现

## 场景标签

`金融量化` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: > Stock research skill for AI agents. Plan → fetch → validate → report. A-share, HK, US.
> L66: |Claude Code|`git clone https://github.com/Agents365-ai/daisy-financial-research.git ~/.claude/skills/daisy-financi
> L95: **Agent-native CLI contract** — every script supports:

## 星数曲线

```mermaid
xychart-beta
    title "Agents365-ai/daisy-financial-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `57ae09716cbf` · [字段定义](../../DATASET.md)*
