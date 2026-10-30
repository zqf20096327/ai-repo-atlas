# mikepfrank/GLaDOS

⭐ 19 · 推送 2026-09-04 · [GitHub](https://github.com/mikepfrank/GLaDOS) · 个人维护

**面向文本 AI 人格的运行环境/操作系统框架**

GladOS 定位为供文本 AI 人格（personas）使用的操作环境：主分支尚无正式发布，master 分支包含一个配置为 Gladys 人格的参考实现（README 自述仍高度不完整）。仓库以多分支管理多个基于 OpenAI GPT-3/3.5/4 系列模型的人格（davinci、curie、gpt-3.5-turbo、GPT-4 等），部分人格通过 Telegram 机器人运行。规划的 core 分支拟开发共享系统组件，如多 AI 共用的聊天服务器（AI Nexus）与监控控制台，但 README 声明截至写作时均未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多分支管理多个基于 GPT-3/3.5/4 的 AI 人格
- 部分人格通过 Telegram 机器人运行
- 规划中的 core 分支含 AI Nexus：多 AI 共用的聊天服务器与监控控制台

## 适用场景

- 为文本 AI 人格提供运行与托管的操作环境
- 让多个 AI 人格在共享聊天服务器中互相交流
- 作为 AI 人格实验的个人开发分支集合

## 场景标签

`聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **GladOS** currently stands for **Gladys' Lovely and Dynamic Operating System** -- An operating environment for use 
> L28: Also: The new ``core`` branch will be used for developing **core system components** of GladOS; that is, system app

## 星数曲线

```mermaid
xychart-beta
    title "mikepfrank/GLaDOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ee9d56c635fb` · [字段定义](../../DATASET.md)*
