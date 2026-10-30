# OpenPawz/openpawz

⭐ 75 · Rust · MIT · 推送 2026-04-17 · [GitHub](https://github.com/OpenPawz/openpawz) · [官网](https://openpawz.ai) · 组织维护 · 中文 README

**离线优先的桌面 AI Agent 平台，本地模型+任意提供商接入**

基于 Tauri v2 与 Rust 后端的原生桌面 AI 平台，可完全离线配合 Ollama 运行，或连接任意 OpenAI 兼容提供商。面向需要私有化 AI Agent 的用户：多 Agent 编排、混合记忆（Engram 知识图谱）、通过内嵌 MCP 桥接 n8n 社区节点生态实现集成。提出三个方法：Librarian 语义工具检索、Foreman 用廉价 worker 模型执行 MCP 调用、Conductor 将流程图编译为优化执行策略。安全上采用 10 层防护（提示注入扫描、沙箱、AES-256-GCM 凭证加密等）。限制：约 5MB 二进制，桌面端形态。

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

- 完全离线运行，配合本地 Ollama worker
- 内嵌 MCP 桥接 n8n 社区节点，集成为 Agent 工具与工作流节点
- Librarian/Foreman/Conductor 三个 Agent 执行优化方法
- 10 层安全防护：提示注入扫描、Docker 沙箱、凭证 AES-256-GCM 加密

## 适用场景

- 在桌面端完全离线运行私有 AI Agent
- 把 n8n 社区集成节点当作对话中的 Agent 工具直接调用
- 以安全沙箱与审批机制运行有副作用的自动化任务

## 场景标签

`AI 助手` `多智能体` `工作流自动化` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: A native desktop AI platform that runs fully offline, connects to any provider, and puts you in control.
> L45: OpenPawz is a native Tauri v2 application with a pure Rust backend engine. It runs fully offline with Ollama, conne

## 星数曲线

```mermaid
xychart-beta
    title "OpenPawz/openpawz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-30 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b3a571f38efa` · [字段定义](../../DATASET.md)*
