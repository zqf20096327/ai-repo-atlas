# schonkopf/soundscape_IR

⭐ 46 · Python · MIT · 推送 2026-07-09 · [GitHub](https://github.com/schonkopf/soundscape_IR) · [官网](https://meil-brcas-org.github.io/V1.1/index.html) · 组织维护

**声景信息检索工具箱：声景音频可视化与非负矩阵分解源分离**

Python 工具箱 soundscape_IR，面向声学生态学研究者，提供两大功能：声景动态可视化（源自 MATLAB 包 Soundscape Viewer）与音频源分离。核心机制为 NMF/PC-NMF：从训练频谱图学习基函数，按源特有周期性分组，实现目标声源（如鹿鸣）与噪声分离；并含信号出现检测，输出每次叫声的起止时间与频率范围，可在 Raven 软件中查看。通过 git clone 源码方式安装，开发中项目完整版本移至 MEIL 组织仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- audio_visualization 生成 Hz/mel 频谱图，支持 Welch 平均与预白化降噪
- PC-NMF 按源特有周期性分离基函数实现音频源分离
- spectrogram_detection 检测目标信号并输出起止时间与频率范围
- 附带鹿鸣检测、水下声景、批量处理等教程示例

## 适用场景

- 从热带森林声景中分离并检测鹿鸣等目标物种叫声
- 分析长时间声景录音的声学多样性与动态
- 批量自动分析大量声景录音

## 场景标签

 · 领域:生态声学/音频分析

## 证据(README 行号)

> L3: **soundscape_IR** is a python-based toolbox of soundscape information retrieval, aiming to assist in the analysis of
> L53: After preparing the training spectrogram, we can train a model with ```source_separation```. NMF learns a set of ba

## 星数曲线

```mermaid
xychart-beta
    title "schonkopf/soundscape_IR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-27 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5871702ff80b` · [字段定义](../../DATASET.md)*
