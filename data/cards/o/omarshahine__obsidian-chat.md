# omarshahine/obsidian-chat

⭐ 13 · TypeScript · 推送 2026-10-25 · [GitHub](https://github.com/omarshahine/obsidian-chat) · 个人维护

**Obsidian 的极简 AI 聊天插件：双供应商，支持移动端**

面向 Obsidian 用户的 agentic AI 聊天插件，仅支持 Anthropic 与 OpenAI 两个供应商，配置只需选择供应商并填入 API key（存于系统钥匙串，不同步）。AI 通过 14 个映射 Vault API 的工具读取、编辑、创建、重命名笔记及查询反链等。移动端为一等公民：无流式输出（requestUrl 限制）、无 vault 索引、右侧滑入边栏。支持选区限定上下文、多会话（保留最近 20 个）、会话历史本地持久化。安装经 BRAT 或手动复制文件，开发需自行构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅两个供应商：Anthropic（Claude Sonnet 4.6）与 OpenAI（Codex 5.3）
- 14 个映射 Obsidian Vault API 的工具（读写/搜索/重命名/反链等）
- 移动端优先设计：无流式、无 vault 索引、右侧滑入边栏
- API key 存于 OS 钥匙串（SecretStorage），不同步；会话本地存储于 chat-state.json

## 适用场景

- 在 Obsidian 中通过对话让 AI 读取并编辑笔记
- 移动端上与自己的知识库对话
- 针对选中文字范围让 AI 做限定修改

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: An agentic AI chat plugin for Obsidian. Two providers, best models, no bloat.
> L9: Existing AI plugins for Obsidian are overcomplicated, break on mobile, or require a dozen settings to configure. Obs
> L24: The chat assistant has 14 tools that map directly to Obsidian's Vault API:

## 星数曲线

```mermaid
xychart-beta
    title "omarshahine/obsidian-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2bd4bacd4566` · [字段定义](../../DATASET.md)*
