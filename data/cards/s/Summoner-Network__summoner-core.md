# Summoner-Network/summoner-core

⭐ 15 · Python · Apache-2.0 · 推送 2026-07-07 · [GitHub](https://github.com/Summoner-Network/summoner-core) · 组织维护

**构建与协调自主 agent 的 SDK 运行时（Python+Rust）**

Summoner 协议的核心 SDK，提供构建和协调自主 agent 所需的钩子、通信层与执行模型，支持去中心化身份、声誉感知消息传递、可编程自动化与编排。安装需 Python 3.9+ 与 Rust 工具链，通过 setup.sh 脚本创建虚拟环境、生成 .env 配置并编译 Rust 服务端；SDK 以 Python 包形式安装，提供 open_server.sh / open_client.sh 冒烟测试脚本。代码贡献仅限内部团队，外部开发者可提 issue 或基于 SDK 模板仓库扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 hooks、通信层与执行模型的 agent 运行时
- Rust 服务端与 Python SDK（editable 安装）组合
- setup.sh 一键配置环境并编译可选前缀的 Rust 服务器
- 附 open_server.sh / open_client.sh 冒烟测试脚本

## 适用场景

- 基于 Summoner 协议构建自主 agent 应用
- 搭建带通信层的服务端与客户端进行消息收发测试
- 开发兼容 Summoner 协议的扩展模块

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > The **Summoner Core SDK** is the foundation of the Summoner protocol, providing a minimal, composable runtime for 
> L5: This core SDK exposes the **hooks**, **communication layer**, and **execution model** needed to support decentralize

## 星数曲线

```mermaid
xychart-beta
    title "Summoner-Network/summoner-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `edfd70636573` · [字段定义](../../DATASET.md)*
