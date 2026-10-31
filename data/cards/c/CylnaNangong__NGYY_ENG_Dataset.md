# CylnaNangong/NGYY_ENG_Dataset

⭐ 14 · 推送 2026-10-06 · [GitHub](https://github.com/CylnaNangong/NGYY_ENG_Dataset) · 个人维护 · 中文 README

**DiffSinger 虚拟歌手『南宫颜·羽』英语演唱数据集**

面向 DiffSinger 声库训练的英文演唱语音数据集，包含约 50 分钟、同一发音人三种音色的录音，使用电容麦在家庭安静环境录制。声学标注在自动标注后经人工修正，采用兼容 DIFF EN+ 音素器的 ARPAbetPlus 方案；音高由 SOME/GAME 自动标注，README 提示发音人音准有限、非母语者口音可能存在不一致，使用时需自行处理音频。禁止以他人或其他角色名义二次发布数据集及训练模型，建议使用时注明出处。数据集日后可能更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 50 分钟英文演唱录音，同一发音人三种音色
- 声学标注为自动标注后人工精修的 ARPAbetPlus 方案，兼容 DIFF EN+ 音素器
- 音频除剪辑外无后期处理，使用者可自行降噪/去混响
- 音高为 SOME/GAME 自动标注，README 提示发音人音准有限

## 适用场景

- 为 DiffSinger 训练英文演唱声库
- 作为歌声合成（SVS）研究的英文数据来源
- 研究不同音色同一发音人的声库表现

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: 3. The dataset contains about 50 mins of English singing voice wav files with three different voice color from the s
> L5: 1. Accoustic-related data is labelled with human correction after auto-labelling and in ARPAbetPlus way (with ax, dx

## 星数曲线

```mermaid
xychart-beta
    title "CylnaNangong/NGYY_ENG_Dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e59c811991b6` · [字段定义](../../DATASET.md)*
