# perrycan/wechat-daily-report-bot

⭐ 28 · Python · MIT · 推送 2026-06-06 · [GitHub](https://github.com/perrycan/wechat-daily-report-bot) · 个人维护 · 中文 README

**微信群日报接龙自动化机器人：点名、催交、LLM 汇总**

面向固定工作群的日报收集自动化工具：定时发起微信原生“接龙”、合并多条 @ 催交未提交者（排除主管/机器人/请假人员）、再由 LLM 按外部可热重载的规则文件将条目汇总成管理层报告私发给主管。基于 wxauto/wxautox4 的 GUI 自动化，Python + FastAPI 提供 HTTP API，支持定时器、CLI、Telegram 经 OpenClaw 远程三种触发方式。匿名化为作品集版本，自述 RPA 自动化即时通讯客户端可能与平台服务条款冲突。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 驱动微信原生接龙流程，保留自动编号与名单
- LLM 汇总规则外置热重载，改规则无需重启
- 模型回退链 gpt-5.4 → gpt-5.4-mini → deepseek-chat-v3
- 定时器 / HTTP API / CLI / Telegram+OpenClaw 四种触发路径，含 DRY-RUN 模式

## 适用场景

- 每天自动在工作群发起日报接龙并催交未交成员
- 把群内日报条目自动汇总成报告私发给主管
- 出差/放假时通过 Telegram 远程触发汇总或补催

## 场景标签

`GUI 自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L3: > Automated daily work-report collection for a WeChat work group — **post the roll-call → chase non-submitters → AI-
> L38: - 🧠 **LLM summary with hot-reloadable rules** — the summarization prompt lives in an external rules file that is **

## 星数曲线

```mermaid
xychart-beta
    title "perrycan/wechat-daily-report-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a711c191ed25` · [字段定义](../../DATASET.md)*
