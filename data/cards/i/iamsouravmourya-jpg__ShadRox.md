# iamsouravmourya-jpg/ShadRox

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/iamsouravmourya-jpg/ShadRox) · [官网](https://www.shadrox.cyou) · 个人维护

**面向开发者的 Windows 本地 AI 编码工作区：编辑器+BYOK聊天+Agent**

基于 Electron 的桌面应用，将代码编辑器、自带密钥（BYOK）的 AI 聊天与 Agent、项目实时预览、Git 工具、Node 调试器、离线死代码扫描和集成终端集成在同一窗口内。项目文件保留在本地磁盘，仅将用户选择的提示与上下文发送到配置的服务商；应用免费、仅 BYOK、无计费。Windows 提供安装包（需 Google 登录），从源码运行需 Node.js 22.12+ 和 Supabase 项目。当前为 Beta（v0.1.3），README 提示模型生成内容可能出错，需人工审查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BYOK 接入 Gemini、Groq 或任意 OpenAI 兼容端点，支持 Ask/Plan/Agent 模式
- Agent 命令风险分级审批：安全命令自动执行、高危命令需确认
- 捆绑 @vscode/js-debug 调试器与本地死代码扫描器，MCP 与插件扩展
- 实时预览、Git 检查点与 AI 提交信息生成

## 适用场景

- 在单一桌面窗口内完成打开文件夹、编辑、AI 辅助、运行与提交
- 用自己的 API 密钥在本地项目中使用 AI 聊天与 Agent
- 对 Node 项目进行断点调试与离线死代码清理

## 场景标签

`编码 Agent` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L13: ShadRox is a native Electron desktop app that puts a code editor, BYOK AI chat and agent, live project preview, Git
> L20: - **AI chat (BYOK)** — Gemini, Groq, or any OpenAI-compatible endpoint with your own key; Ask/Plan/Agent modes, `@`
> L32: 1. **Download** the installer: ShadRox-v0.1.3-Setup.exe (Windows 10/11, 64-bit). The build is unsigned — if SmartSc


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `fc21611ed603` · [字段定义](../../DATASET.md)*
