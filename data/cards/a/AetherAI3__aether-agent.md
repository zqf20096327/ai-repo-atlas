# AetherAI3/aether-agent

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/AetherAI3/aether-agent) · [官网](https://aethersystems.net/) · 组织维护

**终端编码代理：读取仓库、改代码、跑检查，支持本地 Ollama**

开源终端编码代理 CLI（npm/PyPI 安装），读取仓库后执行代码修改、Git 操作并运行测试等检查，记录真实退出码；支持托管账号模型或本地 Ollama 端点推理（无需账号，默认 loopback）。内置对话与 shell 混合控制台（!命令、/shell-result 附件编辑与脱敏）、MCP 服务器与技能接入、会话恢复、变更审查、远程只读观看（aether rc）。附带你账号托管 agent 与 ATS 交易适配器工作区（声明不含自动实盘下单）。要求 Node.js 24+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编码任务带真实退出码的检查验证与计划模式（只读工具）
- 本地 Ollama 端点推理，无需 Aether 账号
- !shell 命令零模型调用，/shell-result 支持编辑/脱敏后发送
- MCP 服务器、agent 技能与本地预览接入

## 适用场景

- 在终端里让 agent 修复失败测试并验证
- 本地 Ollama 模型完成编码任务，推理不出本机
- 审查 agent 改动并准备分支与 PR

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: An open-source coding agent that reads your repository, makes changes, and runs your checks.
> L28: |**Choose your model**|Hosted account models or local Ollama with no account required. Model setup ↓|

## 星数曲线

```mermaid
xychart-beta
    title "AetherAI3/aether-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `66e029101c5c` · [字段定义](../../DATASET.md)*
