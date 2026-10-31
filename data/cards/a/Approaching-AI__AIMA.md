# Approaching-AI/AIMA

⭐ 17 · Go · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/Approaching-AI/AIMA) · [官网](https://aimaservice.ai) · 组织维护 · 中文 README

**单 Go 二进制管理边缘设备 AI 推理，供 Agent 调用**

面向边缘/本地推理基础设施的管理工具：单个 Go 二进制（零 CGO）自动检测 NVIDIA/AMD/昇腾/海光等八类硬件，从 YAML 知识库解析最优配置，经 K3S/Docker/Native 三种运行时部署 vLLM、llama.cpp、SGLang 推理引擎，并通过 61 个 MCP 工具让 AI Agent 以 JSON-RPC 编程化操控硬件、模型、部署与局域网 Fleet。支持离线优先运行、mDNS 设备发现、内置 Web UI，发布前在真实硬件上执行 UAT 矩阵验证。安装提供预编译二进制、一键脚本与源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 61 个 MCP 工具覆盖硬件/模型/引擎/部署/Fleet/知识等域
- YAML 知识库驱动的 L0→L3 四层决策阶梯，逐层优雅降级
- 八类 GPU/NPU 硬件检测与端到端验证（NVIDIA/AMD/昇腾/海光/MetaX/摩尔线程/Apple/Intel）
- 单二进制零 CGO，跨平台编译 Windows/macOS/Linux，离线优先

## 适用场景

- 在异构边缘设备上自动部署和管理本地 LLM 推理
- 通过 Claude Desktop/Cursor 等 MCP 客户端用 Agent 操控推理基础设施
- 局域网内多设备 Fleet 发现与远程工具执行

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: **AI Inference Managed by AI** — A single Go binary that detects hardware, resolves optimal configs from a YAML kno
> L30: - **61 MCP tools** — full programmatic control for AI Agents over hardware, models, engines, deployments, fleet, an
> L125: AIMA orchestrates three inference runtimes — vLLM (Safetensors), llama.cpp (GGUF), and SGLang (Safetensors) — acro

## 星数曲线

```mermaid
xychart-beta
    title "Approaching-AI/AIMA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `019d2a593ff1` · [字段定义](../../DATASET.md)*
