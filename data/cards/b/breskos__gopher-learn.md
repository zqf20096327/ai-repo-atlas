# breskos/gopher-learn

⭐ 12 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/breskos/gopher-learn) · 个人维护

**纯 Go 无依赖的神经网络库：CSV 到分类回归预测**

纯 Go 实现的前馈神经网络库，仅依赖标准库，支持分类与回归。提供从原始 CSV 到预测的完整管线（列检测、编码、缩放、模型单文件保存），包含 SGD/momentum/Adam 优化、dropout、早停、在线流式学习与概念漂移检测（ADWIN、Page-Hinkley），以及网格/随机超参数搜索与置换特征重要性解释。模型可导出 float32 紧凑二进制格式，面向普通 CPU 与嵌入式设备，无 GPU/cgo/BLAS 依赖。要求 Go 1.24+，Apache 2.0 许可（v0.3.0 前为 GPL-3.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Go 实现，仅依赖标准库，无 cgo/BLAS/GPU
- 多核批量训练且结果逐位一致，推理零内存分配
- 在线学习与概念漂移检测（ADWIN、Page-Hinkley）
- float32 紧凑二进制模型，支持 ARMv7/RISC-V/WebAssembly 嵌入式部署

## 适用场景

- 在服务端或嵌入式设备上做表格数据的分类回归预测
- 在数据流上持续训练并检测概念漂移
- 分析模型对各个输入特征的依赖程度

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: Neural networks in pure Go, with no dependencies outside the standard library. Fast enough for services and small e
> L13: - Feed-forward networks (multi-layer perceptrons) with sigmoid, tanh, ReLU, linear and softmax activations, SGD, mo
> L16: - Online learning for streams: test-then-train evaluation, bounded memory and concept drift detection (ADWIN, Page-


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `30842e471663` · [字段定义](../../DATASET.md)*
