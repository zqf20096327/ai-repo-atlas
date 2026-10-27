# Captain-FLAM/KaraFan

⭐ 152 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/Captain-FLAM/KaraFan) · 个人维护

**本地/Colab 运行的 AI 人声分离软件，面向卡拉 OK 制作**

由个人开发者（业余摇滚歌手）开发的音乐人声分离软件，基于 MDX-Net 系列 AI 模型（含 MDX23-8K FFT、Kim Vocal 2 等）并级联多个模型，侧重产出高质量伴奏轨以制作卡拉 OK 文件（KFN 等），供 KaraFun 等软件播放。可在本地 PC（Windows/Linux/macOS，需 GPU）或 Google Colab 运行；作者使用 GTX 1060 Ti 4GB 笔记本开发。项目自 2024 年 6 月起处于搁置状态，等待 2.0 版重写；MIT 许可但要求保留署名与版权头。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 MDX-Net 系列模型的级联人声分离流程
- 支持本地 PC 运行（需 decent GPU）与 Google Colab
- 面向卡拉 OK 伴奏制作，可生成 KFN 文件配合 KaraFun 使用

## 适用场景

- 去除歌曲人声，自制卡拉 OK 伴奏
- 在 Google Colab 上无需本地 GPU 进行分离
- 为不著名歌手的歌曲制作可演唱的伴奏

## 场景标签

 · 领域:音频/音乐信息检索

## 证据(README 行号)

> L5: The **BEST music separation** software with help of A.I. ... **to my ears** ! 👂👂
> L93: So I decided to create my own process, based on the MDX models, but with the **best instrumental** that I could get
> L141: ✔️ Anjok07 & Aufr33 - for having trained **all the MDX-Net AI models** that KaraFan uses.

## 星数曲线

```mermaid
xychart-beta
    title "Captain-FLAM/KaraFan 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 150 --> 153
    line [151, 152, 152]
```

2026-10-18 151 → 2026-10-27 152（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b0b9eb499b05` · [字段定义](../../DATASET.md)*
