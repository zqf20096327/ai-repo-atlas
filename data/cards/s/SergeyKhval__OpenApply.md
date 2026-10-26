# SergeyKhval/OpenApply

⭐ 33 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/SergeyKhval/OpenApply) · [官网](https://openapply.app) · 个人维护

**可自托管的开源求职申请追踪器，带 AI 简历评审与求职信生成**

基于 Vue + TypeScript + Firebase 的求职管理 Web 应用：粘贴职位链接追踪投递状态，管理面试与联系人，一键导入职位（链接或 CSV），存储简历。AI 功能通过 Firebase Functions 调用 Gemini API 实现：简历与职位描述匹配度检查、AI 简历评审、定制求职信生成。原托管服务 openapply.app 已关停，代码需自行搭建：需 Node.js 20+、pnpm、Firebase 项目并配置环境变量。

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

- 简历与职位描述匹配度检查
- AI 简历评审与定制求职信生成（Gemini）
- 申请追踪、面试/联系人管理、链接或 CSV 一键导入
- 自托管部署，基于 Firebase（Auth/Firestore/Storage/Functions）

## 适用场景

- 集中追踪我的求职申请进度和面试安排
- 让 AI 帮我针对职位定制简历与求职信
- 不想用闭源 SaaS 追踪器，自托管管理求职数据

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L6: Open, self-hostable, AI-powered job search assistant. Paste a job link, track every application, and get AI resume r
> L13: - AI resume reviews and tailored cover letters

## 星数曲线

```mermaid
xychart-beta
    title "SergeyKhval/OpenApply 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5bbab9774b0a` · [字段定义](../../DATASET.md)*
