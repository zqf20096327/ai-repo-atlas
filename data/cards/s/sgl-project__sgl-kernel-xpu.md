# sgl-project/sgl-kernel-xpu

⭐ 37 · C++ · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sgl-project/sgl-kernel-xpu) · 组织维护

**SGLang 框架面向 Intel XPU 的官方 kernel 库**

sglang-kernel-xpu 是 SGLang 框架在 Intel XPU 平台上的官方计算 kernel 库，为推理框架提供 MoE group gemm、Flash attention、Gated DeltaNet、MLA 与 QSA 稀疏注意力等算子。默认 AOT 编译，可开启 USE_SYCL_JIT 运行时按需编译以缩短构建；构建需先安装 Intel GPU 驱动并 source oneAPI 环境，通过 pip 源码构建安装。面向在 Intel GPU 上开发/运行 SGLang 的开发者。

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

- MoE group gemm / Flash attention / MLA / QSA 等算子集合
- USE_SYCL_JIT 可选运行时 JIT 编译（icpx 按需编译并缓存 .so）
- 构建期开关可按功能组禁用（USE_MOE/USE_FMHA/USE_GDN 等）
- 提供 make_pytorch_shim 处理第三方库与 PyTorch 的数据类型转换

## 适用场景

- 在 Intel GPU 上运行 SGLang 推理框架
- 为 Intel XPU 开发/扩展 SYCL kernel
- 缩短构建时间或裁剪 wheel 体积

## 场景标签

 · 领域:AI 基础设施/推理 kernel

## 证据(README 行号)

> L3: sglang-kernel-xpu is the official kernel library of the SGLang framework for Intel XPU, which delivers high-performa
> L9: Currently we only support building from source. To use on Intel GPUs, you need to install the Intel GPUs driver firs

## 星数曲线

```mermaid
xychart-beta
    title "sgl-project/sgl-kernel-xpu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-29 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8848d447305f` · [字段定义](../../DATASET.md)*
