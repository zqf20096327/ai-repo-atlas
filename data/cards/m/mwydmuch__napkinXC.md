# mwydmuch/napkinXC

⭐ 70 · C++ · MIT · 推送 2025-11-10 · [GitHub](https://github.com/mwydmuch/napkinXC) · 个人维护

**极限多类/多标签分类库：实现概率标签树方法**

C++/Python 库，面向极限多类与多标签分类（XMLC），核心实现概率标签树（PLT）与层级 softmax。支持 top-k、阈值等多种推理方式，带标签权重（如 propensity scores）的快速预测，多种建树方法（含层级 k-means），自定义树结构与节点权重，并提供从 XML Repository 下载数据、precision@k 等评测指标的工具。可直接 pip 安装预编译 wheel，或作为可执行文件处理 LIBSVM 格式数据。README 声明库仍在开发中，API 在版本间可能不兼容，部分实验性功能未文档化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PLT 与层级 softmax（HSM）实现，Python 与 C++ 双接口
- 多种推理方式与带 propensity scores 的快速预测
- 内置 XML Repository 数据下载与 precision@k / nDCG@k 等评测工具
- 提供预编译 wheel（Linux/macOS/Windows，Python 3.9+），也可作为可执行文件运行

## 适用场景

- 在超大规模标签数据集上训练多标签分类器
- 复现或开展概率标签树相关论文实验
- 以命令行可执行文件在 LIBSVM 格式数据上训练评测模型

## 场景标签

 · 领域:机器学习/分类

## 证据(README 行号)

> L6: napkinXC is an extremely simple and fast library for extreme multi-class and multi-label classification,
> L10: Right now, napkinXC implements the following features both in Python and C++:

## 星数曲线

```mermaid
xychart-beta
    title "mwydmuch/napkinXC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-24 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b142926d6601` · [字段定义](../../DATASET.md)*
