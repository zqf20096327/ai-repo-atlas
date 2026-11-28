# amdnaji/WhatsApp-Agent

⭐ 3 · TypeScript · 推送 2026-11-02 · [GitHub](https://github.com/amdnaji/WhatsApp-Agent) · 个人维护

**可定制的 WhatsApp AI Agent 框架与起步套件**

Kahrman 是一个面向 WhatsApp 的 AI Agent 框架与起步模板：通过 webhook 接入官方 Meta WhatsApp Cloud API，基于 Vercel AI SDK 实现工具调用与对话执行，内置多方言阿拉伯语与英语的自动检测回复。仓库自带一个旅行/酒店助手作为示例，开发者通过修改 persona 文件与工具文件即可适配电商、医疗、餐饮等行业。提供终端 CLI 测试模式，无需先配置 WhatsApp 即可验证 Agent；Node.js + TypeScript + Hono 实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置多方言阿拉伯语（海湾/埃及/黎凡特/MSA）与英语自动检测回复
- 基于 Vercel AI SDK 的工具调用，可在对话中执行后端函数与 API 调用
- 通过单一环境变量切换 Google Gemini、OpenAI、Anthropic Claude
- 直连 Meta WhatsApp Business Cloud API，附带完整接入配置步骤

## 适用场景

- 为自己的业务搭建 WhatsApp 客服或预订机器人
- 搭建支持阿拉伯语方言的用户对话助手
- 在终端 CLI 中先行调试 Agent 人设与工具调用再接入 WhatsApp

## 场景标签

`聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2: ### Customizable AI WhatsApp Agent Framework & Starter Kit
> L8: **Kahrman (كهرمان)** is a flexible, plug-and-play **AI Agent Framework for WhatsApp**, designed with first-class sup
> L44: - 🛠️ **Tool Calling & Live Actions:** Built on the Vercel AI SDK to seamlessly execute backend functions, API calls


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9e855e174e3a` · [字段定义](../../DATASET.md)*
