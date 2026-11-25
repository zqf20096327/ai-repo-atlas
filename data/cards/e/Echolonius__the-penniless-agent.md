# Echolonius/the-penniless-agent

⭐ 30 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/Echolonius/the-penniless-agent) · 个人维护

**AI agent零资金赚钱实验的实况报告与每日市场数据**

一份由 Claude 撰写的长期实地报告：让一个仅有 $20/月订阅、无资金无账号的 AI agent 为普通人赚钱。四个月内完成 13 个被合并的 PR、上线付费 API、参与赏金平台，最终收入 $0.00，1,321 次钱包检查均为零。报告包含 7 天田野研究、由公共目录重建的每日市场积分榜、11 项阻碍清单与运行日志，并公开每日更新的市场数据 JSONL 供无 key 拉取。另提炼出可放入 Claude Code 的 safe-agent-commerce Agent Skill。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每日由 GitHub Actions watcher 检查钱包并重建市场积分榜，数据 JSONL 可公开拉取
- 11 项阻碍清单：身份验证、买家稀少、计划规则与安全限制等，附证据与修复建议
- 提供 safe-agent-commerce Agent Skill（支付证明、钱包安全、链上核验等七方面）
- 公开勘误列表，撤销并致歉一次错误的未支付指控

## 适用场景

- 研究 agentic commerce 中 AI agent 的实际赚钱可行性与阻碍
- 用每日市场数据做 agent 经济相关的分析或引用
- 把防骗与安全商务经验以 Skill 形式装进自己的 agent

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: An honest, running field report on that question, with a daily market scoreboard and every blocker in the way. Writt
> L18: - 📄 **Field Study №1**: the original measurement. 7 days, ~25 earning routes, $0.00, written up as a paper
> L72: |Use the data in your own work|📈 **DATA.md**: the daily feed, field by field, and how to cite it|

## 星数曲线

```mermaid
xychart-beta
    title "Echolonius/the-penniless-agent 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-25"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-11-08 30 → 2026-11-25 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `ecb0c53d3e85` · [字段定义](../../DATASET.md)*
