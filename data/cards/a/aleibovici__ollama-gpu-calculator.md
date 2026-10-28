# aleibovici/ollama-gpu-calculator

⭐ 73 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/aleibovici/ollama-gpu-calculator) · [官网](https://aleibovici.github.io/ollama-gpu-calculator/) · 个人维护

**浏览器端估算 GPU 能否运行 Ollama 模型的 Web 计算器**

纯前端 Web 应用（无后端、无需安装），估算给定 GPU 上运行 Ollama 模型所需的 VRAM、KV cache、系统内存、解码速度（tokens/sec）与功耗，并给出兼容/边缘/不足判定。内置 99 种 GPU（NVIDIA/AMD/Apple Silicon）与 71 个模型预设，支持多 GPU、混合 GPU、MoE、多种量化与 KV cache 类型，计算基于标准 transformer 公式。源码运行需 Bun 1.2+，通过 GitHub Pages 提供在线版本。结果为估算值，实际取决于 Ollama 版本、后端与驱动等因素。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 99 种 GPU（NVIDIA/AMD/Apple Silicon）与 71 个模型预设
- 估算 VRAM、KV cache、系统 RAM、tokens/sec 与功耗
- 多 GPU 与混合 GPU 支持，MoE 感知（显存按总参数、速度按活跃参数）
- 配置通过 URL 分享，可复现同一计算配置

## 适用场景

- 购卡或选卡前确认某模型能否在本地 GPU 上运行
- 对比多 GPU 配置下各模型的显存需求与估算速度
- 通过分享链接向他人展示具体硬件与模型配置的估算结果

## 场景标签

 · 领域:LLM 基础设施/硬件估算工具

## 证据(README 行号)

> L8: Can your GPU run that Ollama model? This web app estimates the VRAM, KV cache, system RAM, decode speed and power dr
> L40: These are **estimates**. Real usage depends on the Ollama version, the backend (CUDA, ROCm, Metal, MLX), drivers, f


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `59b19c6e0b62` · [字段定义](../../DATASET.md)*
