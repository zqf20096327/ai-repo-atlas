# boris-kz/CogAlg

⭐ 101 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/boris-kz/CogAlg) · [官网](https://boris-kz.github.io/CogAlg/) · 个人维护

**自底向上层级聚类模式发现算法的实验实现**

作者自称『认知算法（Cognitive Algorithm）』的草案级实现：从像素出发做横向交叉比较（生成 match 与 miss），再按连接度聚成簇，逐级递归形成『模式的模式』的层级结构；不随机化、不直接训练参数，反馈仅调整超参数，相似度以相对压缩（Jaccard）定义。作者将 Hebbian 学习、CNN、transformer 自注意力等统一解释为交叉比较与聚类的变体。项目定位为开放研究，招募设计与实现贡献并付费，内容以 CC BY 4.0 发布；README 声明代码未完成前测试几乎无用，未给出安装运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从像素到高层表示的自底向上递归聚类流程（agg_recursion）
- 以投影模型-环境对应为目标函数，反馈只调超参数、不做参数训练、不随机化
- 相似度定义为相对输入压缩（Jaccard），同时计算相似性与差异
- 对 Hebbian/CNN/transformer 的统一比较论述

## 适用场景

- 研究无监督模式发现与层级聚类的替代范式
- 阅读作者对现有 ML 方法的理论分析
- 参与开放算法设计与实现并获取报酬

## 场景标签

 · 领域:机器学习算法研究/计算机视觉

## 证据(README 行号)

> L3: This is a draft algorithm for primarily bottom-up hierarchical clustering, from pixels to eternity. My objective fun
> L6: My process starts with lateral cross-comparison of original inputs, followed by summing them into match-defined clus
> L50: |_integer_ pixels|SUB|_binary:_ direction of comparison|blobs of gradient|edge detection, flood fill|

## 星数曲线

```mermaid
xychart-beta
    title "boris-kz/CogAlg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-24 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `5bf4828e0d05` · [字段定义](../../DATASET.md)*
