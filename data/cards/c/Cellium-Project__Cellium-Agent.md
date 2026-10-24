# Cellium-Project/Cellium-Agent

⭐ 226 · Python · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/Cellium-Project/Cellium-Agent) · [官网](https://agent.cellium.top) · 组织维护 · 中文 README

**自进化 AI Agent 助手：决策环驱动、失败中学习、多平台接入**

面向终端用户的通用 AI 助手与自扩展 Agent 框架，基于微内核架构（EventBus + DI + BaseTool），支持任意 OpenAI 兼容 API。核心机制是决策环（Control Loop）加贝叶斯 Bandit 的自学习：每轮提取特征、评估规则、选择 action（continue/retry/redirect/compress/terminate）并更新策略。具备三层记忆（人格/会话/长期，FTS5+可选向量）、PEOP 计划-执行-重规划循环、组件热插拔与沙箱隔离、运行时通过自然语言创建新组件。支持 WebUI、QQ、Telegram、飞书、微信接入，提供定时任务与后台事件触发。可选向量检索默认关闭、不依赖外部服务；QQBot 依赖 websockets，飞书需额外安装 lark-oapi。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 决策环 + 贝叶斯 Bandit（Thompson Sampling）实现从失败中学习的自适应决策
- 运行时自扩展：Agent 可通过自然语言创建新组件，3 秒热加载生效，带进程隔离沙箱
- 三层记忆系统：FTS5 全文 + 可选向量检索混合召回，内置敏感信息脱敏与写入拦截
- 多平台接入（WebUI/QQ/Telegram/飞书/微信）与自然语言创建定时任务

## 适用场景

- 需要一个能自己总结失败经验、避免死循环的个人 AI 助手
- 通过 QQ/Telegram/飞书/微信等渠道与 Agent 对话并接收定时任务结果
- 让 Agent 在运行时自己编写新工具组件扩展能力
- 本地部署带记忆和沙箱隔离的自动化任务助手

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L16: **这是一个自进化AI Agent**
> L30: Cellium Agent 是一个通用的 AI 助手，可以帮助你完成各种任务：
> L40: |**多平台接入**|支持 WebUI、QQ、Telegram、飞书、微信等多平台对话|

## 星数曲线

```mermaid
xychart-beta
    title "Cellium-Project/Cellium-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-24 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f66d69589d6b` · [字段定义](../../DATASET.md)*
