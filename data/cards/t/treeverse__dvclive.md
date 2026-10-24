# treeverse/dvclive

⭐ 195 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/treeverse/dvclive) · [官网](https://dvc.org/doc/dvclive) · 组织维护

**Python 库：以文件格式记录并跟踪 ML 指标、参数与模型**

DVCLive 是一个 Python 的 ML 实验记录库，将训练指标、参数、模型以简单文件格式写入磁盘，与 DVC 完全兼容。记录结果可通过 DVC CLI（dvc exp show、dvc plots）、VS Code 的 DVC 扩展或 DVC Studio 进行跨实验比较与可视化。相对其他 ML Logger，其不要求额外服务或服务器，输出为纯文本文件，可被 Git 版本化或以 DVC 指针跟踪，并可将实验保存为隐藏 Git 提交。提供 PyTorch Lightning、Scikit-learn、Ultralytics YOLO v8 等框架集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以纯文本文件格式记录指标、参数与图表，无需额外服务或服务器
- 实验可保存为隐藏 Git 提交，数据可由 Git 版本化或 DVC 跟踪
- 支持 DVC CLI、VS Code DVC 扩展、DVC Studio 三种可视化比较途径
- 提供 PyTorch Lightning / Scikit-learn / Ultralytics YOLO v8 等框架集成

## 适用场景

- 在训练脚本中记录指标并在多次实验间比较
- 用 Git/DVC 对实验指标与参数做版本管理
- 在 VS Code 或 DVC Studio 中实时查看训练更新

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L13: DVCLive is a Python library for logging machine learning metrics and other
> L132: - **DVCLive** does not **require** any additional services or servers to run.

## 星数曲线

```mermaid
xychart-beta
    title "treeverse/dvclive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 194 --> 196
    line [195, 195]
```

2026-10-18 195 → 2026-10-24 195（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cc211d7201e8` · [字段定义](../../DATASET.md)*
