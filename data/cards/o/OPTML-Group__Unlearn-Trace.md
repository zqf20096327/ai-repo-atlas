# OPTML-Group/Unlearn-Trace

⭐ 25 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/OPTML-Group/Unlearn-Trace) · 组织维护

**检测 LLM 是否经过遗忘操作的轨迹识别方法（ICLR 2026 论文代码）**

ICLR 2026 论文《Unlearning Isn't Invisible: Detecting Unlearning Traces in LLMs from Model Outputs》的官方代码库。方法从模型输出中检测机器遗忘（machine unlearning）留下的轨迹：先对 LLM 执行遗忘操作，再生成回答数据并划分训练集，训练分类器判断模型是否被遗忘处理。流程拆分为 Data.md、Unlearn.md、Response.md、Classification.md 等文档，安装说明见 Installation.md，MIT 许可，面向科研复现。

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

- 从 LLM 输出检测机器遗忘轨迹
- 流水线含数据准备、遗忘操作、回答生成、分类器训练与评估四阶段
- ICLR 2026 论文官方代码，MIT 许可

## 适用场景

- 复现论文中的遗忘轨迹检测实验
- 审计 LLM 是否经过遗忘/删除操作
- 可信 AI 与机器遗忘相关研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: This is the official code repository for the ICLR 2026 paper Unlearning Isn't Invisible: Detecting Unlearning Trace
> L13:  Figure 1: Schematic overview of unlearning trace detection.

## 星数曲线

```mermaid
xychart-beta
    title "OPTML-Group/Unlearn-Trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dfc3bf6ee635` · [字段定义](../../DATASET.md)*
