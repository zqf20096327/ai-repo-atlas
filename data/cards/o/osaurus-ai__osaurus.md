# osaurus-ai/osaurus

⭐ 8,210 · Swift · MIT · 推送 2026-11-25 · [GitHub](https://github.com/osaurus-ai/osaurus) · [官网](https://osaurus.ai) · 组织维护

**macOS 本地 AI agent 平台：本地/云模型+记忆+工具自主执行**

纯 Swift 编写的开源 agent 运行框架，运行在 Apple Silicon Mac 上，支持完全离线。核心机制是一个 Orchestrator 助手，将请求分派给自带或自定义 agent（各含独立提示词、模型、工具、记忆与工作目录），并支持工作流、定时自动化、分层记忆、Linux VM 沙箱代码执行、浏览器/计算机使用、加密身份与端到端同步。模型可本地（MLX）或云端，切换模型时 agent 与记忆保持不变。需 macOS 15.5+ 与 Apple Silicon；沙箱与 Apple 基础模型需 macOS 26+。

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

- 提供 OpenAI/Responses/Anthropic/Ollama 兼容的本地 API 端点
- 本地模型经 MLX 运行于 Apple Silicon，亦支持多家云端提供商
- 既是 MCP 服务器也是 MCP 客户端
- 隐私过滤器在云端发送前替换设备上的敏感信息

## 适用场景

- 在 Mac 上离线运行自有 agent 与个人记忆
- 通过本地 API 端点接入现有开发工具
- 定时或事件触发的自动化工作流
- 给 MCP 客户端开放本机工具能力

## 场景标签

`工作流自动化` `推理引擎` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6:  Agents, memory, tools, and identity that live on your Mac. Built purely in Swift. Fully offline. Open source.
> L43: You talk to one assistant, the **Orchestrator**. Ask in your own words and it decides how to handle the request:
> L55: - **Agents**: custom agents, each with its own prompt, model, tools, memory, working folder, and avatar. They can r

## 星数曲线

```mermaid
xychart-beta
    title "osaurus-ai/osaurus 星数(近 26 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 8060 --> 8223
    line [8073, 8076, 8078, 8080, 8089, 8093, 8094, 8095, 8099, 8076, 8147, 8157, 8160, 8161, 8162, 8166, 8168, 8173, 8180, 8184, 8188, 8189, 8192, 8205, 8203, 8210]
```

2026-10-24 8,073 → 2026-11-26 8,210（+137）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7f74197bffa6` · [字段定义](../../DATASET.md)*
