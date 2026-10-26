# Xuxchloris/Alex

⭐ 35 · JavaScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/Xuxchloris/Alex) · [官网](https://github.com/Xuxchloris/Alex#readme) · 个人维护 · 中文 README

**面向外贸获客的自主 Agent：研究买家、管邮箱与 WhatsApp 跟进**

Alex 是构建在 Hermes Agent 执行内核之上的外贸销售 Agent profile：提供外贸身份、28 项领域工具、基于 SQLite 的长期业务记忆与客户/证据存储。用户在对话中交代目标后，Agent 调用真实 Chromium 研究买家、保存证据与任务检查点，并可接入 Gmail 与 WhatsApp（含 Cloud）做受授权外发、幂等发送、退订处理与后台定时跟进。需自行准备已安装的 Hermes、Node.js 24.5+ 与 Chromium。README 声明当前版本 v0.4，生产客户数为 0，真实获客与发送需实际配置验收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 Hermes 内核的 28 项外贸领域工具与长期业务记忆（SQLite + 独立 profile）
- 真实 Chromium 浏览器研究：保存公司、联系方式、来源原文与任务检查点，中断可续
- Gmail/WhatsApp/WhatsApp Cloud 外发：收件人策略、幂等、每日额度、退订处理
- 后台跟进复用 Hermes 原生定时任务，重复安装不重复创建

## 适用场景

- 外贸业务让 Agent 研究目标市场买家并保存证据与来源
- 接入 Gmail 与 WhatsApp 后由 Agent 在授权名单内做客户开发与跟进
- 跨会话延续客户上下文，重启后恢复原任务进度

## 场景标签

`浏览器自动化` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Alex 基于 Hermes Agent 的执行内核，提供独立的外贸身份、行业技能、长期业务记忆、真实浏览器研究和客户沟通工具。你在对话中交代目标，Alex 使用工具执行、保存证据和进度，再根据结果继续工作。
> L21: 研究任务由 Agent 分析条件，调用真实 Chromium 访问网页，保存公司、公开联系方式、来源原文和任务检查点。重复研究复用客户身份；中断后可以继续原任务。
> L23: 接入 Gmail 后，Alex 可以查询邮件、阅读回复并准备开发信。Gmail、WhatsApp 和 WhatsApp Cloud 的外发经过本机收件人策略与通信记录：保存正文、执行发送、记录服务商消息 ID、处理退订，避免不确定

## 星数曲线

```mermaid
xychart-beta
    title "Xuxchloris/Alex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-26 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `98638dc15932` · [字段定义](../../DATASET.md)*
