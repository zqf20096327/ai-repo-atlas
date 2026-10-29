# CreatureChat/creature-chat

⭐ 18 · Java · GPL-3.0 · 推送 2026-01-11 · [GitHub](https://github.com/CreatureChat/creature-chat) · [官网](http://links.creaturechat.com/) · 组织维护

**让 Minecraft 生物用 AI 对话与行动的 Fabric 模组**

面向 Minecraft 玩家的 Fabric/Forge（经 Sinytra Connector）模组：生物通过 LLM 生成对话，可自主做出跟随、逃跑、攻击、保护等行为，并记录好感度、记忆与库存交互；多人模式下对话跨服务器同步。必须配置一个 LLM 才能使用，支持三种接入方式：本地开源模型（经 Ollama/LiteLLM 的 OpenAI 兼容 HTTP 端点，标注难度 Hard 且需强 GPU）、自带 API key（默认 OpenAI gpt-3.5-turbo）、以及在 Discord 购买 token。安装方式为下载 jar 放入 mods 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生物经 LLM 生成对话，并自主执行跟随/逃跑/攻击/保护等行为
- 好感度系统、跨互动记忆与生物库存交互
- 三种 LLM 接入：本地开源模型 / 自带 API key / token 商店
- 对话在多人服务器与玩家间同步

## 适用场景

- 在生存世界里和任何生物聊天、送礼、结交或结仇
- 让生物作为同伴跟随和保护自己
- 和朋友在多人服务器共享生物对话体验

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: ## Chat with any mob in Minecraft! All creatures can talk & react using AI!
> L38: CreatureChat™ **requires** an AI / LLM (large language model) to generate text (characters and chat). There are man

## 星数曲线

```mermaid
xychart-beta
    title "CreatureChat/creature-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7be29c6956fc` · [字段定义](../../DATASET.md)*
