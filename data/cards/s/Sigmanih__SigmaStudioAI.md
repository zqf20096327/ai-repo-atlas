# Sigmanih/SigmaStudioAI

⭐ 13 · Python · NOASSERTION · 推送 2026-11-13 · [GitHub](https://github.com/Sigmanih/SigmaStudioAI) · 个人维护

**本地 AI 工作台：统一编排本地与云端模型、Agent 与 MCP 工具**

模块化桌面 AI 工作区，围绕自研 SigmaEngine 推理引擎组织：从 Hugging Face/GGUF 下载模型、流式对话、20 个预定义 Modelfile 角色切换、12 个 MCP 服务器工具执行、GGUF 量化转换、Unsloth QLoRA 微调，以及可按需热加载的扩展模块（文生图、TTS/语音克隆、DAG 流水线、知识图谱、Home Assistant 智能家居桥接）。支持多 GPU CUDA/Apple Metal/CPU RAM 分层分片，自动完成首启环境安装。以 AGPL-3.0 与商业许可双许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地推理引擎 SigmaEngine：多 GPU 层分片、RAM offload、FlashAttention-2、内存 GGUF 量化
- 12 个 MCP 服务器与 AST 沙箱工具执行治理
- 可热加载的模块化扩展（创意、语音、训练、流水线、遥测、家居）
- 自动首启安装：克隆仓库后运行脚本即可，无需手动配置

## 适用场景

- 在统一界面下载、量化并在本机运行开源模型
- 编排多 Agent 流水线并调试 MCP 工具服务器
- 用自己的 GPU 做 QLoRA 微调与硬件基准测试
- 把异构 GPU、内存与树莓派边缘设备组成统一推理运行时

## 场景标签

`推理引擎` `模型量化` `微调` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L36: **Sigma Studio** is a modular AI workspace that turns local hardware into an extensible AI development environment.
> L51: Sigma Studio is engineered around a clean architectural separation between the **workspace orchestrator** and the *
> L62: |**Local models are fragmented**|**Unified model & provider abstraction layer** (seamlessly route between local wei

## 星数曲线

```mermaid
xychart-beta
    title "Sigmanih/SigmaStudioAI 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-20", "2026-11-25"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-11-13 12 → 2026-11-25 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `78f1ce0b2fa7` · [字段定义](../../DATASET.md)*
