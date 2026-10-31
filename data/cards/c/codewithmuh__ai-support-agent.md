# codewithmuh/ai-support-agent

⭐ 14 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/codewithmuh/ai-support-agent) · [官网](https://youtu.be/LW0qd8Ekv34?si=uSVp0bDtClgJ2kDL) · 个人维护

**自托管多渠道 AI 客服系统：接管 WhatsApp/Telegram/邮件/网页聊天工单**

面向需要客服自动化的团队的全栈自托管应用：统一接入 WhatsApp Cloud API、Telegram Bot、Gmail 与网页聊天，用 Claude Haiku 做工单分类与置信度评估、Claude Sonnet 基于知识库生成回答，pgvector 做语义检索；设三层防幻觉护栏与三类人工升级触发（低置信、负面情绪、用户要求）。Django + Next.js 15 技术栈，Docker Compose 编排 4 个容器部署，含多租户团队与坐席仪表盘。回答范围限定于上传的知识库文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四渠道消息统一归一化处理与自动回复
- 双模型分工：Haiku 分类 + Sonnet 生成，回答限定知识库范围
- 三层防幻觉护栏（系统提示/空 RAG 拒答/响应扫描）
- 低置信、负面情绪、要求人工三类自动升级机制

## 适用场景

- 小团队用自托管系统替代人工客服处理常见工单
- 接入 WhatsApp/Telegram/邮件/网页聊天做统一客服
- 坐席在仪表盘处理升级工单并查看 AI 摘要与建议回复

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L26: - **AI classifies** each ticket (billing, technical, account, general) using Claude Haiku
> L28: - **Generates responses** using Claude Sonnet — constrained to your KB only
> L59: 6. **Generate response** → Claude Sonnet answers using KB context only

## 星数曲线

```mermaid
xychart-beta
    title "codewithmuh/ai-support-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6c3d7cd3bd2d` · [字段定义](../../DATASET.md)*
