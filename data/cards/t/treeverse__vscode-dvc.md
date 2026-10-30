# treeverse/vscode-dvc

⭐ 220 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/treeverse/vscode-dvc) · [官网](https://marketplace.visualstudio.com/items?itemName=lakefs.lakefs-dvc) · 组织维护

**VS Code 扩展：在 IDE 内追踪与可视化 DVC 管理的 ML 实验**

为 VS Code 提供的 DVC 扩展：在 IDE 中运行、比较、可视化基于 Git 的机器学习实验，记录训练数据、参数与指标，支持实时指标追踪、可定制绘图仪表盘、实验表格编辑器，以及通过 DVC Tracked 面板与 Source Control 面板管理大型数据集与模型文件的版本和远程存储同步。面向使用 DVC 做实验管理与数据版本控制的 ML 开发者，需本机存在 DVC 二进制（或通过 Microsoft Python 扩展的环境定位 dvc 包），无需额外服务或数据库，遥测数据发送至 Azure 且可随 VS Code 设置关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Git 的实验追踪：记录数据、参数与指标并比较实验结果
- 可定制绘图仪表盘与实时指标追踪
- DVC Tracked 面板管理数据文件状态并与远程存储同步
- 与 Microsoft Python 扩展集成定位 DVC 解释器

## 适用场景

- 在 VS Code 内比较多次训练实验的指标与图表
- 对大型数据集与模型文件做版本管理并同步到远程存储
- 按 Git 提交恢复或重置项目版本以保证实验可复现

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L17: Run, compare, visualize, and track machine learning experiments right in VS
> L27: - **Experiment tracking**: Record training data, parameters, and metrics on top
> L35: - **Data Management**: Handle and version large datasets, files, and models

## 星数曲线

```mermaid
xychart-beta
    title "treeverse/vscode-dvc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 219 --> 221
    line [220, 220]
```

2026-10-18 220 → 2026-10-30 220（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `eef0cb127cc0` · [字段定义](../../DATASET.md)*
