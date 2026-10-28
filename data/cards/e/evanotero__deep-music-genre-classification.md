# evanotero/deep-music-genre-classification

⭐ 22 · Python · GPL-3.0 · 推送 2026-09-10 · [GitHub](https://github.com/evanotero/deep-music-genre-classification) · 组织维护

**实时音乐流派分类：CRNN 模型 + 交互式 Web 可视化**

基于卷积循环神经网络（Conv1D + LSTM）的音乐流派实时预测项目：将音频转为 128 维 log mel 频谱图，逐帧输出 16 类流派概率分布，并通过时间均值池化给出整曲分类。在 Free Music Archive 数据集（21,695 首，16 类）上训练，验证集准确率 54.52%。附带 Tornado Web 应用，支持上传 mp3/wav，播放时每 100ms 更新饼图并渲染音频响应粒子效果。供源码克隆后 pip 安装依赖并运行本地服务器使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRNN（Conv1D×3 + LSTM）逐帧输出 16 类流派概率分布
- 训练于 FMA 数据集 21,695 首歌曲，验证准确率 54.52%
- Tornado Web 应用：上传音频、实时饼图（每 100ms）与音频响应粒子可视化
- Librosa 生成 128 mel bins log 频谱图（22,050Hz，窗长 2048）

## 适用场景

- 上传歌曲查看流派概率随播放进程的实时演变
- 分析歌曲内部流派转换（前奏、独奏、主歌等段落）
- 研究频谱图 + CRNN 在音乐信息检索中的应用与复现实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Using deep learning to categorize music as time progresses through spectrogram analysis.
> L12: Our goal is to create a machine learning model capable of continuously predicting the probability distribution of a

## 星数曲线

```mermaid
xychart-beta
    title "evanotero/deep-music-genre-classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4f0a516aeac5` · [字段定义](../../DATASET.md)*
