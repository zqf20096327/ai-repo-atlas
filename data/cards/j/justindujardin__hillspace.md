# justindujardin/hillspace

⭐ 17 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/justindujardin/hillspace) · [官网](https://hillspace.justindujardin.com) · 个人维护

**NALU 算术能力研究报告：正文、交互图表与实验源码**

Justin DuJardin 的研究项目，聚合一份报告（markdown 单文件构建为网页与 PDF）、可拖拽交互的 SVG 图表，以及对应各章节的 Python 实验脚本。主题为 NALU（Neural Arithmetic Logic Unit）：论点是其稳定源于选择而非计算。实验脚本枚举权重、训练算术与三角算子并生成报告中的表格，结果数据 checked in 于 results/ 目录。网页构建用 penname + npm，PDF 渲染依赖 uv 与 WeasyPrint；训练日志对接 Weights and Biases。代码 MIT，报告与图表 CC BY 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 markdown 源同时构建网页（含交互图表）与 PDF
- 各实验脚本与报告章节一一对应
- 实验结果数据 checked in，重跑实验后重建表格即更新
- 通用训练器训练报告中全部算术与三角算子并记录到 W&B

## 适用场景

- 阅读并复现 NALU 算术学习行为的实验
- 在自己的数据上重跑 optimizer snapping 等扫描实验
- 参考同一源构建论文网页+PDF 的写作流程

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Source for the report _Stable Because Stuck: NALU Selects, It Doesn't Compute_: the text, the interactive figures, a
> L27: Python 3.10 or newer, managed with uv:

## 星数曲线

```mermaid
xychart-beta
    title "justindujardin/hillspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `4d67a6044a2b` · [字段定义](../../DATASET.md)*
