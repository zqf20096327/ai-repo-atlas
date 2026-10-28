# vitorfdl/narratrix

⭐ 91 · TypeScript · AGPL-3.0 · 推送 2026-09-28 · [GitHub](https://github.com/vitorfdl/narratrix) · [官网](https://narratrixai.com) · 个人维护

**桌面端 AI 辅助跑团与角色扮演应用：角色卡、设定集与可定制提示词**

基于 Tauri（React/TypeScript/Rust/SQLite）的桌面应用，面向跑团与角色扮演玩家：可自定义聊天看板小部件、角色卡与属性表（内置 D&D 5E 模板、计算字段）、Lorebook 设定集（关键词/相似度检索注入上下文）、AI 工具调用（掷骰、读写属性表）与节点编辑器自定义 Agent 自动化。模型连接由用户自选（OpenAI/Anthropic/Gemini/OpenRouter/Bedrock/Ollama 或 OpenAI 兼容端点），数据本地存储、API key 加密。支持导入 SillyTavern 预设与角色卡。提供 Windows/macOS/Linux 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽式聊天看板小部件布局，可保存会话布局
- Lorebook 按关键词或相似度选条目注入模型上下文，含测试对话框
- 节点编辑器构建 Agent：JavaScript、提示词、掷骰、设定搜索等可组合
- 支持导入 SillyTavern 预设与角色卡；本地存储、API key 加密

## 适用场景

- 跑团时把角色表、世界观笔记和 AI 对话放在同一界面管理
- 为角色扮演对话配置自定义提示词模板与自动掷骰
- 用本地或自选云端模型进行桌面端角色扮演，数据留在本机

## 场景标签

`提示工程` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L15: NarratrixAI is a desktop app for AI-assisted roleplay and tabletop campaigns. Create characters, keep track of thei
> L74: Connect to OpenAI, Anthropic, Google Gemini, OpenRouter, AWS Bedrock, Ollama, or an OpenAI-compatible endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "vitorfdl/narratrix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-28 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `3024a16da27d` · [字段定义](../../DATASET.md)*
