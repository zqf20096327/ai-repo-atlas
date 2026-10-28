# savannah-i-g/HyperCat-Agent

⭐ 53 · C++ · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/savannah-i-g/HyperCat-Agent) · 个人维护

**给桌面用户的本地多 agent 协作工作台（C/C++ 编写）**

运行在 Linux x86-64 桌面上的独立多 agent 工作区应用：一个“指挥者”负责对话，真实任务到来时派出多个 worker agent 并行执行并汇报实际结果。模型侧通过 OpenRouter 兼容的 API key 接入（环境变量或 OS 钥匙串），可经 HC_MODEL 指定模型。界面含聊天、Fleet、被监禁的文件工作区、跨会话语义记忆、可观测性面板与工具管理；用户可用 C/C++/Python/Rust 编写扩展工具，运行在受限进程中。所有触及机器的操作经过审批门。自称 0.1.2 预发布测试版，未硬化用于生产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 指挥者+worker 舰队的多 agent 并行执行模式，汇报真实结果含失败项
- 所有触及机器的操作经审批门；文件系统监禁、网络与外部程序默认拒绝+白名单
- 支持 C/C++/Python/Rust 编写工具，各自运行在受限进程并通过行协议通信
- 跨会话语义记忆与按项目隔离的文件/会话/记忆

## 适用场景

- 在桌面本地与多 agent 舰队协作完成实际工作
- 为 agent 编写并安全运行自定义工具
- 在隔离工作区内让 agent 处理项目文件并跟踪 token 花费

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L13: You talk to me the way you'd talk to a sharp colleague who is good company and tells you the truth. Most of the tim
> L18: - An API key for an OpenRouter-compatible model provider. I run on your own machine and reach out only to the
> L53: Launch `hypercat` and you land in a blank chat with me, the conductor. Talk to me the way the README describes:

## 星数曲线

```mermaid
xychart-beta
    title "savannah-i-g/HyperCat-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b266ac2f310d` · [字段定义](../../DATASET.md)*
