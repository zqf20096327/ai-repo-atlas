# rajveer43/VeloxQuant-MLX

⭐ 32 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/rajveer43/VeloxQuant-MLX) · [官网](https://veloxquant.dev/) · 个人维护

**Apple Silicon 上 MLX 模型的 KV 缓存压缩库：更长上下文、更少内存**

面向在 Apple Silicon 本地运行 MLX 模型的开发者，提供 43 种来自论文改编的 KV-cache 压缩方法（量化 22 种、低秩/跨层 6 种、token 驱逐/合并 15 种），统一 3 行 API，切换方法只需改 method 参数。热路径使用手写 Metal kernel，在 12 个生产模型及视觉语言模型上验证。附带 CLI、本地 Web 控制面板和 veloxquant serve 服务器，可对接 OpenAI 兼容客户端。需注意：多数方法的压缩比是位宽核算而非实测 RSS；维护者为个人加一名贡献者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 43 种论文改编压缩方法，统一 3 行 API
- 手写 Metal kernel 加速量化（最高 14.7×）
- veloxquant panel 本地 Web 控制面板与 OpenAI 兼容 serve 命令
- CLI recommend 按芯片/内存/模型规格推荐方法

## 适用场景

- 本地跑大模型时突破上下文长度或内存限制
- 在 Mac 上压缩 KV 缓存以运行更长 prompt
- 通过控制面板选择方法并对外提供 OpenAI 兼容推理服务

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L27: VeloxQuant-MLX shrinks the KV cache of any `mlx_lm` model on Apple Silicon, up to 16× smaller with near-lossless qu
> L29: Inside are 43 compression methods, each adapted from a published paper, spanning zero-calibration 1-bit quantizers,
> L222: Every method runs the same three-step pipeline: rotate the K/V tensors into a friendlier basis, quantize them (opt

## 星数曲线

```mermaid
xychart-beta
    title "rajveer43/VeloxQuant-MLX 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-26 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `13b357c28102` · [字段定义](../../DATASET.md)*
