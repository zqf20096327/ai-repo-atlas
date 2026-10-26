# pyfenn/fenn

⭐ 81 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/pyfenn/fenn) · [官网](https://pyfenn.com) · 组织维护

**简化深度学习工作流的 Python 框架：配置/日志/训练器/模板**

面向机器学习/深度学习研究者的 Python 框架，自动处理训练工作流周边事务：YAML 配置自动注入（支持 CLI 覆盖）、统一日志捕获并同步到 W&B/TensorBoard、实验开始/完成/失败的 Discord/Telegram 通知、内置训练器减少样板代码、可分享的实验模板（fenn pull 从 GitHub 仓库下载）以及浏览会话与指标曲线的本地 Web 面板。通过 pip 安装，用 fenn CLI 初始化项目后运行 python main.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 配置自动解析注入并支持 CLI 覆盖
- 日志与实验元数据自动捕获，同步到 W&T/TensorBoard
- 内置训练器与可下载复用的实验模板
- 本地 Web 面板浏览会话、查看损失/准确率曲线、一键运行模板

## 适用场景

- 减少训练脚本中的配置、日志与训练循环样板代码
- 通过模板快速启动可复现的深度学习实验
- 在 Discord/Telegram 接收实验状态通知并集中跟踪指标

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9: Friendly Environment for Neural Networks (fenn) is a simple framework that automates ML/DL workflows by providing pr
> L32: - **Trainers**: Built-in support for training loops, validation, and testing with minimal boilerplate. Just define 

## 星数曲线

```mermaid
xychart-beta
    title "pyfenn/fenn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-26 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2a0828b6fbc3` · [字段定义](../../DATASET.md)*
