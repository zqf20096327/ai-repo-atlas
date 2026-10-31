# 0ffy/beenote

⭐ 42 · TypeScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/0ffy/beenote) · [官网](https://beenote-ai.netlify.app) · 个人维护

**面向语言学习的全栈笔记 Web 应用，集成 ChatGPT 写作**

基于 Next.js 13 app 目录构建的语言学习 CRUD Web 应用，后端用 PocketBase 提供数据库与用户认证，富文本编辑基于 Tiptap，支持音频录制与文件上传，邮件经 AWS SES 发送，AI 部分为调用 ChatGPT（gpt-3.5-turbo）进行 AI 写作辅助。项目同时作为 Next.js、DaisyUI、PocketBase 等开源库的示例展示，README 未给出安装运行步骤，TODO 列出 OAuth2 登录、拖拽排序等待实现功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PocketBase 提供数据库与用户认证
- Tiptap 富文本编辑器
- 音频录制与文件上传
- ChatGPT 用于 AI 写作

## 适用场景

- 语言学习时记录词汇与笔记并获 AI 写作辅助
- 参考 Next.js 13 + PocketBase 全栈实现的示例项目

## 场景标签

`知识库管理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L1: # BeeNote - Full stack CRUD web application built with Next.js
> L5: BeeNote is a web application for language learning, showcasing several open source web dev libraries including Next.
> L16: - ChatGPT for AI writing.

## 星数曲线

```mermaid
xychart-beta
    title "0ffy/beenote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f2d12eaf2aad` · [字段定义](../../DATASET.md)*
