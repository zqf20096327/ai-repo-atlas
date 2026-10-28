# sonoisa/code2vec

⭐ 30 · Python · MIT · 推送 2026-02-05 · [GitHub](https://github.com/sonoisa/code2vec) · 个人维护

**code2vec 论文的 PyTorch 复现：学习代码的分布式表示**

论文 "code2vec: Learning Distributed Representations of Code" 的第三方实现：以 AST 路径与终端节点为输入，通过注意力机制聚合并训练代码嵌入，最终生成代码向量文件（code.vec）。依赖 Python 3.6+、PyTorch 1.1+ 与 scikit-learn，tensorboardX 为可选。提供命令行训练入口 main.py，支持小数据集与 top11 大数据集两种训练配置，需自行准备 corpus/path_idxs/terminal_idxs 格式的数据。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 AST 路径与终端节点训练代码分布式表示
- 生成代码向量文件（code.vec）供下游使用
- 提供小数据集与 top11 大数据集两组训练命令示例

## 适用场景

- 复现 code2vec 论文方法并训练自己的代码嵌入
- 研究代码表示学习时获得可运行的 PyTorch 基线
- 为源码分析任务生成代码向量

## 场景标签

 · 领域:源码分析/机器学习

## 证据(README 行号)

> L2: an implementation of "code2vec: Learning Distributed Representations of Code"
> L15: python main.py --lr 0.01 --corpus_path ./dataset/corpus.txt --path_idx_path ./dataset/path_idxs.txt --terminal_idx_

## 星数曲线

```mermaid
xychart-beta
    title "sonoisa/code2vec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1462bf6ea127` · [字段定义](../../DATASET.md)*
