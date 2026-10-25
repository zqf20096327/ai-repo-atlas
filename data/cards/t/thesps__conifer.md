# thesps/conifer

⭐ 65 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/thesps/conifer) · 组织维护

**将训练好的 BDT 模型转换为 FPGA 固件的低延迟推理工具**

面向粒子物理等低延迟场景的工具：读取 scikit-learn、xgboost、ONNX、TMVA、ydf 训练的 Boosted Decision Tree，生成 Xilinx HLS、VHDL、FPU IP 核、C++、Python 等多种后端工程。FPU 为可复用 IP 核，可重编程加载不同 BDT 而无需重建比特流。构建 FPGA 固件需 Xilinx HLS/Vivado 工具（验证版本 2024.1），C++ 后端需 JSON 头文件与 Xilinx 任意精度头文件。源自 hls4ml 项目，由 Fast Machine Learning Lab 开发，已被 ATLAS 实验用于 tau 触发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 5 种 BDT 训练框架转换（scikit-learn/xgboost/ONNX/TMVA/ydf）
- 5 种后端输出：Xilinx HLS、VHDL、FPU IP 核、C++、Python
- Forest Processing Unit 可重编程加载不同 BDT，无需重建比特流
- 提供若干预编译 FPU 比特流供指定开发板下载

## 适用场景

- 将训练好的 BDT 部署到 FPGA 实现微秒级触发推理
- 在高能物理实验触发系统中运行 BDT 事件重建
- 在嵌入式 FPGA 上做前端数据过滤与医学图像分割加速

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: Conifer translates trained Boosted Decision Trees to FPGA firmware for extreme low latency inference.
> L19: Conifer converts from popular BDT training frameworks, and can emit code projects in different FPGA languages.

## 星数曲线

```mermaid
xychart-beta
    title "thesps/conifer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-25 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `72b8576b3e25` · [字段定义](../../DATASET.md)*
