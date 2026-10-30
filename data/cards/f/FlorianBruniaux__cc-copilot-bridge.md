# FlorianBruniaux/cc-copilot-bridge

⭐ 61 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/FlorianBruniaux/cc-copilot-bridge) · [官网](https://ccbridge.bruniaux.com/) · 个人维护

**给 Claude Code 用户的 Bash 多后端切换路由器**

一个 Bash 脚本工具，为 Claude Code CLI 提供三后端路由：通过 ccd/ccc/cco 别名在 Anthropic Direct API、GitHub Copilot（经 copilot-api 代理消耗 premium 配额）与 Ollama 本地离线推理之间切换，覆盖 40+ 模型。附 MCP 兼容性 profile 自动生成、GPT 模型身份注入、健康检查与会话日志。面向已有 Copilot 订阅或需离线跑 Claude Code 的开发者；Copilot 路径需订阅与本地 copilot-api，Ollama 路径需自配 64K 上下文 Modelfile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ccd/ccc/cco 三别名在 Anthropic/Copilot/Ollama 间即时切换
- Copilot 路径经 copilot-api 代理访问 Claude/GPT/Gemini 15+ 模型
- Ollama 离线路由（Apple Silicon 优化，需 64K 上下文配置）
- MCP 兼容 profile 自动生成与模型身份注入

## 适用场景

- 用已有 Copilot 订阅跑 Claude Code 日常开发
- 离线/涉密代码场景用 Ollama 本地模型编码
- 按任务在付费与免费模型间快速切换控制成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **TL;DR**: Bash script that routes Claude Code CLI through multiple AI providers. Switch between Anthropic Direct 
> L32: A **multi-provider router** for Claude Code CLI that lets you switch between AI backends with simple aliases.

## 星数曲线

```mermaid
xychart-beta
    title "FlorianBruniaux/cc-copilot-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-30 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `39dcf24943b9` · [字段定义](../../DATASET.md)*
