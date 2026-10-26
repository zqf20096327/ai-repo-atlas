# vicharak-in/Axon-NPU-Guide

⭐ 38 · Shell · 推送 2026-09-24 · [GitHub](https://github.com/vicharak-in/Axon-NPU-Guide) · 组织维护

**在 Axon SBC 的 NPU 上运行 AI 模型的工具链配置指南**

面向 Vicharak Axon（RK3576/RK3588）单板机用户的操作指南仓库：说明如何通过 max_freq.sh 脚本解锁 NPU 及各计算单元的最大频率，给出 LLM 与 CNN 模型（Llama3.2、Qwen2-VL、YOLO 系列、Whisper 等）在 NPU 上的吞吐基准数据，并分步讲解在 PC 与 Axon 上安装 rknn-toolkit2 / rknn-toolkit-lite2、将 ONNX 或 HuggingFace/gguf 模型转换为 .rknn/.rkllm 格式、用 C API 编译运行 LLM 的流程。仓库本身为文档，不含可安装软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 包含 LLM（Llama3.2-1B 21.23 tok/s 等）与 CNN（YOLO 最高 648.9 FPS）的 NPU 基准数据
- 覆盖 ONNX→.rknn 与 HuggingFace/gguf→.rkllm 的模型转换全流程
- 提供 rknn-toolkit2 在 x86 PC 与 Axon(arm64) 上的分环境安装步骤
- 包含零拷贝视频管线（MPP 解码 + RGA + DMA-BUF）的 YOLO 速度/精度对比表

## 适用场景

- 我想在 Axon 板子的 NPU 上跑自己的 CNN 模型
- 查看 LLM 在 RK3588/RK3576 NPU 上的实际 tokens/s 参考数据
- 把 HuggingFace 或 gguf 模型转成 rkllm 格式并在板端编译运行

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # Axon-NPU-Guide
> L2: This repository contains guide on how to setup toolkits to use NPU present on Axon for running various AI/ML/DL mode
> L62: ### How to convert your custom CNN model to rknn format to run it on NPU

## 星数曲线

```mermaid
xychart-beta
    title "vicharak-in/Axon-NPU-Guide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-26 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `53aaf48935d0` · [字段定义](../../DATASET.md)*
