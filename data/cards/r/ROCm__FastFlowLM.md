# ROCm/FastFlowLM

⭐ 2,079 · C++ · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/ROCm/FastFlowLM) · [官网](http://fastflowlm.com/) · 组织维护 · 中文 README

**在 AMD Ryzen AI NPU 上本地运行 LLM 的轻量运行时**

面向 AMD Ryzen AI 系列（XDNA2 NPU）芯片的本地模型运行时，提供单命令 CLI（flm run/serve）与本地服务器（默认端口 52625，REST 与 OpenAI API），支持文本、视觉、音频、嵌入与 MoE 模型，上下文最长 256k tokens。运行时 17 MB，模型内核经 HuggingFace 下载；Windows 提供 MSI 安装包，Linux 有入门指南；也可用 CMake 从源码构建。编排代码与 CLI 为 MIT 许可，NPU 二进制内核不开源但可免费使用与再分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单命令 CLI 与本地服务器模式，提供 REST 与 OpenAI 兼容 API
- 支持视觉、音频、嵌入与 MoE 模型，上下文最长 256k tokens
- 运行时 17 MB，完全在 NPU 上运行，无需 GPU
- 已并入 AMD ROCm 组织，并集成进 Lemonade Server

## 适用场景

- 在带 Ryzen AI NPU 的 PC 上离线私有运行 LLM/VLM
- 本地起 OpenAI 兼容 API 供应用调用
- 在无 GPU 设备上运行 VLA 机器人策略模型（SmolVLA）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: ## ⚡ FastFlowLM (FLM) — Unlock Ryzen™ AI NPUs
> L10: 📦 **The only out-of-box, NPU-first runtime built exclusively for Ryzen™ AI.**
> L85: - 🧰 Simple CLI and API (REST and OpenAI API)

## 星数曲线

```mermaid
xychart-beta
    title "ROCm/FastFlowLM 星数(近 27 点)"
    x-axis ["2026-10-21", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 1957 --> 2090
    line [1968, 1980, 1981, 1984, 1990, 1993, 1996, 2000, 2005, 2006, 2007, 2011, 1984, 2030, 2037, 2041, 2042, 2043, 2048, 2053, 2055, 2056, 2064, 2072, 2075, 2079, 2079]
```

2026-10-21 1,968 → 2026-11-24 2,079（+111）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `39123c69a356` · [字段定义](../../DATASET.md)*
