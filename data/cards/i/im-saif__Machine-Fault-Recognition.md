# im-saif/Machine-Fault-Recognition

⭐ 10 · Python · 推送 2026-05-07 · [GitHub](https://github.com/im-saif/Machine-Fault-Recognition) · 组织维护

**工业机械声学故障识别流水线：判别正常/异常运行**

基于 STgram-EfficientNet-B0 混合架构的机器听音系统：音频重采样至 16kHz 单声道，经静音裁剪与 RMS 归一化后，从 log-Mel 频谱图与 TgramNet（1D-CNN）时序特征双通路提取特征，经 EfficientNet-B0 骨干与 MLP 分类头输出 3 类机器×正常/异常共 6 类结果，报告测试准确率 97%。含 Focal Loss 处理类不平衡、SpecAugment 增强、SWA、双 GPU 训练配置；提供 pip/Docker 环境与 infer.py 推理脚本，另在 Hugging Face Spaces 提供在线演示。面向预测性维护场景的研究实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- STgram-EfficientNet-B0 双通路：128 带频谱图 + TgramNet 时序特征
- 静音裁剪、RMS 归一化、CMVN 预处理流水线
- Focal Loss（γ=2.0）应对正常/异常样本不平衡
- Hugging Face Spaces 交互式演示支持上传音频实时推理

## 适用场景

- 对工业设备录音批量推理判定正常/异常状态
- 复现或扩展基于 MIMII/DCASE 框架的异常声检测实验
- 预测性维护项目中接入声学监测模块

## 场景标签

 · 领域:工业/机器听音与故障诊断

## 证据(README 行号)

> L10: This repository contains the development of an automated **“Machine Listener”** system designed to classify acousti
> L13: Predictive maintenance is a critical component of modern Industry 4.0, aiming to detect mechanical failures before 
> L66: ### Running Inference

## 星数曲线

```mermaid
xychart-beta
    title "im-saif/Machine-Fault-Recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `cb03e965ea5b` · [字段定义](../../DATASET.md)*
