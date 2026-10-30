# gxf1027/randomforests

⭐ 23 · C++ · GPL-2.0 · 推送 2026-08-28 · [GitHub](https://github.com/gxf1027/randomforests) · 个人维护 · 中文 README

**随机森林算法的 C++ 实现：分类、回归与特征分析工具**

随机森林算法的 C++ 实现，供需要将随机森林嵌入自身程序的开发者使用。功能覆盖分类、回归（支持多维输出）、Proximities 与离群值计算、特征重要性评估和缺失值 imputation，支持 3 种随机性模式（Original RF / Near Original / Extra-Trees），使用 OpenMP 加速。提供命令行与嵌入代码（C 风格 C++）两种使用方式，模型可保存为 Plain Text 或 XML 格式并从本地读取。实验部分在 22 个 UCI/libsvm 等数据集上给出 oob 误差结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分类与回归（含多维输出 multi-target regression）
- Proximities、离群值计算、特征重要性与 imputation
- 3 种随机性模式：Original RF / Near Original / Extra-Trees
- 模型可保存/读取，支持 Plain Text 与 XML 两种格式，OpenMP 加速

## 适用场景

- 在 C++ 项目中嵌入随机森林做分类或回归预测
- 评估特征重要性或进行数据 imputation
- 通过命令行训练并保存模型，供后续加载预测

## 场景标签

 · 领域:机器学习/经典算法库

## 证据(README 行号)

> L11: C++ implementation of random forests
> L14: 1. 适用于分类和回归, 支持回归的多维输出（multi-target regression)

## 星数曲线

```mermaid
xychart-beta
    title "gxf1027/randomforests 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f215bbac84b0` · [字段定义](../../DATASET.md)*
