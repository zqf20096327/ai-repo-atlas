# trimplexx/music-transcription

⭐ 18 · TeX · 推送 2026-01-14 · [GitHub](https://github.com/trimplexx/music-transcription) · 个人维护

**深度学习吉他六线谱自动转录系统（CRNN，PyTorch）**

将复音吉他录音转录为六线谱的深度学习系统：CRNN 架构（CQT 频谱输入 + 双向 GRU），多任务学习同时预测音符起始与品格位置，输出 ASCII 与 MIDI 格式。在 GuitarSet 数据集上取得 0.8736 MPE F1 与 0.8569 TDR F1。训练依赖 7 种数据增强策略，提供超参数搜索框架；数据经 mirdata 自动下载，按 80/10/10 划分。配套波兰语硕士论文（西里西亚理工大学）。需 Python 3.10+、PyTorch 2.5，GPU 加速需 CUDA 12.1+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRNN 多任务学习：同时进行音符起始检测与品格分类
- GuitarSet 上 MPE F1 0.8736、TDR F1 0.8569
- 7 种数据增强（时间拉伸/噪声/混响/EQ/SpecAugment 等）
- 输出 ASCII 六线谱与 MIDI 文件

## 适用场景

- 把吉他录音自动转成六线谱或 MIDI
- 在 GuitarSet 上复现或改进吉他转录模型
- 研究数据增强对音乐信息检索任务的影响

## 场景标签

 · 领域:音频/音乐信息检索

## 证据(README 行号)

> L7: A deep learning system for **Automatic Guitar Tablature Transcription (GTT)** that converts polyphonic guitar audio 
> L28: ✅ **Multi-task Learning** - Simultaneous onset detection and fret classification

## 星数曲线

```mermaid
xychart-beta
    title "trimplexx/music-transcription 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2a1aea29c2bc` · [字段定义](../../DATASET.md)*
