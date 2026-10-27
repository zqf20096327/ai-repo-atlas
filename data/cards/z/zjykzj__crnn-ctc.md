# zjykzj/crnn-ctc

⭐ 29 · Python · Apache-2.0 · 推送 2026-07-19 · [GitHub](https://github.com/zjykzj/crnn-ctc) · [官网](https://arxiv.org/abs/1507.05717) · 个人维护 · 中文 README

**CRNN/LPRNet+CTC 车牌与数字识别训练框架**

基于 PyTorch 的 CRNN+CTC 与 LPRNet(+STNet) 序列识别实现，支持在 EMNIST 数字与中文车牌（CCPD2019/2020）数据集上训练、评估与预测，并提供模型转 ONNX 与基于 Gradio 的在线演示。README 列出各模型在不同数据集上的准确率、计算量与体积（含 CRNN_Tiny 超轻量版本），训练脚本支持混合精度。面向需要理解和部署车牌识别算法（如边缘设备）的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRNN(CONV+GRU/LSTM) 与 LPRNet/LPRNetPlus 纯卷积架构 + STNet 模块
- 覆盖 EMNIST 与 CCPD2019/2020 数据集的训练/评估/预测脚本
- 支持 PyTorch 模型转 ONNX 与 Gradio 在线演示
- 训练脚本支持混合精度训练

## 适用场景

- 在 CCPD/EMNIST 数据集上训练车牌或数字识别模型
- 将车牌识别模型转换为 ONNX 用于边缘设备部署
- 对比不同轻量模型在车牌识别上的准确率与体积

## 场景标签

`OCR` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L1: «crnn-ctc» implemented CRNN+CTC
> L48: This warehouse aims to better understand and apply CRNN+CTC, and has currently achieved digital recognition and lic
> L43: |v0.2.0|2023/10/11|Support training/evaluation/prediction of CRNN+CTC based on license plate.|

## 星数曲线

```mermaid
xychart-beta
    title "zjykzj/crnn-ctc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-27 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `08d2cbc6f96c` · [字段定义](../../DATASET.md)*
