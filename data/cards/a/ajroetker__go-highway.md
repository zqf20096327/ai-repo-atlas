# ajroetker/go-highway

⭐ 119 · Assembly · Apache-2.0 · 推送 2026-07-08 · [GitHub](https://github.com/ajroetker/go-highway) · 个人维护

**Go 的可移植 SIMD 抽象库：一次编写，多架构运行**

受 Google Highway C++ 库启发的 Go 语言 SIMD 抽象层：同一套向量运算代码可运行于 AMD64 AVX2/AVX-512（Go 1.26 原生 simd/archsimd）、ARM64 NEON/SVE/SME（GoAT 生成的 hwy/asm 汇编）或纯 Go 标量回退。提供 Load/Store、算术、归约、逐元素数学变换等核心操作，contrib 包含矩阵乘、激活函数、损失函数、量化、GGUF 格式支持等。附带 hwygen 代码生成器，从泛型实现生成按目标架构分发的优化代码，neon:asm 模式经 C→GoAT 汇编转译处理整段数组。要求 Go 1.26+，AMD64 硬件加速需 GOEXPERIMENT=simd。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套代码支持 AVX2/AVX-512/NEON/SVE/SME 与纯 Go 回退
- hwygen 从泛型实现生成目标特定代码并自动分发
- contrib 包含 matmul/激活函数/损失函数/量化/GGUF 等 SIMD 实现
- neon:asm 汇编模式整段处理数组，消除逐向量调用开销

## 适用场景

- 在 Go 中编写跨架构的向量计算内核
- 为神经网络算子（激活、损失、矩阵乘）获得 SIMD 加速
- 向量量化与相似度计算的批量加速

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: A portable SIMD abstraction library for Go, inspired by Google's Highway C++ library.
> L7: Write SIMD code once, run it on AVX2, AVX-512, ARM NEON, or pure Go fallback.
> L101: |`hwy/contrib/activation`|Neural network activation functions|

## 星数曲线

```mermaid
xychart-beta
    title "ajroetker/go-highway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-29 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `7b0069f3bef4` · [字段定义](../../DATASET.md)*
