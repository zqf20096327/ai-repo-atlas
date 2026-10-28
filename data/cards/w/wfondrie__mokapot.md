# wfondrie/mokapot

⭐ 53 · Python · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/wfondrie/mokapot) · [官网](https://mokapot.readthedocs.io) · 组织维护

**蛋白质组学肽段检测的半监督学习 Python 库**

对 Percolator 首创的半监督学习算法的 Python 实现：读取搜索引擎生成的 PSM（Percolator tab-delimited/PIN 或 PepXML 格式），训练分类器估计肽段检测的置信度，支持替换线性 SVM 为梯度提升等非线性分类器、跨实验联合训练并保留各实验有效置信估计，也支持交联质谱数据。提供命令行基础功能与 Python API，由学术作者维护并附发表文献引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Percolator 半监督学习算法的 Python 实现
- 支持非线性分类器（如梯度提升）替换线性 SVM
- 跨实验联合训练且保留每实验置信估计
- 支持 PIN 与 PepXML 格式输入，提供 CLI 与 Python API

## 适用场景

- 对质谱肽段检测结果做半监督置信度重打分
- 在 Python 分析流程中灵活定制分类器与训练策略
- 处理交联质谱等扩展蛋白质组学数据

## 场景标签

 · 领域:生物信息学/蛋白质组学

## 证据(README 行号)

> L3: mokapot is fundamentally a Python implementation of the semi-supervised learning
> L6: swapping Percolator's linear support vector machine classifier for a non-linear,

## 星数曲线

```mermaid
xychart-beta
    title "wfondrie/mokapot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-28 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c3e182898c20` · [字段定义](../../DATASET.md)*
