# TheProductAgency/flipper-ai-composer

⭐ 3 · C · MIT · 推送 2026-10-22 · [GitHub](https://github.com/TheProductAgency/flipper-ai-composer) · [官网](https://github.com/TheProductAgency/flipper-ai-composer) · 个人维护

**Flipper Zero 上的离线旋律生成应用：神经网络在设备上逐音符创作**

Flipper Zero 应用（.fap），内置一个 32,834 参数、量化为 8 bit（36.8 KB）的 GRU 网络，在设备上逐音符生成旋律，无需联网或电脑。提供 8 种风格、两种风格按比例混合、五级创造力（采样温度 0.45–1.3）、任意调性与音量调节，生成结果可在屏幕逐音符显示并通过扬声器播放，可存为 .fmf 供内置 Music Player 打开。训练数据由自带规则作曲器生成的 64,000 首旋律构成。仅适配官方固件（release 渠道）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 种风格且可按百分比混合两种风格
- 36.8 KB int8 权重，C 实现在设备端推理，无需联网
- 五级创造力（采样温度）与自由调性、音量设置
- 生成的旋律可保存为 .fmf 并在 Music Player 中播放

## 适用场景

- 在 Flipper Zero 上离线生成并试听新旋律
- 把喜欢的旋律存成 .fmf 在 Music Player 里播放
- 从源码重新训练或导出模型做实验

## 场景标签

 · 领域:嵌入式/音乐生成应用

## 证据(README 行号)

> L3:  A tiny neural network that writes brand-new melodies – on the Flipper Zero itself.
> L4:  No internet, no computer, no samples: every tune is invented note by note on the device.
> L46: 4. **The Flipper runs it.** `composer_model.c` is a small, dependency-free C

## 星数曲线

```mermaid
xychart-beta
    title "TheProductAgency/flipper-ai-composer 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `fc6dc8a1fc9e` · [字段定义](../../DATASET.md)*
