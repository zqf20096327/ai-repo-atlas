# saminkhan1/real-estate-ai-agent

⭐ 33 · Python · GPL-3.0 · 推送 2026-05-21 · [GitHub](https://github.com/saminkhan1/real-estate-ai-agent) · 个人维护

**面向房产中介的全栈 AI 助手：线索接入、房源查询、预约排期**

基于 LangGraph 的全栈房产代理应用：Python 后端编排 main_agent、search_criteria_agent、appointment_agent 等节点，提供房源信息查询（面积/价格/状况）、数据库查找、Google Calendar 预约排期，敏感预约操作前设人工审批环节。前端为 React/TypeScript 的 WebSocket 聊天组件，接入渠道覆盖聊天挂件、短信与电话（Twilio/Retell 数据来自主题标签）。数据来自 Kaggle 房产数据集，需转换为 SQL 后使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 多 agent 图编排（main_agent 路由至查询/预约子流程）
- Google Calendar 预约集成，敏感操作前有人工审批
- 聊天挂件、短信、电话多渠道接入
- React WebSocket 实时聊天组件，可嵌入第三方网站

## 适用场景

- 房产中介承接客户咨询并自动安排看房预约
- 通过网站聊天挂件、短信或电话回答房源问题
- 全天候接收线索并按条件检索房源数据库

## 场景标签

`AI 助手` `语音 Agent` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Realtor AI Assistant is a full-stack LangGraph real estate agent with a Python
> L4: backend and a React chat widget. It coordinates lead intake, property-search
> L5: criteria, database lookup, Google Calendar scheduling, and chat, SMS, and voice

## 星数曲线

```mermaid
xychart-beta
    title "saminkhan1/real-estate-ai-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `80dcc95e89a8` · [字段定义](../../DATASET.md)*
