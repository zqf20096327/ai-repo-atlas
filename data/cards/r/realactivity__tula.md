# realactivity/tula

⭐ 47 · TypeScript · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/realactivity/tula) · 组织维护

**自托管个人健康 AI 助手的 OpenClaw 技能层**

RealActivity 维护的开源（Apache-2.0）项目，基于 OpenClaw 构建：提供 8 个健康类 agent 技能（SMART on FHIR 拉取病历、医疗 PDF 解析、门户消息起草、纵向记忆比对、就诊准备包等）、自托管 Wren 病历中继、检查入钱包（通过 SMART Testing EHR 全部三项 Connectathon 场景）及 78 任务的评估标准。面向个人、照护者与开发者，数据保留在用户自托管工作区。声明非医疗设备、非临床决策支持。商业版 My Aria/Aria 由同公司另行运营，属开放核心模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SMART on FHIR 拉取病历，Wren 中继可自托管无第三方依赖
- 8 个 Apache-2.0 技能 + 78 任务的患者 Agent 评估标准 v0.1（Microsoft Waza CI 门控）
- 检查入钱包通过 SMART Testing EHR 全部三项 Connectathon 最低场景
- 模型路由支持多家后端（含开源权重模型），PHH 限定于工作区内、门户消息仅起草不自动发送

## 适用场景

- 个人/照护者整合病历、化验单、门户消息到私有 AI 工作区
- 生成日常健康摘要与就诊前准备材料
- 起草给医疗团队的门户消息（人工确认后发送）

## 场景标签

`AI 助手` `文档解析` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: Tula is an open-source personal health agent skill layer built on OpenClaw. It helps individuals, caregivers, and h
> L82: Tula is a health-focused skill layer for OpenClaw. It provides reusable agent skills, configuration patterns, evalu
> L151: Tula runs on a single self-hosted VM. The OpenClaw gateway routes user input (Telegram, email, future voice) into 

## 星数曲线

```mermaid
xychart-beta
    title "realactivity/tula 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-28 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `22f35747b4d2` · [字段定义](../../DATASET.md)*
