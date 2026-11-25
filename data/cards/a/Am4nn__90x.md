# Am4nn/90x

⭐ 3 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/Am4nn/90x) · [官网](https://90x.amanarya.com) · 个人维护

**面向求职者的 DSA 与系统设计 AI 面试备考应用**

90x 是一个面试备考 PWA：用户选择 30/60/90 天计划后，应用按薄弱领域生成每日任务（新题、到期复习、设计主题等），对用户输入的答案进行 AI 评分，并基于 FSRS 调度间隔复习卡片。内置九个学习轨道的课程库、0-100 就绪度评分、教练聊天（搜索课程库、审阅解答、运行限时模拟面试）与 LeetCode 同步。技术栈为 Next.js + Supabase + Upstash，AI 调用在服务端执行并受管理员设置的用量上限约束。注册账号需管理员审批。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 评分书面答案并按 FSRS 调度间隔复习
- 教练聊天可检索课程库、审阅解答、运行限时模拟面试
- 五领域 0-100 就绪度评分与 90 天打卡网格
- AI 调用服务端执行并记录到用量上限与硬停机制

## 适用场景

- 按 30/60/90 天计划备战 DSA 与系统设计面试
- 用 AI 教练做模拟面试和解答复盘
- 用间隔复习卡片维持知识点记忆

## 场景标签

 · 领域:教育/面试备考

## 证据(README 行号)

> L3:  Interview prep that plans your day and checks your answers.
> L31: **Coach.** A chat that remembers you. It searches the library and cites what it used, finds problems, reviews paste
> L67: |AI|Vercel AI SDK; DeepSeek by default, or Anthropic or any OpenAI-compatible endpoint|

## 星数曲线

```mermaid
xychart-beta
    title "Am4nn/90x 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-23 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `13d1219c84c2` · [字段定义](../../DATASET.md)*
