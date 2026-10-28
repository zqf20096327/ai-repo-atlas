# n57d30top/gemma4-on-FPGA

⭐ 50 · Verilog · NOASSERTION · 推送 2026-04-05 · [GitHub](https://github.com/n57d30top/gemma4-on-FPGA) · 个人维护

**在 Xilinx KV260 FPGA 上运行 Gemma 蒸馏模型推理的部署包**

面向边缘部署的可复现 FPGA 推理工件包：将自研的 INT4 量化蒸馏模型（weights_int4_FINAL.bin，教师模型为 31B Gemma 系 CRACK 变体）与比特流、分卷权重、固定 tokenizer、模型契约和 SHA-256 校验打包，在 Kria KV260（Zynq UltraScale+ ZU5EV，ARM 控制面 + FPGA 可编程逻辑）上运行确定性推理。架构包含 HDC、Mamba 式序列路径、KAN 式计算路径与 36 核 NPU 集群。README 声明不将完整 31B 稠密权重驻留于 KV260 内存，采用有界工作集与硬件调度/流式方式；后续训练因算力不足暂停。许可为项目自有材料的 Dual-Use 非商业许可，商业使用被禁止。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 36 核 NPU 集群 + HDC/Mamba 式/KAN 式路径的 FPGA 推理架构
- INT4 蒸馏部署模型 + 固定 tokenizer + 模型契约的可复现工件链
- SHA-256 校验与 Base 链上锚定证明文件
- 实测吞吐约 443 words/s（bring-up 快照，标准化 TOPS 基准未发布）

## 适用场景

- 在 KV260 上以可复现工件运行边缘 LLM 推理
- 带完整性校验的 FPGA 模型部署与移植（for_other_fpgas 包）
- 摄像头到推理的边缘视觉管线原型（MIPI-CSI + ISP）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains a reproducible deployment bundle for running Gemma-based inference on a Xilinx Kria KV260 F
> L51: - The deployed runtime artifact is our **own smaller distilled deployment model** in `weights_int4_FINAL.bin`.

## 星数曲线

```mermaid
xychart-beta
    title "n57d30top/gemma4-on-FPGA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `79e3ce9dee89` · [字段定义](../../DATASET.md)*
