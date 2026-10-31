# tellmefrankie/ai-investment-skills

⭐ 23 · HTML · MIT · 推送 2026-05-24 · [GitHub](https://github.com/tellmefrankie/ai-investment-skills) · [官网](https://jaehyunpark.gumroad.com/l/tcyahy) · 个人维护

**面向个人投资者的 Claude Code 技能集：期权流扫描、止损监控等**

一组以 SKILL.md 格式发布的 Claude Code 技能，分免费与 29 美元付费两层：免费层含 EV 情景计算器与新闻情绪引擎，付费层含期权流分析器（P/C 比率扫描与彩票式看涨期权过滤）、9 波晨报 agent、止损/止盈监控（Telegram 告警）与多 agent 编排器；另附 6 个无需 API key 的开发工具（git standup、PR 描述生成等）。作者声明技能来自真实账户的每日运行。安装方式为复制 SKILL.md 到 ~/.claude/skills，兼容 Claude Code、Cursor、Codex CLI、Gemini CLI 等支持该标准的 agent，另提供带免费额度（5 次/天）的期权分析 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 彩票式看涨期权过滤：按 delta<0.15、premium<$0.10 剔除后输出调整 P/C 比率
- 9 波晨报 agent：宏观→板块→技术面→新闻→批评→模拟
- 止损/止盈监控并经 Telegram 告警（示例 1.8 秒送达）
- 附 35 个测试用例与含信号反转样例的 eval fixtures

## 适用场景

- 每天早上让 Claude Code 跑一遍投资晨报与期权扫描
- 过滤高散户期权活动标的的失真 P/C 比率信号
- 持仓止损/止盈监控并接收 Telegram 提醒

## 场景标签

`金融量化` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: 10+ Claude Code skills — investment analysis and developer tools — options flow scanner, stop-loss monitor, earnings
> L111: Works with Claude Code, Cursor, Codex CLI, Gemini CLI — any agent supporting the SKILL.md standard.

## 星数曲线

```mermaid
xychart-beta
    title "tellmefrankie/ai-investment-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f47a6619bace` · [字段定义](../../DATASET.md)*
