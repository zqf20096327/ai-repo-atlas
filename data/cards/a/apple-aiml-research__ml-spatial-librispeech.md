# apple-aiml-research/ml-spatial-librispeech

⭐ 130 · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/apple-aiml-research/ml-spatial-librispeech) · 组织维护

**650+ 小时一阶 ambisonics 空间音频数据集，供机器学习训练**

Apple ML Research 发布的空间音频合成数据集：基于 LibriSpeech 语料增广，覆盖 200k+ 模拟声学条件、8k+ 合成房间，提供声源位置、说话方向、房间声学与几何标签，另含可选的干扰噪声。面向机器学习模型训练研究者使用，配套 Interspeech 2023 论文。当前仅支持通过 URL 手动下载 metadata.parquet 与 FLAC 样本，官方下载脚本与 PyTorch dataloader 尚未上传，19 通道原始音频暂未开放托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 650+ 小时一阶 ambisonics 空间音频，含可选干扰噪声
- 标签覆盖声源位置、说话方向、房间声学与几何
- 由 LibriSpeech 在 8k+ 合成房间、200k+ 声学条件下增广生成
- 配套 Interspeech 2023 论文可引用

## 适用场景

- 训练空间音频相关的机器学习模型（如声源定位/波达方向估计）
- 研究房间声学与混响条件下的语音任务
- 在论文中作为数据集引用并复现实验

## 场景标签

 · 领域:语音/音频机器学习数据集

## 证据(README 行号)

> L3: Spatial LibriSpeech, is a spatial audio dataset with over 650 hours of first-order
> L4: ambisonics, and optional distractor noise (with raw 19-channel audio coming soon). Spatial LibriSpeech is designed f

## 星数曲线

```mermaid
xychart-beta
    title "apple-aiml-research/ml-spatial-librispeech 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-29 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6824dd70ac82` · [字段定义](../../DATASET.md)*
