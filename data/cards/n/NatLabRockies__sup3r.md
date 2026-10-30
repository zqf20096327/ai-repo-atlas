# NatLabRockies/sup3r

⭐ 142 · Python · BSD-3-Clause · 推送 2026-10-28 · [GitHub](https://github.com/NatLabRockies/sup3r) · [官网](https://natlabrockies.github.io/sup3r/) · 组织维护

**用 GAN 将粗分辨率气候数据降尺度为高时空分辨率数据**

NLR 开发的开源 Python 软件，基于生成对抗网络（生成器+判别器）将全球气候模型或再分析等粗分辨率数据（可低至 100km/日均）降尺度为 0.5-4km、5-60 分钟分辨率的风、太阳辐照、温湿度等时空数据。提供 DataHandler 数据结构读取 .h5/.nc 文件，支持训练与推理流程、CLI 及 HPC 部署；附带 Sup3rCC（气候情景）、Sup3rWind（风资源）、Sup3rUHI（城市热岛）三个应用与预训练示例。依赖 TensorFlow，GPU 训练需另装 CUDA 版本，面向能源系统建模与气候分析用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GAN 生成器/判别器架构学习高分辨率物理特征
- 将粗气候数据降尺度至 0.5-4km 空间、5-60 分钟时间分辨率
- DataHandler 支持 .h5 与 .nc 数据，训练/推理测试与预训练示例齐备
- 提供 CLI 支持 HPC 环境下的完整运行

## 适用场景

- 为风电场选址或能源系统规划生成高分辨率风资源数据
- 研究城市高温热浪的街区级温湿度分布
- 将全球气候模型输出降尺度用于未来气候情景分析

## 场景标签

 · 领域:气候/可再生能源数据科学

## 证据(README 行号)

> L36: available datasets that leverages generative adversarial networks to
> L60: Sup3r uses a generative machine learning approach to produce synthetic

## 星数曲线

```mermaid
xychart-beta
    title "NatLabRockies/sup3r 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 141 --> 143
    line [142, 142]
```

2026-10-18 142 → 2026-10-30 142（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7e032f852e4e` · [字段定义](../../DATASET.md)*
