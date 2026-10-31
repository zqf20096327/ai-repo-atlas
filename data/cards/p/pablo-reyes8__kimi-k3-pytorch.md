# pablo-reyes8/kimi-k3-pytorch

⭐ 14 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/pablo-reyes8/kimi-k3-pytorch) · 个人维护

**纯 PyTorch 从零复现 Kimi K3 架构的研究实现与训练框架**

面向研究者的 Kimi K3 核心机制独立复现项目：以模块化 PyTorch 代码重建 Kimi Delta Attention、Gated MLA、3:1 混合骨干与 Stable LatentMoE 等结构，并含 MoonViT 视觉编码、MTP、渐进式上下文训练与缓存自回归推理。通过严格 YAML profile（data/model/training 三件套）将实验从 CPU 冒烟测试（0.05M）阶梯式扩展到 2.8T 规范拓扑元数据；支持 DDP/TP/EP 分布式启动。声明与 Moonshot AI 无关联，不提供训练权重。需 Python 3.10+，源码 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现 KDA、Gated MLA、Stable LatentMoE 等核心组件
- YAML profile 阶梯覆盖 0.05M CPU 到 2.8T 规范拓扑元数据
- 支持 DDP、complete-head TP、MoE EP 分布式训练
- 原生 KDA/MLA 缓存解码与 MoonViT 多模态路径

## 适用场景

- 在单张 T4/消费级 GPU 上复现和验证前沿架构机制
- 研究 KDA/MLA/MoE 等组件的从零实现与行为测试
- 通过 YAML profile 组织可复现的缩放实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L11: Kimi-K3 Mini is a pure-PyTorch reproduction of the core architectural, training, and inference mechanisms introduce
> L13: This is not just a Transformer renamed after Kimi. The repository delivers a faithful, from-scratch reconstruction 

## 星数曲线

```mermaid
xychart-beta
    title "pablo-reyes8/kimi-k3-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d611e266dd14` · [字段定义](../../DATASET.md)*
