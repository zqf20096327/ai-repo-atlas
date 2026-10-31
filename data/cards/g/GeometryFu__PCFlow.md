# GeometryFu/PCFlow

⭐ 14 · Python · Apache-2.0 · 推送 2026-09-12 · [GitHub](https://github.com/GeometryFu/PCFlow) · 组织维护

**为探地雷达 B-scan 合成提供物理条件流匹配生成框架**

面向探地雷达（GPR）研究者的 B-scan 图像合成框架：将 gprMax .in 场景文件解析为介电常数、电导率与几何图，构建 26 通道 Maxwell 物理条件，用条件 U-Net 学习 rectified flow 速度场，经 Euler/Heun 求解器积分 ODE 并通过 SDXL VAE 解码生成雷达图，用于数据增强，替代耗时数分钟到数小时的数值仿真。内置 800 场景配对数据集，训练主预设 5 万步。需 Python 3.10+、PyTorch 2.1+，推荐 CUDA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Maxwell 物理条件场引导的 flow matching 生成 B-scan 图像
- 从 gprMax .in 场景构建 26 通道物理条件
- 内置 800 场景配对数据集并支持自定义数据集索引构建
- 支持 EMA、AMP、断点续训与 Euler/Heun 求解器

## 适用场景

- 为 GPR 检测模型快速生成带物理一致性的仿真雷达图数据
- 替代传统 gprMax 数值仿真以缩短数据生成时间
- 基于自定义场景配置批量扩充训练数据

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: 🔥 **PCFlow** is a framework for fast Ground-Penetrating Radar (GPR) B-scan synthesis, based on Maxwell-informed cond
> L98: The sampler rebuilds a physics condition from the scene, uses EMA weights when available, integrates the rectified-

## 星数曲线

```mermaid
xychart-beta
    title "GeometryFu/PCFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `b795e5aa9093` · [字段定义](../../DATASET.md)*
