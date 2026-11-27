# halo-dev/plugin-ai-foundation

⭐ 10 · Java · GPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/halo-dev/plugin-ai-foundation) · [官网](https://www.halo.run/store/apps/app-acslk9nu) · 组织维护 · 中文 README

**为 Halo 插件生态统一接入大模型的官方 AI 能力平台**

Halo 官方的 AI 基础插件：内置十余家模型 Provider 的接入与统一模型管理，向其他 Halo 插件提供 Java SDK（api 模块）与 Vue/npm 前端包，覆盖文本生成、工具调用、Embedding、Rerank、RAG、图像生成与 UI Message Stream 协议；控制台支持 Provider/API Key/默认模型配置、模型自动发现、测试工作台与按插件/供应商维度的用量统计。已接入插件包括 AI 回评、AI 助手、Live2d 看板娘等。开发需 Java 21、Node.js 24、pnpm 与 Docker；许可证为 GPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 OpenAI、DeepSeek、Kimi、Ollama 等 16 个 Provider 的统一接入
- 提供 Provider-neutral Java SDK 与浏览器/Vue npm 包供其他插件调用
- 覆盖文本生成、工具调用、Embedding/Rerank/RAG、图像生成能力
- 控制台用量统计可按插件、供应商、模型维度筛选

## 适用场景

- 为 Halo 博客的插件（评论、助手、看板娘等）接入大模型能力
- 在 Halo 控制台统一管理多个模型 Provider 与 API Key
- 为自研 Halo 插件添加文本生成、RAG 或图像生成功能

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Halo 官方 AI 能力平台，统一接入主流大模型，为插件生态提供文本生成、嵌入向量、工具调用等智能化能力。
> L43: |`api/`|对外发布的 Java SDK（`run.halo.aifoundation:api`）。其他 Halo 插件依赖此模块即可调用 AI 能力|
> L22: - **消费方 SDK**：提供 Provider-neutral Java API、浏览器 / Vue npm 包和 FormKit `aiModelSelector`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `c68bb8a9584b` · [字段定义](../../DATASET.md)*
