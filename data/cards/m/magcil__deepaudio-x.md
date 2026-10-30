# magcil/deepaudio-x

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/magcil/deepaudio-x) · [官网](https://magcil.github.io) · 组织维护

**基于预训练音频基础模型的音频分类训练库**

PyTorch 库，用预训练音频基础模型（BEATs、PaSST、MobileNet-AudioSet 系列）作为特征提取器，构建、训练、评估音频分类器。提供从目录结构或自定义映射创建数据集、长音频切分、可选池化策略（GAP/SimPool/EP）、Trainer 自动保存最优检查点与早停、Evaluator 输出预测与后验、单行推理（支持分段多数投票）等 API。检查点同时保存权重与架构配置，可一行恢复。由 NCSR Demokritos 旗下 MagCIL 研究组开发，支持 Python 3.11-3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BEATs/PaSST/MobileNet(AudioSet) 预训练骨干，pretrained=True 时自动下载缓存权重
- GAP/SimPool/EP 三种池化策略可切换
- Trainer 支持早停、最优检查点、自定义优化器与调度器、cuda/mps/cpu 设备选择
- 推理支持分段多数投票并输出逐段标签与后验

## 适用场景

- 用自己的音频数据集微调音频分类器
- 用预训练骨干提取音频嵌入或接自定义分类头
- 对长音频做分段分类并按多数投票得出整体标签

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L14: DeepAudioX is a PyTorch-based library that provides **simple, flexible pipelines for audio classification** using *
> L20: - 🔊 **Pretrained audio backbones** for feature extraction

## 星数曲线

```mermaid
xychart-beta
    title "magcil/deepaudio-x 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0c40eeb6015c` · [字段定义](../../DATASET.md)*
