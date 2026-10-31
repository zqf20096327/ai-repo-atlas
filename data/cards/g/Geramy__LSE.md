# Geramy/LSE

⭐ 33 · C++ · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Geramy/LSE) · 个人维护

**面向 AMD GPU 的 LLM 推理引擎，自优化生成 GPU 内核**

LSE 是在 Linux、macOS 和 iPadOS 上为 AMD GPU 运行 LLM 推理的引擎：将模型前向过程记录为图，融合算子并按设备特性（计算单元、LDS、wave size 等）生成 Loom 方言内核，经 loomc 编译后由 HRX 启动并缓存；多布局内核在 GPU 上实测择优。支持 Qwen3.5 系 MLX 4/8-bit 检查点、FP16/BF16/FP8 KV 缓存、MTP 与 DFlash2 投机解码、FlashPrefill V2 稀疏预填充，附带 OpenAI 兼容 HTTP 服务器、CLI 与 C 库。多 GPU/多节点支持尚在开发中且无公开结果。

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

- 按设备事实自动生成并实测择优 GPU 内核（on-disk 缓存）
- MTP 与 DFlash2 投机解码，按实测接受率与验证开销动态调整草稿深度
- FlashPrefill V2 稀疏长提示预填充
- OpenAI 兼容 HTTP 服务器、CLI 与 C 库（libLSE）

## 适用场景

- 在 Linux/macOS/iPadOS 的 AMD GPU 上本地运行 Qwen3.5 系模型
- 通过 OpenAI 兼容接口对外提供推理服务
- 对模型做困惑度评测与 KL 散度对比

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: LLM inference engine for AMD GPUs on Linux, macOS and iPadOS.
> L5: LSE records a model's forward pass as a graph, fuses operations, and generates kernels for the GPU it runs on. Kerne

## 星数曲线

```mermaid
xychart-beta
    title "Geramy/LSE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `539628cb1b0e` · [字段定义](../../DATASET.md)*
