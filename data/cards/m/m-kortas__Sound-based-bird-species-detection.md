# m-kortas/Sound-based-bird-species-detection

⭐ 102 · Jupyter Notebook · 推送 2026-04-14 · [GitHub](https://github.com/m-kortas/Sound-based-bird-species-detection) · [官网](https://wimlds.voicelab.ai/) · 组织维护

**基于声音的中欧鸟类物种识别 Web 应用与训练流程**

WiMLDS 波兰分部成员于 2020 年创建的训练项目：从 xeno-canto.org 下载波兰及周边国家鸟类录音，切成 5 秒片段并预处理为梅尔频谱图，经高通滤波去噪，按 8:1:1 划分数据集（防止同源文件泄漏）。用 CNN（Xception、MobileNet、EfficientNet 及手工网络）做鸟类物种分类，覆盖 19 类（中欧录音）与 27 类（全球录音）两组实验。后端为 Python/Flask，配套 Jupyter notebook 完成数据下载与预处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 录音切分为 5 秒片段并转为梅尔频谱图，配合高通滤波去噪
- 按 8:1:1 划分数据集，显式规避同源文件导致的数据泄漏
- 对比测试 Xception、MobileNet、EfficientNet 与手工 CNN
- 两组实验：19 类中欧鸟类与 27 类全球鸟类

## 适用场景

- 上传鸟鸣录音识别中欧常见鸟类物种
- 作为深度学习入门的端到端训练项目参考
- 复用频谱图预处理与防数据泄漏的数据划分方法

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # Sound-based bird recognition Web Application
> L72: We approached the problem of song classification with Convolutional Neural Networks. We have tested it with:

## 星数曲线

```mermaid
xychart-beta
    title "m-kortas/Sound-based-bird-species-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-30 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d36ad187df9f` · [字段定义](../../DATASET.md)*
