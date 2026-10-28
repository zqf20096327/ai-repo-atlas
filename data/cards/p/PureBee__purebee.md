# PureBee/purebee

⭐ 28 · JavaScript · NOASSERTION · 推送 2026-02-27 · [GitHub](https://github.com/PureBee/purebee) · 组织维护

**纯软件定义的 GPU：无硬件依赖运行 Llama 3.2 1B 推理**

用 JavaScript/WebAssembly 在单 CPU 核上实现 LLM 推理的运行时，宣称零依赖、无 GPU/CUDA/驱动要求。四层架构（Runtime/Kernel/ISA/SIMD 视图），通过 Typed arrays、WASM 编译核、Q4 量化、SIMD 与 Worker threads 将 Llama 3.2 1B 从 0.08 提升到 3.6 tok/sec。支持 Llama 3.2 1B、SmolLM2-135M 及 stories 系列小模型，需 Node.js ≥ 20 并扩大堆内存运行。采用 FSL-1.1-Apache-2.0 许可，2028 年转为 Apache 2.0，处于活跃开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单 CPU 核上运行 Llama 3.2 1B，达 3.6 tok/sec，45 倍累计加速
- 四层可替换架构，零依赖，无 GPU/CUDA/驱动要求
- 支持 Llama 3.2 1B、SmolLM2-135M 与 stories 开发用小模型
- 仅需 Node.js ≥ 20，通过 git clone 源码运行

## 适用场景

- 在无 GPU 环境的普通设备上运行小模型 LLM 推理
- 研究/学习 GPU 计算模型的纯软件实现
- 作为可审计的分层推理实现进行教学或实验

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L7: PureBee is pure math — four layers, zero dependencies, runs Llama 3.2 1B at **3.6 tok/sec on a single CPU core**.
> L49: This isn't a demo. This is Llama 3.2 1B running full inference.

## 星数曲线

```mermaid
xychart-beta
    title "PureBee/purebee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `85aa389fe450` · [字段定义](../../DATASET.md)*
