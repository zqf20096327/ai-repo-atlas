# mj-will/nessai

⭐ 50 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/mj-will/nessai) · [官网](https://nessai.readthedocs.io/) · 个人维护

**基于正规化流的嵌套采样算法，用于贝叶斯推断（面向计算昂贵似然）**

nessai 是一个将正规化流（normalising flows）引入嵌套采样的 Python 贝叶斯推断库，面向似然函数计算代价高的应用场景。核心嵌套采样代码基于 cpnest，正规化流实现来自或基于 nflows。支持 pip 与 conda 安装；自 bilby 2.3.0 起推荐通过 nessai-bilby 采样器插件使用，插件支持重要性嵌套采样（inessai）。PyTorch 版本默认不一定匹配系统驱动，需按 PyTorch 官方说明安装对应 CUDA 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 嵌套采样结合正规化流进行贝叶斯推断
- 针对计算昂贵似然的应用场景设计
- 提供 nessai-bilby 插件，支持重要性嵌套采样 inessai
- 正规化流基于 nflows 实现

## 适用场景

- 计算昂贵似然的贝叶斯参数估计
- 通过 bilby 使用 nessai 进行引力波等天文数据分析
- 学术研究中复现论文方法并按 DOI 引用

## 场景标签

 · 领域:科学计算/统计推断

## 证据(README 行号)

> L15: ``nessai`` is a nested sampling algorithm for Bayesian Inference that incorporates normalising flows. It is designe

## 星数曲线

```mermaid
xychart-beta
    title "mj-will/nessai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `92257a44ed5f` · [字段定义](../../DATASET.md)*
