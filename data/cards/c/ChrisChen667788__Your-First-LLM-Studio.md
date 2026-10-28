# ChrisChen667788/Your-First-LLM-Studio

⭐ 81 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/ChrisChen667788/Your-First-LLM-Studio) · [官网](https://github.com/ChrisChen667788/Your-First-LLM-Studio) · 个人维护 · 中文 README

**面向 Apple Silicon 的本地优先 LLM 工作台，集成 Agent、对比、微调与评测**

本地优先的 LLM 工作台，运行于 Apple Silicon 并以 MLX 为本地运行时，统一覆盖工具化 Agent 会话、模型/提示词对比（Compare Studio）、数据集与 LoRA 微调、基准评测（含 MATH-500 定量快照与 Math-Verify 评分）、模型发现、检索验证、实验时间线与管理员监控。面向需要对比模型行为、调试运行时、跑评测、准备适配器的使用者。通过统一运行时契约接入 MLX、Ollama、llama.cpp、LocalAI、vLLM、SGLang。注意 README 大量声明证据门控状态：分发为 HOLD、生产为 BLOCKED，多项能力处于预览/待证据阶段；仪表盘数字含标注历史本地证据与示意性动画。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一运行时契约覆盖 MLX/Ollama/llama.cpp/LocalAI/vLLM/SGLang，聊天与 SSE 在 Apple Silicon 通过
- MATH-500 评测快照固定校验、Math-Verify 0.9.0 评分与可复现运行指纹
- 自包含 Apple Silicon 桌面应用（ZIP/DMG 打包、原生 arm64 启动器、签名与公证流程）
- v1.3.x 起加入 MCP 服务器注册与 Ed25519 签名扩展安装、macOS Seatbelt 隔离

## 适用场景

- 在同一工作台内对比本地与远程模型的提示词行为
- 在 Mac 上准备数据集并执行 LoRA 微调与适配器导出
- 运行固定数据集的基准评测并留存可复查证据

## 场景标签

`提示工程` `LLM 可观测性` `模型评测` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L38: First LLM Studio is a local-first LLM workbench for Apple Silicon. It brings local MLX runtimes, remote API targets
> L71: |`v1.2.1` Runtime Fabric|Implements one normalized runtime contract across MLX, Ollama, llama.cpp, LocalAI, vLLM, a
> L30: Latest development batch: v5.8.0-v5.9.4 Activation Operations. Extends verified intake with pinned operational poli

## 星数曲线

```mermaid
xychart-beta
    title "ChrisChen667788/Your-First-LLM-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-28 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `7ef046295aee` · [字段定义](../../DATASET.md)*
