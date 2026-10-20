# botpress/botpress

⭐ 14,957 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/botpress/botpress) · [官网](https://botpress.com) · 组织维护

**面向开发者的开源聊天机器人/Agent 构建与部署平台**

Botpress Cloud 的主仓库，包含 Botpress Hub 的公开集成、开发者工具（CLI、SDK、API Client）以及仅用 SDK 和 CLI 编写的 "as code" 机器人示例。开发者可通过 npm/yarn/pnpm 安装 @botpress/cli，用 bp init 从模板生成集成，修改 integration.definition.ts 与 src/index.ts 后用 bp deploy 部署到工作区，并可设为公开分享到 Hub。所有包以 MIT 许可开源。README 明确说明 bots-as-code 不是官方推荐方式，Studio 才是主要构建途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 4.5 天,年发版 0,75 位贡献者
- 涨星:近 1 天 **+1**(自 20261016 起算)
- 安装:npm 包 `@botpress/cli` 月下载 40,712

## 能力要点

- 提供 @botpress/cli、@botpress/client、@botpress/sdk 三类开发者工具包
- bp init 从模板生成集成，bp deploy 部署并支持公开可见性
- 包含 Botpress Hub 全部公开集成与 as-code 机器人示例
- 全部包以 MIT 许可开源

## 适用场景

- 为 Botpress Hub 开发并发布自己的集成
- 用 SDK 和 CLI 以代码方式程序化构建机器人
- 基于 OpenAI 驱动的能力搭建业务聊天助手

## 场景标签

`Agent 框架` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L9: Botpress is the ultimate platform for building **next-generation chatbots** and assistants powered by OpenAI. Start 
> L21: - **Integrations** – all public integrations on the Botpress Hub maintained by Botpress
> L22: - **Devtools** – all Botpress Cloud dev tools (CLI, SDK, API Client)

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `6865db38ddf6` · [字段定义](../../DATASET.md)*
