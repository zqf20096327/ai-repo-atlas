# Mintplex-Labs/anything-llm-cli

⭐ 33 · TypeScript · 推送 2026-03-05 · [GitHub](https://github.com/Mintplex-Labs/anything-llm-cli) · [官网](https://anythingllm.com) · 组织维护

**终端与 AnythingLLM 实例对话的命令行客户端**

Mintplex-Labs 维护的 CLI 工具，通过 AnythingLLM Developer API 从终端向用户的 Desktop 或 Cloud/Self-Hosted 实例发送 prompt：支持指定或自动创建 workspace、线程管理、附加图片、流式开关；管道输出时自动去除 ANSI 格式，支持带工具的 agent workspace。配置经环境变量（API key、base URL），macOS/Linux 提供交互式 setup 向导，Windows 需手动设置。安装途径含 shell 脚本、npm/yarn 及五平台预编译二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Developer API 与 AnythingLLM 实例交互，支持 Desktop 与 Cloud/Self-Hosted
- workspace 指定/自动创建、线程管理与图片附件
- 管道输出自动剥离 ANSI 格式，支持带工具的 agent workspace
- 提供 macOS/Linux/Windows 预编译二进制与 npm 安装

## 适用场景

- 在终端或脚本中直接调用我的 AnythingLLM 工作区提问
- 把 AnythingLLM 回答接入管道与其他命令行工具组合
- 用 CI 或自动化脚本批量向实例发送 prompt

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A command-line interface for chatting with your AnythingLLM instance from the terminal.
> L45: 1. **Get your API key** from your AnythingLLM instance under **Settings > Developer API**.

## 星数曲线

```mermaid
xychart-beta
    title "Mintplex-Labs/anything-llm-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `17d2e88a046a` · [字段定义](../../DATASET.md)*
