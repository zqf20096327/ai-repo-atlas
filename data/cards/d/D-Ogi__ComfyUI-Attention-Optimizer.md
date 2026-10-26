# D-Ogi/ComfyUI-Attention-Optimizer

⭐ 37 · Python · MIT · 推送 2026-02-09 · [GitHub](https://github.com/D-Ogi/ComfyUI-Attention-Optimizer) · 个人维护

**ComfyUI 插件：自动基准测试并选用最快 attention 后端加速扩散模型**

面向 ComfyUI 用户的自定义节点（model_patches 类别）：对 PyTorch SDPA、Flash Attention 2、SageAttention（含 FP8/sage3 变体）、xFormers 等 attention 后端进行基准测试，按模型哈希、head_dim、seq_len/num_heads 缓存结果到 benchmark_db.json，并自动为模型应用最快后端。兼容 SDXL、SD1.5/3、Flux、LTX-V、WAN、Hunyuan Video、Cosmos 等；AMD ROCm 仅基线无加速。通过 ComfyUI Manager 或 git clone 安装，优化后端需额外 pip 安装。

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

- 基准测试全部可用 attention 后端并自动应用最快者（首次约 5-10 秒，之后走缓存）
- 支持 PyTorch SDPA / Flash Attention / SageAttention 多变体 / xFormers 共 9 种后端
- 输出 speedup、time_ms、head_dim、基准报告等节点数据，兼容 KJNodes PatchSageAttention
- 兼容 SDXL/SD/Flux/LTX-V/WAN/Hunyuan Video/Cosmos，SeedVR2 不适用

## 适用场景

- 让我的 SDXL/Flux 工作流在不同 GPU 上自动选最快的 attention 后端
- 查看各类 attention 实现在我显卡上的实测加速数据
- 视频模型（WAN/Hunyuan）生成太慢时通过更换后端提速

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L25: This plugin **benchmarks all available backends** and **automatically applies the fastest one**.
> L77: 1. Add **"Attention Optimizer"** node to your workflow (category: `model_patches`)

## 星数曲线

```mermaid
xychart-beta
    title "D-Ogi/ComfyUI-Attention-Optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b72b7d5f37ea` · [字段定义](../../DATASET.md)*
