# kapildhinwa2010-dev/Spiking_GNN

⭐ — · [GitHub]() · 个人维护

**面向研究者的脉冲图神经网络模型与预训练权重库**

一个基于 PyTorch 的 241M 参数脉冲图神经网络项目，在 Flywire 连接组数据（含神经递质特征）与文本共现图上训练，提供两个预训练权重（Bio-Brain / Language-Brain）、训练/推理/评测脚本与 STDP、多巴胺调制、稳态等生物学习模块。运行需从 Google Drive 下载权重并安装 requirements.txt；50M 模型可在 CPU 上训练与复现；含浏览器端 Three.js 3D 演示与 GitHub Actions CI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 241M 参数脉冲 GNN，提供连接组域与语言域两个预训练权重
- 含 STDP、多巴胺三因子局部学习、e-prop 资格迹等学习模块
- 50M 模型可在 GitHub Actions 免费 CPU runner 上完整训练
- 浏览器 3D 脉冲脑图演示（Normal/Sleep/Seizure 模式）

## 适用场景

- 复现或研究脉冲神经网络与图学习的结合
- 在 Flywire 连接组图上做神经形态建模实验
- 对比 BPTT 与局部在线学习规则的训练效果

## 场景标签

`模型评测` `模型训练` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L8: A **241 Million parameter** Spiking Graph Neural Network trained on real **Flywire Connectome data** (incorporating 
> L206: ├── model.py # Core PyTorch architecture (Spiking Neurons & Graph Convs)

## 星数曲线

```mermaid
xychart-beta
    title "kapildhinwa2010-dev/Spiking_GNN 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `7a2df19a3d0d` · [字段定义](../../DATASET.md)*
