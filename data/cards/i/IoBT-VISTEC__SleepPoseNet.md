# IoBT-VISTEC/SleepPoseNet

⭐ 26 · Jupyter Notebook · 推送 2025-12-02 · [GitHub](https://github.com/IoBT-VISTEC/SleepPoseNet) · 组织维护

**UWB 雷达睡眠体位转换识别研究数据集与论文配套仓库**

IEEE JBHI'2020 论文 SleepPoseNet 的配套仓库，发布两套 UWB 雷达睡眠数据集：Dataset I 含 930 个 16 秒样本（160x180 时序阵列），标注 6 类体位转换标签；Dataset II 含壁挂与天花板两种雷达布置、静态与风扇干扰两种会话，标注 7 类标签。采集自 38 名志愿者，设备为 XeThru X4M03（10Hz）。README 以数据描述为主，未给出模型代码或安装运行方式。

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

- 两套 UWB 雷达睡眠体位数据集（含壁挂/天花板双视角）
- 930 个 16 秒样本，160x180 时序阵列与逐样本标签
- 38 名志愿者、XeThru X4M03 设备（10Hz 帧率）采集

## 适用场景

- 复现或验证睡眠体位转换识别研究
- 作为 UWB 时序人体活动识别的基准数据
- 开展多视角学习方法的实验对比

## 场景标签

 · 领域:生物医学工程/睡眠监测

## 证据(README 行号)

> L6: **Recognizing the movements during sleep is crucial for the monitoring of patients with sleep disorders. However, th
> L9: All data can be downloaded here.

## 星数曲线

```mermaid
xychart-beta
    title "IoBT-VISTEC/SleepPoseNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d388ce7d9f11` · [字段定义](../../DATASET.md)*
