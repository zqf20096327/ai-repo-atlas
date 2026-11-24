# AiXenix/AiXenix-Telegram-Scraper-AI

⭐ 4 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI) · [官网](https://aixenix.com) · 个人维护 · 中文 README

**Telegram 频道的 AI 新闻编辑台：采集、去重、按批准发布**

面向 Telegram 频道主的内容服务：每数分钟读取公开频道的网页预览，做年龄/空帖/广告等本地初筛，再由过滤模型判定重复新闻点；新事件先推送原文供拒绝，随后由写作模型按风格指南与频道近帖起草贴文，经用户在 bot 中按下 Publish 才发布。可作 bb 插件（含管理页）或单文件 Node.js 脚本运行；完整媒体需可选接入 Telegram 用户账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重复判定由过滤模型完成，初筛阶段不调用模型
- 起草使用风格指南加频道近六帖作为范例，保留源链接与事实
- 所有发布需用户在 bot 中批准，支持 Publish/Reject/换一稿/编辑
- 两种运行方式：bb 插件（含管理页）或单文件 standalone 脚本

## 适用场景

- 为 Telegram 频道自动收集新闻草稿并由我逐条批准发布
- 监控多个公开频道并过滤重复报道
- 让草稿保持我频道已有的写作风格与署名

## 场景标签

`网页抓取` `AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **An AI news desk for your Telegram channel.**
> L48: 3. **Repeat check.** Up to 10 posts at a time go to the filter model together with the titles of recent stories (pu
> L50: 5. **Draft.** The writer model gets your style guide, up to six recent posts of your channel as examples and up to 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `d08a7b6994f7` · [字段定义](../../DATASET.md)*
