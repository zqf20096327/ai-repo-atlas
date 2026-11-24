# ZacharyZhang-NY/AemeathCLI

⭐ 18 · TypeScript · MIT · 推送 2026-05-21 · [GitHub](https://github.com/ZacharyZhang-NY/AemeathCLI) · [官网](https://aemeathcli.pages.dev/) · 个人维护

**多模型 CLI 编码工具：在终端编排并行 agent 团队写代码**

基于终端的多模型编码 CLI：内置 9 个模型、5 家提供商（Anthropic/OpenAI/Google/Moonshot，另支持经 Ollama 接入本地模型），按角色（规划/编码/评审/测试等）自动路由模型并支持回退链。提供 swarm 模式：主 agent 分解任务、专职 worker 并行执行，经文件协议共享板协同，可投射到 iTerm2/Windows Terminal/tmux 等原生分屏。支持 OAuth PKCE 登录、密钥链存储与 AES-256-GCM 加密回退、token 成本追踪、YAML 技能扩展与 MCP 服务器接入。需 Node.js≥20 与原生构建工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 模型/5 提供商，含 Ollama 本地模型（可配 base URL）
- 4 步角色路由管线：用户覆盖→角色配置→回退链→系统默认
- swarm agent 团队：hub-and-spoke 编排 + 文件共享板协同 + 原生终端分屏
- MCP 服务器接入（stdio/Streamable HTTP）与 YAML 自定义技能

## 适用场景

- 在一个会话内按任务角色切换不同厂商模型写代码
- 让 agent 团队并行执行规划、编码、评审、测试分工
- 追踪每个模型的 token 成本并设置预算上限

## 场景标签

`编码 Agent` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: AemeathCLI orchestrates **multiple AI models** across **parallel agent teams** in your terminal. Route Claude for p
> L31: - **Multi-model orchestration** -- Use the right model for each task. Claude Opus for architecture, GPT-5.2 for imp
> L161: AemeathCLI ships with 9 models across 5 providers:

## 星数曲线

```mermaid
xychart-beta
    title "ZacharyZhang-NY/AemeathCLI 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-24"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-11-08 18 → 2026-11-24 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `80fad103f7a4` · [字段定义](../../DATASET.md)*
