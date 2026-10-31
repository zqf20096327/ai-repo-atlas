# InCogNiTo124/knarrow

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/InCogNiTo124/knarrow) · [官网](https://knarrow.readthedocs.io/en/latest/) · 个人维护

**检测数据序列拐点(knee point)的 Python 库，含 CLI**

knarrow 是一个用多种方法检测曲线拐点(knee point)的 Python 库：输入 list、tuple 或 numpy 数组，通过 find_knee 函数返回拐点索引。提供 pip 安装，安装 cli 扩展后附带命令行工具，可从 stdin 读取数据。README 列出实现类似功能的项目 mariolpantunes/knee。项目基于 python-blueprint 脚手架构建。

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

- find_knee 函数接受 list/tuple/np.ndarray 输入并返回拐点索引
- 多种方法检测拐点
- pip 安装 cli 扩展后附带命令行工具，支持 stdin 输入

## 适用场景

- 在肘部法则场景确定聚类或超参数选择的关键点
- 从文本数据流中快速检测拐点

## 场景标签

 · 领域:数值分析/机器学习工具

## 证据(README 行号)

> L17: Detect knee points in various scenarios using a plethora of methods
> L20: Just plug in your values in a `list`, `tuple` or an `np.ndarray` and watch `knarrow` hit the knee:

## 星数曲线

```mermaid
xychart-beta
    title "InCogNiTo124/knarrow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `83662aef5ed5` · [字段定义](../../DATASET.md)*
