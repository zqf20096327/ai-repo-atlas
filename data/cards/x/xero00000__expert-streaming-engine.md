# xero00000/expert-streaming-engine

⭐ 22 · C++ · MIT · 推送 2026-10-26 · [GitHub](https://github.com/xero00000/expert-streaming-engine) · [官网](https://github.com/xero00000/expert-streaming-engine/releases/latest) · 个人维护

**桌面本地 LLM 运行引擎：跨 SSD/RAM/GPU 运行 MoE 大模型**

Expert Streaming Engine (ESE) 提供桌面应用 ESE Studio 与命令行工具，用于浏览、下载 GGUF 模型并本地运行对话。核心机制是 expert streaming：将支持的稀疏模型（MoE）的专家权重保留在 SSD 上，按需在 RAM 与 NVIDIA GPU 显存间流动，从而在显存有限的硬件上运行更大模型；密集模型使用常规放置，CPU-only 包也可用。附带配置扫描器（Config sweeper）实测启动配置并保存验证过的 profile。限制：Windows GPU 推理、AMD/Intel 加速与 macOS 未获本版认证，实验性功能默认禁用，流式以速度为代价。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- expert streaming 将 MoE 专家权重放在 SSD，按需流经 RAM 与 GPU 显存
- ESE Studio 桌面应用：模型库浏览、本地聊天、启动计划与配置扫描
- 读取 GGUF 模型格式，支持本地模型文件夹导入
- 提供 Windows/Linux (CPU 与 CUDA) 安装包及源码构建命令行工具

## 适用场景

- 在显存有限的家用 PC 上运行超过显存容量的 MoE 模型
- 不接触终端，通过桌面应用浏览、下载并本地聊天
- 实测并保存适合自己机器的模型启动配置

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Expert Streaming Engine (ESE) brings local AI to a desktop app. Browse models,
> L23: A large AI model can take more memory than your graphics card has. ESE can keep
> L24: supported models' specialist weights on your SSD and move the parts in use
> L156: ESE is MIT licensed and builds on `ik_llama.cpp` and `llama.cpp`, with their

## 星数曲线

```mermaid
xychart-beta
    title "xero00000/expert-streaming-engine 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-27"]
    y-axis "stars" 19 --> 23
    line [20, 21, 22, 22]
```

2026-10-18 20 → 2026-10-27 22（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `163cd049303e` · [字段定义](../../DATASET.md)*
