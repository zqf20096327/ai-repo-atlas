# shashankswe2020-ux/rigspark

⭐ 20 · Rust · MIT · 推送 2026-10-19 · [GitHub](https://github.com/shashankswe2020-ux/rigspark) · [官网](https://www.rigspark.si/) · 个人维护

**硬件感知的本地 LLM 选型与运行工具：判定能否运行并管理服务**

原生 Rust 编写的 CLI/TUI/GUI 工具：检测本机 GPU VRAM 与内存，基于离线策展目录对本地模型给出 yes/slow/no 判定与 tokens/s 估计，支持 recommend、can-run、catalog 等命令，输出确定性、无需网络。判定后可通过 Ollama、llama.cpp、MLX、LM Studio、BitNet 后端拉取、校验并运行模型，提供本地聊天与浏览器工作区，另可编排 ComfyUI 做本地图像/视频生成。面向想在下载权重前确认可行性的本地 LLM 用户；吞吐为估计值而非实测，部分指标标注 unknown。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于检测硬件与离线目录给出 yes/slow/no 判定与 tokens/s 估计
- 支持 Ollama、llama.cpp、MLX、LM Studio、BitNet 后端，含权重完整性校验
- loopback 浏览器工作区与终端 UI，含聊天、agent、MCP 工具
- 通过本地 ComfyUI 编排开源图像/视频模型生成

## 适用场景

- 下载大模型权重前先确认我的机器能不能跑
- 让工具按本机硬件排序推荐合适的本地模型
- 一条命令拉取、校验并启动本地模型进行聊天

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L7:  RigSpark is a hardware-aware native Rust CLI that gives local AI models a
> L110: - **Ollama** — recommended default and managed child process

## 星数曲线

```mermaid
xychart-beta
    title "shashankswe2020-ux/rigspark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f2007b2f3253` · [字段定义](../../DATASET.md)*
