# linzm1007/nano-vllm-ascend

⭐ 95 · Python · MIT · 推送 2026-05-04 · [GitHub](https://github.com/linzm1007/nano-vllm-ascend) · 个人维护 · 中文 README

**面向昇腾 NPU 的轻量 LLM 推理引擎学习项目**

基于开源 nano-vllm 移植到华为昇腾 NPU 的轻量推理引擎，核心约 2428 行 Python 代码，定位是帮助初学者理解 LLM 推理整体流程。支持张量并行、torchair 图编译与图缓存、融合算子、PageAttention、前缀缓存与在线推理；模型覆盖 Qwen3/Qwen2/Llama-3.2/MiniCPM4 及 MoE、VL 各一个。API 与 vLLM 基本一致，环境搭建参考 vllm-ascend，需 CANN 与 torch-npu。附大量模块流程图文档与 bench 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 核心约 2428 行代码的轻量推理引擎，昇腾 NPU 原生 Attention 实现
- 支持张量并行、torchair 图编译/图缓存、融合算子、PageAttention、前缀缓存
- 支持 Qwen3/Qwen2/Llama-3.2/MiniCPM4 及 MoE、VL 模型，支持在线推理
- 附各模块 Mermaid 流程图文档与推理优化技术大纲

## 适用场景

- 在昇腾 NPU 上以小体量代码学习 LLM 推理引擎实现
- 运行 Qwen3 等小模型做推理实验与性能基准测试
- 对照三种 Attention 实现理解 FlashAttention/PageAttention 机制

## 场景标签

`推理引擎` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: nano-vllm是github开源的一个gpu推理项目，基于开源版本弄的一个ascend npu版本推理小demo，旨在帮助初学者了解推理的整体流程，区别于vllm，nano-vllm体量更小，麻雀虽小五脏俱全，更有助于初学者学习
> L346: 请参见 example.py 了解用法。该 API 与 vLLM 的接口基本一致，仅在 LLM.generate 方法上存在一些细微差异：

## 星数曲线

```mermaid
xychart-beta
    title "linzm1007/nano-vllm-ascend 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 94 --> 97
    line [96, 95, 95]
```

2026-10-18 96 → 2026-10-26 95（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `30ab3082de94` · [字段定义](../../DATASET.md)*
