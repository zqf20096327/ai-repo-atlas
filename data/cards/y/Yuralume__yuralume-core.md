# Yuralume/yuralume-core

⭐ 39 · Python · NOASSERTION · 推送 2026-08-28 · [GitHub](https://github.com/Yuralume/yuralume-core) · [官网](https://yuralume.com/) · 个人维护

**自托管 AI 陪伴平台：角色拥有日程、记忆与主动消息**

面向长期 AI 陪伴用户与角色/叙事研究开发者的自托管平台：每个角色拥有 LLM 规划的每日日程、跨会话与跨渠道的五层长期记忆（pgvector 检索）、IG 风格社交动态 LumeGram，以及经三重门控的主动消息；可绑定 Telegram/LINE/Discord/WhatsApp 同一身份。支持按功能/角色路由多 LLM 提供商（BYOK）、用量记账与自托管 NSFW 模式基础。技术栈为 Python 3.13 + Vue 3 + PostgreSQL 16，通过一行脚本拉取 Docker 镜像安装，需自行配置 LLM provider key。状态标注为 alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 规划日程 + 五层结构化长期记忆（pgvector 语义检索）
- 三重门控主动消息与 LumeGram 角色社交动态
- Telegram/LINE/Discord/WhatsApp 跨渠道同一记忆池身份
- 按功能组/功能/角色的多模型路由与生成用量记账

## 适用场景

- 与一两个有日程和记忆的 AI 角色长期相处，且数据留在本机
- 研究 LLM 驱动 NPC 的日程/记忆/主动性脚手架而不从零搭建
- 把静态角色设定变成有日程、会发动态、会主动联系的存在

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  **A self-host AI companion platform where each character has their own life.**
> L22: Yuralume inverts that. Characters here **have a day of their own** — a schedule planned by the LLM, memories that s
> L28: - **Long-term companion users** — you want one or two AI characters you can live with, you care about conversationa

## 星数曲线

```mermaid
xychart-beta
    title "Yuralume/yuralume-core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-31 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `19c12d9b6b97` · [字段定义](../../DATASET.md)*
