# merantix-momentum/entquant

⭐ 27 · Python · NOASSERTION · 推送 2026-06-17 · [GitHub](https://github.com/merantix-momentum/entquant) · [官网](https://arxiv.org/abs/2601.22787) · 组织维护

**给开发者的 LLM 无数据量化压缩库：8 位精度存 2 位体积**

EntQuant 是面向 LLM 的后训练压缩库：权重保持 Float8/Int8 高精度格式，通过可微熵正则优化（以 L1 范数代理 Shannon 熵）使权重分布趋向低熵，再用 GPU 加速的 nvCOMP ANS 编解码器无损压缩，达到约 2 bits/参数的有效码率。无需校准数据与恢复训练，支持加载时即时 GPU 解压与逐块流式处理（完整模型不驻留内存）。以 Python 库提供，要求 Python>=3.11 与 CUDA GPU，依赖 NVIDIA nvCOMP 与 nvcc（后端 JIT 编译）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 位精度下实现低至约 2 bits/参数的压缩，码率连续可调（LAMBDA）
- 数据无关：无需校准数据与恢复训练，适用于指令微调与推理模型
- 单 GPU 10 分钟内压缩 70B 模型，块流式架构避免全模型驻留内存
- ANS 压缩在加载时即时完成，解压集成进推理前向过程

## 适用场景

- 把大模型压到 2-4 bit 存储并直接推理加载
- 无校准数据场景下快速压缩任意 HuggingFace 模型
- 复现论文实验或批量压缩对比实验

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L20: EntQuant breaks this coupling. It keeps weights in a high-precision 8-bit format (Float8 or Int8) but optimizes the
> L162:  It wraps a standard HuggingFace model and manages quantization, compression, and serialization.
> L166: - **`optimum-quanto`** provides the quantization primitives (`QLinear`, `WeightQBytesTensor`). EntQuant adds a cus

## 星数曲线

```mermaid
xychart-beta
    title "merantix-momentum/entquant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `249c0293b0c0` · [字段定义](../../DATASET.md)*
