# dennisvdang/chorus-detection

⭐ 49 · Jupyter Notebook · 推送 2026-08-22 · [GitHub](https://github.com/dennisvdang/chorus-detection) · 个人维护

**检测歌曲副歌段落的深度学习模型与 CLI 工具**

PyTorch 实现的层级卷积循环神经网络（CRNN），在 332 首人工标注的电子音乐歌曲上训练，用于检测音乐录音中的副歌段落，测试集 F1 为 0.871。模型按小节读取音频特征（RMS、色度图、mel 频谱、MFCC、tempogram 经 NMF 分解），输出逐小节副歌概率，再经 Viterbi 解码与边界吸附转为时间戳。提供 CLI 工具（输入 YouTube 链接）、HuggingFace Spaces 在线试用与预训练模型，首次运行自动下载。局限：边界精确落点 76.5%，剩余错误多为错误段落识别。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 层级 CRNN：CNN 处理小节内帧特征，双向 LSTM 捕捉跨小节结构
- 依赖节拍/小节网格，默认使用 Beat This! 追踪的重拍网格
- Viterbi 解码 + 边界吸附后处理，输出副歌时间戳
- 支持自训练模型（YAML 配置、可复现切分、checkpoint）

## 适用场景

- 输入 YouTube 链接自动定位一首歌的副歌段落
- DJ 场景下对齐混音曲目的副歌起始点
- 基于自己的标注数据训练自定义副歌检测模型

## 场景标签

 · 领域:音乐信息检索/音频分析

## 证据(README 行号)

> L7: A hierarchical convolutional recurrent neural network designed for detecting choruses in music recordings, implement
> L98: The model employs a two-tier architecture that respects the heirarchical structure of music (frames → meters → song

## 星数曲线

```mermaid
xychart-beta
    title "dennisvdang/chorus-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `aed80fa19320` · [字段定义](../../DATASET.md)*
