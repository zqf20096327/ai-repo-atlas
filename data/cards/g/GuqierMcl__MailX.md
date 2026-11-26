# GuqierMcl/MailX

⭐ 27 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/GuqierMcl/MailX) · [官网](https://mailxapp.com) · 个人维护 · 中文 README

**本地优先的 AI 邮件客户端：统一收件箱并整理邮件**

基于 Tauri/Rust 的桌面邮件客户端，将多个邮箱合并为统一收件箱，邮件、草稿与附件存于本地，无云中转与遥测，支持 IMAP/SMTP 账户手动接入。内置 AI 助手可跨账户查找待回复邮件、起草回复与整理收件箱，操作前需确认并引用所用邮件；MailX 本身不带模型，需用户自行添加模型提供方，也支持通过本地 MCP 服务器接入自己的工具。提供 macOS/Windows/Linux 安装包，可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多邮箱统一收件箱，预置 Gmail、Outlook、QQ、163 等服务，其他 IMAP/SMTP 服务器可手动添加
- 内置 AI 助手：查找待回复邮件、起草回复、整理收件箱，操作前询问并引用来源邮件
- 本地优先：无账户、无云中转、无遥测，搜索在本机运行，密码存于系统密钥链
- 内置本地 MCP 服务器（默认关闭），DeepL/Microsoft/Google 翻译可选配置

## 适用场景

- 在单一客户端管理 Gmail、QQ 邮箱、163 等多个账户
- 让 AI 助手扫读全部邮箱并起草回复，人工确认后发送
- 无网络依赖地在本地检索已缓存的邮件内容

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: The local-first, AI-native email client—lightweight, fast, and built to unite all your inboxes effortlessly.
> L20: - **Local first** — Mail, drafts and attachments live on your own computer, so the app opens straight into what it 
> L21: - **AI native** — The built-in assistant works on your mail directly: it finds what needs a reply across every acco


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `67a4c6a62127` · [字段定义](../../DATASET.md)*
