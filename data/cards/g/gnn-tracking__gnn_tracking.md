# gnn-tracking/gnn_tracking

⭐ 53 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/gnn-tracking/gnn_tracking) · [官网](https://gnn-tracking.rtfd.io/) · 组织维护

**用图神经网络重建粒子径迹的 Python 包（高能物理径迹重建）**

GNN Tracking 项目的主 Python 包：以图神经网络实现带电粒子径迹重建的完整流程，覆盖从数据预处理、模型训练到最终性能指标评估。基于 PyTorch Lightning 构建，通过 hooks 和回调保持模块化，模型可训练与恢复。面向高能物理实验数据处理的研究者与开发者。提供 arXiv 论文（2309.16754、2312.03823）与 demo notebook。安装需先以 micromamba/conda 配置环境文件，再 pip 可编辑安装；采用 CalVer 版本。

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

- 覆盖预处理、模型、性能评估的完整径迹重建流水线
- 基于 PyTorch Lightning，hooks 与回调保持模块化
- 配套 arXiv 论文与 demo notebook
- CalVer 版本管理与 pytest 测试

## 适用场景

- 高能物理实验中重建海量粒子径迹
- 研究 GNN 在粒子径迹重建任务上的表现
- 复现相关论文并扩展径迹重建方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: * 🔋 Batteries included: This repository implements a hole pipeline: from preprocessing to models,
> L13: Detailed write-ups of our progress are available in [arXiv:2309.16754][preprint1] and [arXiv:2312.03823][preprint2]

## 星数曲线

```mermaid
xychart-beta
    title "gnn-tracking/gnn_tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `01ade34570d0` · [字段定义](../../DATASET.md)*
