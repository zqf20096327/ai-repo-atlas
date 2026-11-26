# xingkaixin/yomitomo

⭐ 14 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/xingkaixin/yomitomo) · [官网](https://yomitomo.app) · 个人维护 · 中文 README

**本地优先的 AI 阅读伴侣桌面应用：标注、问答与本地阅读记忆**

基于 Electron 的本地优先阅读应用，支持导入网页文章、EPUB/AZW3/MOBI 电子书与 PDF，提供高亮、批注、讨论评论、蒸馏笔记、阅读器问答与微信读书同步。AI 部分：用户在 Providers 页配置 base URL、API key 与模型，或经 Ollama 本地推理；@assistant 触发助手回复并引用对应原文；本地多语言嵌入模型索引标注构建可检索的阅读记忆。数据存于本地 SQLite，API key 存系统 keyring。提供 macOS 与 Windows 安装包，项目处于 early alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持网页文章、EPUB/AZW3/MOBI 与 PDF 导入及阅读
- @assistant 助手回复引用原文并可跳转对应段落
- 本地嵌入模型索引标注，构建多语言阅读记忆
- 阅读数据与 API key 本地存储，匿名遥测可关闭

## 适用场景

- 集中管理网页文章、电子书与 PDF 的批注笔记
- 阅读时与 AI 讨论并让回答锚定原文段落
- 在本地检索过去的高亮与判断记录
- 同步微信读书笔记与阅读统计

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: Yomitomo is a local-first AI reading companion desktop app. The Electron desktop app handles web article, EPUB/AZW3/
> L16: - Reading assistants: mention `@assistant` in a discussion, ask an assistant to add a thought under a highlight, or
> L20: - Reading memory: a local multilingual embedding model indexes highlights, thoughts, discussions, and published dis


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c5c21ef4a4e2` · [字段定义](../../DATASET.md)*
