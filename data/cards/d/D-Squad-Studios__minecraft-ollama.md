# D-Squad-Studios/minecraft-ollama

⭐ 10 · Java · GPL-3.0 · 推送 2026-08-26 · [GitHub](https://github.com/D-Squad-Studios/minecraft-ollama) · 组织维护

**Minecraft 模组：通过 Ollama 与村民对话并观察游戏世界**

一个 Minecraft Forge 模组，接入本地运行的 Ollama 服务，让玩家与村民对话，并计划实现观察世界的 Overseer 角色：读取村庄、村民与世界事件上下文（如袭击、铁傀儡建造）提供给玩家。技术栈为 Java 21/JDK、Git、Gradle，需先 git clone 源码并运行提取脚本与向量库种子步骤构建 Minecraft 知识库。限制：对话可能仅限于有职业的村民；上下文长度需按机器性能调整，推荐 16,000 token 以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过交易界面的 Chat 按钮与村民对话
- 计划读取世界事件/村庄/村民上下文作为对话素材
- 基于 minecraft-data 构建知识库并向量库种子（nomic-embed-text 嵌入）
- 支持 Ollama 云端模型（如 minimax-m2.5:cloud）与本地模型混用

## 适用场景

- 在游戏内与村民进行自然语言对话
- 让 AI 基于村庄状态与世界事件提供背景信息
- 本地 Ollama 环境下的 Minecraft AI 伴游体验

## 场景标签

`聊天机器人` `AI 助手` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L8: It would be awesome to implement Ollama into Minecraft as a Mod/Plugin where you can talk to villagers and have a mo
> L10: * [ ] Implement Ollama into minecraft to interact with the player (kind of like an AI pal)

## 星数曲线

```mermaid
xychart-beta
    title "D-Squad-Studios/minecraft-ollama 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `0b8375d95e1a` · [字段定义](../../DATASET.md)*
