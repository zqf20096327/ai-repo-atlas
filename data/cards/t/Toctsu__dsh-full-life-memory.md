# Toctsu/dsh-full-life-memory

⭐ 4 · JavaScript · MIT · 推送 2026-11-13 · [GitHub](https://github.com/Toctsu/dsh-full-life-memory) · [官网](https://www.npmjs.com/package/@tuhengyu/dsh-full-life-memory) · 个人维护 · 中文 README

**给 DSH 用的仿生记忆插件，解决上下文溢出**

一个面向 DeepSeek Harness（DSH）的终身记忆插件：上下文快满时用正则把旧对话蒸馏成关键词、seed_tokens 与摘要，经 DSH 的 surface 节点替换物理切除历史，不留原文、不存向量；需要时通过 recall_from_clues 工具让模型顺着线索重建记忆。折叠过程 0 次模型调用、0 token 计费。数据存本地 SQLite，无网络请求。要求 Node 运行环境，peer 依赖钉定 DSH 0.2.x 区间；通过 DSH 插件管理器 link 安装，另提供 AstrBot 独立插件与 flm CLI 消费同一份线索库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正则蒸馏折叠，0 次模型调用、0 token 计费
- 走 DSH surface 节点替换，物理移除旧对话并降低 KV cache/显存占用
- 群聊按发送者隔离记忆，支持 QQ/微信等多场景覆盖配置
- 本地 SQLite 存储，无网络请求与遥测，零 npm 依赖

## 适用场景

- 长对话会话中自动折叠历史，避免上下文爆窗
- QQ 群机器人按群友隔离记忆，防止串台
- 多个接入入口（桌面/QQ/微信）按场景配置不同记忆策略
- 用 flm CLI 把线索库接入其他平台

## 场景标签

`Agent 记忆` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L17:  一个给 DeepSeek Harness 用的「仿生终身记忆」插件：
> L29: |**🧠 仿生记忆** 不存原文，只存 Token 线索|落盘的只有 `keywords`、`seed_tokens`、一句摘要——没有 message 正文，没有向量，没有 embedding。回忆时用线索组装一段"想起"的提示
> L30: |**⚡ 零 Token 成本** 正则蒸馏，不调模型|遗忘不经过任何 LLM：引号里的原话、文件路径、标识符、中文短语，用规则抽出来就完事。一次折叠 **0 次模型调用、0 token 计费、0 延迟**。|

## 星数曲线

```mermaid
xychart-beta
    title "Toctsu/dsh-full-life-memory 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-01", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-28 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d1960bbc8e4d` · [字段定义](../../DATASET.md)*
