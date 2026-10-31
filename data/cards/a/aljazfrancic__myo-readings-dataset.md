# aljazfrancic/myo-readings-dataset

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-06-14 · [GitHub](https://github.com/aljazfrancic/myo-readings-dataset) · 个人维护

**Myo 腕带 8 类手势肌电（EMG）机器学习数据集**

Myo armband 采集的表面肌电（EMG）数据集，覆盖休眠、屈曲、伸展、桡偏、尺偏、旋前、旋后与握拳共 8 类手腕/手部手势。每行数据为 8 个 EMG 通道（signed byte，约 200 Hz 采样）加手势标签，按参与者随机 ID-会话号组织目录，左右手分文件夹存放；每文件约 1 分钟录制（约 12000 行），标签每 5 秒在休眠与目标手势间交替。附 curated.txt 精选会话清单，推荐机器学习用途仅使用精选会话。面向肌电手势识别方向的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 EMG 通道、8 类手势标签，采样率约 200 Hz
- 按参与者 ID-会话号组织，左右手分目录，含多会话录制
- curated.txt 提供跨参与者准确率较好的精选会话清单

## 适用场景

- 训练和评测基于 EMG 的手势分类模型
- 复现或对比肌电信号机器学习研究
- 开展跨/同参与者手势识别实验

## 场景标签

 · 领域:生物信号/机器学习数据集

## 证据(README 行号)

> L3: Machine learning dataset of EMG recordings from the Myo armband of hibernation, flexion, extension, radial deviation
> L41: The `curated.txt` file contains a list of sessions that yield a decent intra-participant accuracy across most gestu

## 星数曲线

```mermaid
xychart-beta
    title "aljazfrancic/myo-readings-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9eed659ffffa` · [字段定义](../../DATASET.md)*
