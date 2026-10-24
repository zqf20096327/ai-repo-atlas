# NLP-LOVE/Model_Log

⭐ 147 · Python · Apache-2.0 · 推送 2026-01-09 · [GitHub](https://github.com/NLP-LOVE/Model_Log) · [官网](http://era.dx3906.info) · 个人维护 · 中文 README

**机器学习训练指标记录与曲线可视化的轻量工具**

基于 Python3 的模型训练评估指标可视化工具：通过三步 API 在训练过程中记录超参数、Loss、Accuracy、Precision、F1 等指标，持久化到 SQLite 本地数据库，由 web 端自动检测训练中的模型并用 Echarts 交互式曲线图呈现，多模型可在同一曲线图中对比，修改过的超参数在表格中高亮显示。支持多用户按昵称隔离数据。与 TensorFlow、PyTorch、PaddlePaddle 结合使用，pip 安装后运行 model-log 命令启动 web 端（默认 5432 端口）。

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

- 三步 API 记录超参数与训练/测试评估指标
- web 端自动检测训练中的模型并可视化（Echarts 曲线图）
- SQLite 存储，多用户按昵称数据隔离
- 表格高亮显示修改过的超参数，便于模型对比

## 适用场景

- 调参时记录多轮训练的超参数与指标并直观对比
- 训练过程中实时查看 Loss/Accuracy 等曲线变化
- 多人共用环境下各自独立记录与分析自己的模型数据

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: Model Log 是一款基于 Python3 的轻量级机器学习(Machine Learning)、深度学习(Deep Learning)模型训练评估指标可视化工具，与 TensorFlow、Pytorch、PaddlePaddl
> L16: - 只需要把模型的超参数和评估指标数据通过API添加即可，轻松三步即可实现。

## 星数曲线

```mermaid
xychart-beta
    title "NLP-LOVE/Model_Log 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-24 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `33eb6bdd338e` · [字段定义](../../DATASET.md)*
