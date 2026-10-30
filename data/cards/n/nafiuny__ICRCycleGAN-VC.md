# nafiuny/ICRCycleGAN-VC

⭐ 15 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/nafiuny/ICRCycleGAN-VC) · 个人维护

**波斯语/英语非平行语音转换的 CycleGAN PyTorch 实现**

ICRCycleGAN-VC 的官方 PyTorch 实现：基于循环生成对抗网络做非平行语音转换，在循环结构中引入 Inception-ResNet 模块以多组并行滤波器提取特征，针对波斯语语音结构设计，亦用于英语转换。流程为：克隆仓库、conda 环境安装、下载 VCC2018（或 FarsDat）数据、预处理为梅尔频谱 pickle、训练若干轮后用 test 脚本生成转换音频，支持断点续训与 Tensorboard 日志。README 未提供预训练模型下载入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CycleGAN 非平行语音转换，上下文无关
- 生成器使用 Inception-ResNet 模块并行提取特征
- 支持 A→B / B→A 双向转换与断点续训
- 预处理采用 melgan vocoder，可在推理时解码试听

## 适用场景

- 我想在两名说话人间做非平行语音转换实验
- 波斯语语音转换研究复现与对比
- 用 VCC2018 数据训练并生成转换后的 wav 音频

## 场景标签

 · 领域:语音处理/深度学习

## 证据(README 行号)

> L3: This is the official ICRCycleGAN-VC implementation repository with PyTorch.
> L5: Due to the results and poor performance of voice conversion models in Persian VC, we proposed ICRCycleGAN-VC , which
> L28: We used FarsDat dataset for tests in Persian language and VCC2018 for English VC.

## 星数曲线

```mermaid
xychart-beta
    title "nafiuny/ICRCycleGAN-VC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `38bad98d1c96` · [字段定义](../../DATASET.md)*
