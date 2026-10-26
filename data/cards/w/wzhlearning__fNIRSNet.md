# wzhlearning/fNIRSNet

⭐ 36 · Python · Apache-2.0 · 推送 2026-05-23 · [GitHub](https://github.com/wzhlearning/fNIRSNet) · [官网](https://ieeexplore.ieee.org/document/10311392) · 个人维护

**面向 fNIRS 脑机接口分类的 CNN 模型 PyTorch 代码库**

论文 Rethinking Delayed Hemodynamic Responses for fNIRS Classification（IEEE TNSRE）的官方代码实现：将延迟血流动力学响应作为领域知识引入 fNIRS 分类，提出 CNN 模型 fNIRSNet 并总结三条设计准则。提供在 MA 与 UFFT 两个公开 fNIRS 数据集上的数据转换脚本，以及 KFold-CV 与 LOSO-CV 两种训练/评估脚本，含标签平滑与数据加载模块。训练前需自行下载数据集并指定路径，README 未给出依赖安装命令。面向脑机接口方向的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fNIRSNet 模型代码（考虑延迟血流动力学响应的 CNN）
- MA 与 UFFT 两个公开 fNIRS 数据集的转换与加载脚本
- KFold-CV 与 LOSO-CV 训练及结果评估脚本

## 适用场景

- 复现论文中 fNIRS 分类实验结果
- 在公开 fNIRS 数据集上做交叉验证训练与评估
- 基于 fNIRSNet 开发脑机接口分类方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L17: Currently, deep neural networks do not consider the inherent delayed hemodynamic responses of fNIRS signals, which 
> L63: ***fNIRSNet.py*** : Code for the proposed fNIRSNet.

## 星数曲线

```mermaid
xychart-beta
    title "wzhlearning/fNIRSNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ab847982e38b` · [字段定义](../../DATASET.md)*
