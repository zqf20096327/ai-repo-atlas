# anton-jeran/FAST-RIR

⭐ 184 · Python · AGPL-3.0 · 推送 2026-03-19 · [GitHub](https://github.com/anton-jeran/FAST-RIR) · [官网](https://anton-jeran.github.io/FRIR/) · 个人维护

**神经网络房间脉冲响应生成器：给定房间参数快速生成 RIR**

ICASSP 2022 论文的官方实现，基于 StackGAN 架构的生成对抗网络，按房间尺寸、听者/声源位置、混响时间等条件生成矩形声学环境的房间脉冲响应（RIR），可下载预训练模型直接生成，也提供训练流程（训练数据由 Diffuse Acoustic Simulator 生成）。生成范围有明确限制：房间 8-11m × 6-8m × 2.5-3.5m，混响时间 0.2s-0.7s。README 顶部说明作者毕业后失去 Google Drive 访问权，数据和模型下载脚本可能失效，需社区补档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按房间尺寸、声源/听者位置、混响时间条件生成 RIR
- 提供预训练模型下载与训练流程
- 训练数据基于 Diffuse Acoustic Simulator 合成
- 后续工作 MESH2IR（任意 3D 网格场景）与 Speech2IR 已开源

## 适用场景

- 为语音识别/语音增强训练合成混响数据增强
- 快速生成指定房间几何条件下的房间脉冲响应
- 声学仿真研究中复现 ICASSP 2022 论文结果

## 场景标签

 · 领域:声学/语音信号处理

## 证据(README 行号)

> L9: This is the official implementation of our neural-network-based fast diffuse room impulse response generator (**FAST
> L53: python3 main.py --cfg cfg/RIR_eval.yml --gpu 0

## 星数曲线

```mermaid
xychart-beta
    title "anton-jeran/FAST-RIR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 183 --> 185
    line [184, 184]
```

2026-10-18 184 → 2026-10-26 184（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d5903be19b1c` · [字段定义](../../DATASET.md)*
