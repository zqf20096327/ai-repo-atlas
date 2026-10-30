# helgklaizar/turboquant-mlx

⭐ 50 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/helgklaizar/turboquant-mlx) · [官网](https://github.com/helgklaizar/turboquant_mlx) · 个人维护

**Apple Silicon 上 MLX 模型的 1-3 bit KV 缓存压缩库**

面向 Apple MLX 框架的 KV cache 压缩库，基于 PolarQuant（笛卡尔-极坐标变换）算法做无偏点积估计，将 LLM 推理的 KV 缓存压缩至 1-3 bit，内存占用最高降至约 1/5.3。机制包括 K/V 非对称压缩（k_bits=8/v_bits=3）、Boundary V 层隔离（首末各 2 层不压缩）、Attention Sink（系统提示词保留 float16）、64 token 分块缓冲。以两行代码接入 mlx_lm，附 OpenAI 兼容服务脚本；明确说明与 LM Studio 不直接兼容。安装方式为 git clone 后 pip install -e。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PolarQuant 算法实现 1-3 bit KV 缓存压缩（约 5.3x 内存缩减）
- K/V 非对称压缩 + Boundary V 层隔离 + Attention Sink
- 两行代码接入 mlx_lm 的插件式使用
- 附带 OpenAI 兼容 API 服务脚本（run_server.py）

## 适用场景

- 长上下文 LLM 推理时降低 M 系列 Mac 的内存占用
- 在 MLX 上运行 DeepSeek/Llama/Qwen 等模型的 KV 缓存压缩
- 为 Chatbox/Jan/Open WebUI 等前端提供本地压缩推理后端

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: **Extreme KV Cache Compression (1-3 bit) for LLMs on Apple Silicon**
> L10: The library utilizes the **PolarQuant** (Cartesian-to-Polar transformations) algorithm for unbiased dot-product est
> L31: You can seamlessly plug TurboQuant into any existing `mlx_lm` models (Llama 3, Gemma 2, etc.) to immediately free u

## 星数曲线

```mermaid
xychart-beta
    title "helgklaizar/turboquant-mlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c44499953472` · [字段定义](../../DATASET.md)*
