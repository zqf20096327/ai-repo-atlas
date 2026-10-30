# TuguiDragos/n8n-ai-call-agent

⭐ 17 · NOASSERTION · 推送 2026-08-02 · [GitHub](https://github.com/TuguiDragos/n8n-ai-call-agent) · [官网](https://tuguidragos.gumroad.com/l/n8n-ai-call-agent) · 个人维护

**给销售团队的 n8n 无代码 AI 电话外呼工作流**

由 25 个 n8n 节点组成的可视化工作流模板：通过 Vapi 与 Twilio 拨打潜在客户电话，AI 语音进行对话，从通话转写中用正则提取邮箱（处理 at/dot 等口语表达），并将状态、录音链接、完整转写、AI 摘要与意向标记逐行写入 Google Sheets，每次呼叫（接听与否）均推送 Slack 通知。兼容 n8n v2 引擎，Vapi 节点带错误重试。运行需 n8n、Vapi 账户、Twilio 号码、Google 服务账户与 Slack bot。本仓库为免费/精简版，另有基于 GoHighLevel 的付费完整版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个 n8n 节点的完整外呼-解析-记录流程
- 从语音转写中提取邮箱（处理 at/dot、空格与迟疑）
- 通话结果（状态/录音/转写/AI 摘要/意向）写入 Google Sheets 并推送 Slack
- 4 个 Vapi 节点均带自动重试与错误继续处理

## 适用场景

- 代理机构给本地商家做 AI 电话初筛外呼
- 电商对弃购和未回复工单用户电话跟进
- SaaS 对新注册用户电话确认邮箱并评估意向

## 场景标签

`工作流自动化` `语音 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L14: A no-code AI voice agent that calls your leads, holds a real conversation, pulls their email straight out of what t
> L50: - Calls leads with an AI voice that holds a natural conversation

## 星数曲线

```mermaid
xychart-beta
    title "TuguiDragos/n8n-ai-call-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9af76a8772c1` · [字段定义](../../DATASET.md)*
