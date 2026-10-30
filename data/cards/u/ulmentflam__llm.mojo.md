# ulmentflam/llm.mojo

⭐ 31 · Mojo · MIT · 推送 2026-10-27 · [GitHub](https://github.com/ulmentflam/llm.mojo) · 个人维护

**纯 Mojo 实现的 GPT-2 训练：手写 CUDA/Metal GPU 内核**

将 Karpathy 的 llm.c 移植到 Mojo 语言，用手写 CUDA 与 Metal GPU 内核训练 GPT-2 124M。支持 bf16/fp32(TF32) 训练精度，另加入 FP8(e4m3/e5m2) 与 NVFP4(e2m1) 低精度训练路径；在 NVIDIA GB10 上 bf16 与 llm.c 对齐、fp32(TF32) 约快 7%，在 Apple M4 Max Metal 上 bf16 比 PyTorch MPS 快 1.71×。提供多 GPU 数据并行（WORLD_SIZE 编译期指定、ZeRO 0-3 分片、等价性测试门控）、FineWeb 预训练数据脚本与断点续训的进程守护方案。安装经 git clone 子模块 + pixi 环境 + make 流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手写 CUDA 与 Metal GPU 内核，覆盖前向与反向传播
- FP8(e4m3/e5m2) 与 NVFP4(e2m1) 可训练精度，master 权重保持 fp32
- 多 GPU ZeRO 0-3 分片，各阶段经单 GPU 基线等价性测试门控
- make verify 逐梯度对拍 PyTorch，复现 llm.c 的 40 步训练轨迹

## 适用场景

- 在 NVIDIA 或 Apple Silicon GPU 上训练 GPT-2 124M 并复现 llm.c 结果
- 学习/验证 Mojo 语言编写的 GPU 训练内核
- 多 GPU 环境下做 ZeRO 分片的 GPT-2 数据并行训练
- 实验 FP8/NVFP4 低精度训练的收敛行为

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This is my port of Andrej Karpathy's llm.c, extending the GPU kernels of @dorjeduck's llm.🔥 in honor of Mojo's v1.0.
> L5: - On an NVIDIA GB10, it matches or beats llm.c's CUDA path at both training precisions (bf16 parity, fp32 ~7% faster
> L6: - On an Apple M4 Max, it runs 1.71× faster than PyTorch MPS bf16, though Apple's own MLX is faster still (see Benchm

## 星数曲线

```mermaid
xychart-beta
    title "ulmentflam/llm.mojo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c928bba4b478` · [字段定义](../../DATASET.md)*
