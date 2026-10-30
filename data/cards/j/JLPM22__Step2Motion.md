# JLPM22/Step2Motion

⭐ 20 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/JLPM22/Step2Motion) · [官网](https://vcai.mpi-inf.mpg.de/projects/Step2Motion/) · 组织维护

**从压力鞋垫传感器重建全身运动的研究代码（Eurographics 2026）**

Eurographics 2026 论文 Step2Motion 的官方代码：利用多模态鞋垫传感器（压力+IMU）数据重建全身运动，用于无约束真实环境下的动作捕捉，替代传统动捕服或光学系统。支持 UnderPressure、Step2Motion、Dancing 三个数据集的预处理、预测、指标计算与可视化，附 Unity 可视化工程，并提供训练脚本。需要 Python 3.9+ 与 PyTorch，模型输出 BVH 文件可在 Blender 或 Unity 中查看。

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

- 从鞋垫压力+IMU 数据生成全身运动 BVH 输出
- 支持三个数据集的预处理、预测与论文指标计算
- 提供 Unity 可视化工程（2022.3 测试）与训练脚本

## 适用场景

- 研究者复现论文中的运动重建结果
- 用鞋垫传感器数据进行无标记动作捕捉实验
- 训练新模型并可视化预测与真值对比

## 场景标签

 · 领域:计算机图形学/人体运动捕捉

## 证据(README 行号)

> L14: Step2Motion is a system for reconstructing full-body locomotion from multi-modal insole sensors (pressure + IMU). I
> L127: @article{2026:ponton:step2motion,

## 星数曲线

```mermaid
xychart-beta
    title "JLPM22/Step2Motion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `136a79cc41bb` · [字段定义](../../DATASET.md)*
