# arclab-hku/DEIO

⭐ 119 · Jupyter Notebook · MIT · 推送 2026-07-07 · [GitHub](https://github.com/arclab-hku/DEIO) · [官网](https://kwanwaipang.github.io/DEIO/) · 组织维护

**首个单目学习型事件-惯性里程计，输出高鲁棒位姿估计**

ICCV 2025 论文的官方代码实现：基于事件相机的循环网络，在时间维度上提供事件块稀疏关联，与 IMU 紧耦合恢复带真实尺度的位姿；利用可微分光束平差（DBA）的 Hessian 信息优化共视因子图，在关键帧滑动窗口内融合事件块对应与 IMU 预积分。作者发布了 10 个公开基准数据集上的估计轨迹（tum 格式）及基于 evo 的评估示例代码。通过 conda 环境安装，需 CUDA 11.7，示例针对 DAVIS240c 等事件相机数据运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 首个单目学习型事件-惯性里程计框架
- 事件循环网络生成事件块稀疏关联并与 IMU 紧耦合
- 利用 DBA Hessian 优化共视因子图（关键帧滑动窗口）
- 公开 10 个基准数据集的估计轨迹与 evo 评估示例代码

## 适用场景

- 在事件相机数据集上运行单目视觉惯性里程计
- 复现论文实验并与 10 个公开基准对比
- 获取 tum 格式轨迹用于其他 SLAM 方法的量化对比

## 场景标签

 · 领域:机器人/SLAM

## 证据(README 行号)

> L9: Event cameras show great potential for visual odometry (VO) in handling challenging situations, such as fast motion 
> L58: @inproceedings{GWPHKU:DEIO,

## 星数曲线

```mermaid
xychart-beta
    title "arclab-hku/DEIO 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 117 --> 120
    line [118, 119, 119]
```

2026-10-18 118 → 2026-10-24 119（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7043c86c8c45` · [字段定义](../../DATASET.md)*
