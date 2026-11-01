# mkr-infinity/MIRA

⭐ 12 · TypeScript · 推送 2026-06-16 · [GitHub](https://github.com/mkr-infinity/MIRA) · 个人维护

**本地优先的跨平台 AI 桌面助手，支持对话、语音与自动化**

基于 TypeScript/React/Vite/Tauri 构建的跨平台 AI 助手，提供聊天、语音交互（F11 进入语音模式）、图片附件、会话搜索、项目文件夹组织、8 套主题与自定义技能等功能。无遥测、无账号、无云端，API key 在本地配置。初始向导支持选择 OpenAI、Groq 或 Ollama（本地）等提供方。通过 git clone 源码运行，Web 版可在浏览器使用；桌面版需另装 Rust >=1.77 用 npm run tauri:build 构建出 dmg/msi/AppImage，README 未提供预编译安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地优先：无遥测、无账号、无云端，API key 本地配置
- 支持 OpenAI、Groq、Ollama（本地）等提供方切换
- 语音模式、图片附件、会话搜索、8 套主题与自定义技能
- Tauri 桌面构建可产出 macOS/Windows/Linux 三平台包

## 适用场景

- 在本机与多种 AI 提供方对话且不上传数据
- 通过语音和快捷键快速使用 AI 助手
- 按项目组织 AI 会话并自定义助手技能

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: **Your intelligent AI assistant that lives on your machine.**
> L53: 3. **Pick a provider** — the onboarding wizard shows you options like OpenAI, Groq, or Ollama (local)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `68f2e1103067` · [字段定义](../../DATASET.md)*
