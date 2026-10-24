# liruifengv/amon-agent

⭐ 181 · TypeScript · AGPL-3.0 · 推送 2026-04-25 · [GitHub](https://github.com/liruifengv/amon-agent) · 个人维护 · 中文 README

**运行在桌面上的 AI 协作助手，帮你写代码执行命令**

基于 Electron + React + TypeScript 的本地桌面 AI 协作应用（AI coworker）：支持思考过程与工具调用、文件 diff 展示、图片消息、多工作区管理。采用自研三层 agent 架构：provider 无关的 AI 流式层（内置 Anthropic Claude、OpenAI、Google Gemini 及 API 兼容提供方如 GLM、MiniMax、Kimi）、框架无关的双循环 agent 核心、Electron 集成层。0.3.0 起移除 Claude Agent SDK，运行时自研。安装包从 Releases 下载，macOS 需手动去除隔离属性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 provider 无关流式层，内置 Anthropic/OpenAI/Google 及 API 兼容提供方
- 双层循环 agent 架构：LLM 调用→工具执行→转向检查
- 多工作区管理、文件 diff、图片消息、暗色主题
- 0.3.0 起不再依赖 Claude Agent SDK，运行时仓库内自研

## 适用场景

- 在桌面本地用 AI 帮我写代码、执行命令、管理文件
- 在同一应用里切换多家 LLM 提供方
- 按项目文件夹建立多个工作区进行 AI 会话

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L15: Amon is an intelligent AI coworker that runs locally on your desktop. It doesn't just chat with you — it actually h
> L17: Amon features a custom three-layer agent architecture with a provider-agnostic AI streaming layer, supporting multi

## 星数曲线

```mermaid
xychart-beta
    title "liruifengv/amon-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 180 --> 182
    line [181, 181]
```

2026-10-18 181 → 2026-10-24 181（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3a8c6e2b232e` · [字段定义](../../DATASET.md)*
