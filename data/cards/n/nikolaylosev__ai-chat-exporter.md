# nikolaylosev/ai-chat-exporter

⭐ 3 · TypeScript · MIT · 推送 2026-11-10 · [GitHub](https://github.com/nikolaylosev/ai-chat-exporter) · 个人维护

**把 Claude/Gemini/Grok/ChatGPT/DeepSeek 对话导出为 Markdown 的浏览器扩展**

Chrome 扩展，通过各平台网页版自身的内部接口读取会话，将对话连同上传与模型生成的文件导出到本地：支持 Markdown（含 YAML frontmatter）、HTML、JSON、docx 格式，支持单条、批量（搜索/日期过滤/勾选）、项目与 Gemini 笔记本导出，输出目录可直接作为 Obsidian vault 使用。内置本地归档全文搜索。声明为非官方独立项目，依赖未文档化内部接口，平台变更可能使其失效；无服务器、无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 导出对话为 Markdown/HTML/JSON/docx，附件保留原格式
- 支持单条、批量、项目与 Gemini 笔记本导出
- 内置本地归档搜索（多语言词形、短语、多过滤条件）
- 无服务器、无遥测，数据全部留在本机

## 适用场景

- 把各家 AI 对话归档进 Obsidian 笔记库
- 定期备份 Claude/ChatGPT 等平台的全部聊天记录
- 本地全文检索历史 AI 对话与附件

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L9: A Chrome extension that saves your conversations from **claude.ai**, **gemini.google.com**, **grok.com**, **chatgpt.
> L34: - Everything stays on your computer. The extension has no server, no analytics and no telemetry.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `3e6486a9327b` · [字段定义](../../DATASET.md)*
