# ayagmar/llm-usage-metrics

⭐ 35 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ayagmar/llm-usage-metrics) · [官网](https://ayagmar.github.io/llm-usage-metrics/) · 个人维护

**17 种 AI 编码工具的 token 与成本用量报告 CLI**

读取本机及 ssh 可达的其他机器上 17 种 AI 编码工具（Claude Code、Codex、Gemini CLI、Copilot CLI、OpenCode 等）的本地会话日志，归一化为统一 UsageEvent 后存入 SQLite 事件账本，提供按日/周/月/小时/项目/会话的 token 与估算成本报告、5 小时计费窗口检查、订阅价格对比、Git 活动关联分析、交互式 HTML 报告与 JSON/Markdown 导出。需要 Node.js 22.16+/24+ 或 Bun 1.4+，支持 npx 免安装运行；部分来源适配器尚未对照真实日志校验。

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

- 17 种 AI 编码工具本地会话日志的统一解析与成本报告
- SQLite 事件账本支持增量解析与已删除文件的历史保留
- 多机器经 ssh 聚合用量，跨机器重复会话只计一次
- 生成自包含离线 HTML 交互报告，支持 --redact 脱敏

## 适用场景

- 查看我今天/本周/本月在各 AI 编码工具上的 token 与花费
- 对比 API 计价用量与订阅套餐价格，评估换模型的成本
- 按项目维度归因 AI 用量并与 Git 活动关联分析

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L18: `llm-usage-metrics` reads local session data from 17 AI coding tools, on this machine and on others you reach over 
> L84: |Source|Local format|Real logs|

## 星数曲线

```mermaid
xychart-beta
    title "ayagmar/llm-usage-metrics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `de36f4a9bf4f` · [字段定义](../../DATASET.md)*
