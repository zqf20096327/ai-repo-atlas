# manjunathshiva/turboquant-mlx

⭐ 91 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/manjunathshiva/turboquant-mlx) · [官网](https://pypi.org/project/turboquant-mlx-full/) · 个人维护

**面向 Apple Silicon 的 LLM 权重与 KV cache 极限压缩工具（TurboQuant 的 MLX 实现）**

Google TurboQuant 论文的 MLX 实现，通过 Hadamard 旋转 + Lloyd-Max 码本对权重（编译期）和 KV cache（运行期）做 2-4 bit 乃至三值（1.58-bit）压缩，数据无关、无需校准集。支持稠密模型、MoE、Mamba/注意力混合与多模态模型；提供专家流式加载（超内存 MoE 从磁盘按需分页）、OpenAI 兼容端点、turboquant-plan 预估与 turboquant-doctor 就绪检查。以 PyPI 包 turboquant-mlx-full 提供，要求 macOS Apple Silicon 与 Python 3.11+。限制：仅限 Apple Silicon 平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 权重与 KV cache 双压缩，2-4 bit 及三值专家，数据无关无需校准
- 专家流式加载：权重超 RAM 的 MoE 按需从磁盘分页（如 35B 模型 <4 GB 内存运行）
- 支持稠密/MoE/Mamba 混合/多模态及滑动窗口、线性注意力等架构
- turboquant-plan 仅读 safetensors 头部即可预估内存占用

## 适用场景

- 在 16-64 GB 内存的 Mac 上运行原本放不下的大模型
- 压缩 KV cache 以支撑 131K+ 长上下文
- 为 Cursor / VS Code 本地部署 OpenAI 兼容的编码模型端点

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Extreme **weight** and **KV cache** compression for LLMs on Apple Silicon. MLX implementation of Google's TurboQuant
> L92: pip install turboquant-mlx-full
> L97: - macOS on Apple Silicon (M1 or later)

## 星数曲线

```mermaid
xychart-beta
    title "manjunathshiva/turboquant-mlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-30 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `263472f45e06` · [字段定义](../../DATASET.md)*
