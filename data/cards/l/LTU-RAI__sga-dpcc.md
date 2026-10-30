# LTU-RAI/sga-dpcc

⭐ 24 · Python · MIT · 推送 2026-01-05 · [GitHub](https://github.com/LTU-RAI/sga-dpcc) · 组织维护

**基于语义场景图的深度点云压缩框架（RA-L'25 论文）**

面向多机器人系统 3D 点云传输的深度压缩研究代码：将点云分解为语义一致的 patch，用 FiLM 条件化的语义感知编码器编码为紧凑隐表示，折叠式解码器结合图节点属性重建点云，数据量最高缩减 98%。在 SemanticKITTI 与 nuScenes 上实验，支持多机器人位姿图优化与地图合并等下游应用。提供训练、推理、仅编码与仅解码工作流，Python 3.8+ 环境，CUDA GPU 推荐用于训练，预训练权重从 Google Drive 下载，配置中第 3/4 层与论文顺序相反。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 点云分解为语义 patch，FiLM 条件化编码 + 折叠式解码重建
- 数据量最高缩减 98%，保留结构与语义保真
- 支持 encode-only / decode-only 传输工作流与 Chamfer 距离评估
- 提供多 GPU torchrun 分布式训练

## 适用场景

- 机器人在带宽受限环境下压缩传输 LiDAR 点云
- 复现论文在 SemanticKITTI/nuScenes 上的压缩实验
- 多机器人位姿图优化与地图合并的压缩数据输入

## 场景标签

 · 领域:机器人/3D 视觉

## 证据(README 行号)

> L14: **Abstract:** Efficient transmission of 3D point cloud data is critical for advanced perception in centralized and 
> L161: The `test/predict.py` script performs point cloud compression inference using the pre-trained autoencoder models. 
> L267:   journal={IEEE Robotics and Automation Letters},

## 星数曲线

```mermaid
xychart-beta
    title "LTU-RAI/sga-dpcc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `534fcea1d758` · [字段定义](../../DATASET.md)*
