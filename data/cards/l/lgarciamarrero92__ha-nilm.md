# lgarciamarrero92/ha-nilm

⭐ 55 · HTML · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/lgarciamarrero92/ha-nilm) · [官网](https://ha-nilm.bigwicho.com/) · 个人维护

**Home Assistant 本地 NILM：从总电表推测各电器活动与能耗**

面向 Home Assistant 用户的无侵入负荷监测（NILM）工具，由两个服务组成：NILM 推理服务监控总电表传感器，实时发布各电器的功率、累计能耗与开关状态实体；NILM Training Server 在引导式训练阶段从 Home Assistant 历史数据学习电器模式，返回训练后的嵌入与阈值。支持以 Home Assistant OS 应用或 Docker 容器部署，全流程本地运行。限制：训练范围仅限前 7 天历史，实时实体约每 8 秒更新，输出为估算值而非分电器计量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一总电表传感器推测各电器活动、能耗与占比
- 训练与推理分离：训练完成后可停用训练服务仅保留推理
- 支持分相/多相供电的多个总电表传感器
- 本地运行，实体可直接用于仪表盘、自动化与能源面板

## 适用场景

- 不想给每台设备装计量插座，用总电表估算各电器用电
- 在 Home Assistant 仪表盘查看各电器实时开关与能耗占比
- 训练自家电器模型后接入自动化与能源工作流

## 场景标签

 · 领域:智能家居/能源监测

## 证据(README 行号)

> L11: HA-NILM learns your appliance patterns during a short guided training phase, then uses them to estimate real-time a
> L49: - Runs live NILM inference.
> L144: - `NILM Training Server` handles heavier ML training workloads.

## 星数曲线

```mermaid
xychart-beta
    title "lgarciamarrero92/ha-nilm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 53 --> 56
    line [54, 55, 55]
```

2026-10-18 54 → 2026-10-24 55（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e1c3c211a819` · [字段定义](../../DATASET.md)*
