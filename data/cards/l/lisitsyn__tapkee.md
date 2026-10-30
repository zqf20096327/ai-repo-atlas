# lisitsyn/tapkee

⭐ 236 · C++ · BSD-3-Clause · 推送 2026-10-18 · [GitHub](https://github.com/lisitsyn/tapkee) · [官网](http://tapkee.lisitsyn.me) · 个人维护

**C++ 降维模板库：为开发者提供20余种降维算法**

源自 Shogun 机器学习工具箱（GSoC 2011）的头文件式 C++ 模板库，偏重谱方法，提供 LLE、Isomap、t-SNE、PCA、MDS 等 20 余种降维算法实现。基于 Eigen 线性代数库，可选使用 ARPACK 特征求解器，通过回调接口将算法与数据表示解耦。提供 C++ 方法链 API、Python（pip/nanobind）与 R（Rcpp）绑定，并附带命令行示例程序。构建需 C++20 编译器、Eigen 3.4+ 与 fmt，ARPACK 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 余种降维算法（LLE/Isomap/t-SNE/PCA/MDS 等）
- 回调接口解耦算法与数据存储方案
- 提供 C++/Python/R 三种语言接口
- CoverTree 与 VP-tree 最近邻搜索

## 适用场景

- 在高维数据上做流形学习与降维嵌入
- 将降维能力以头文件形式集成进现有 C++ 代码库
- 在 Python 或 R 中快速调用多种降维算法对比结果

## 场景标签

 · 领域:机器学习/降维

## 证据(README 行号)

> L1: Tapkee is a C++ template library for dimensionality reduction with some bias on
> L5: The project aim is to provide efficient and flexible standalone library for

## 星数曲线

```mermaid
xychart-beta
    title "lisitsyn/tapkee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 235 --> 237
    line [236, 236]
```

2026-10-18 236 → 2026-10-30 236（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1e15e57f7346` · [字段定义](../../DATASET.md)*
