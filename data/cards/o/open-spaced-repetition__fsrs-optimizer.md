# open-spaced-repetition/fsrs-optimizer

⭐ 112 · Python · BSD-3-Clause · 推送 2026-08-06 · [GitHub](https://github.com/open-spaced-repetition/fsrs-optimizer) · [官网](https://pypi.org/project/FSRS-Optimizer/) · 组织维护

**用个人复习日志训练 FSRS 记忆调度算法参数的 Python 库**

Python 库，读取符合标准 schema 的间隔重复复习日志（卡片 ID、复习时间、评分、状态、耗时、时区等），对 FSRS 算法的参数进行训练优化，输出适配用户个人记忆特征的调度参数。定位是为多种编程语言的 FSRS 实现提供统一优化器，并统一各间隔重复软件的学习数据格式，使学习者在不同平台获得一致的复习安排。附带 CLI，直接对 revlog.csv 运行即可完成优化；README 提及不装 torch 的替代品 fsrs-rs-python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按标准化 review_logs schema 读取个人复习日志并优化 FSRS 参数
- CLI 一条命令处理 revlog.csv（python -m fsrs_optimizer）
- 面向多语言 FSRS 实现的统一优化器与复习日志数据标准

## 适用场景

- 用自己的 Anki 等复习记录调出个人化的 FSRS 参数
- 各平台 FSRS 实现接入统一的参数优化工具
- 以标准 schema 归并不同间隔重复软件的学习数据

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: The FSRS Optimizer is a Python library capable of utilizing personal spaced repetition review logs to refine the FSR
> L7: Delve into the underlying principles of the FSRS Optimizer's training process at: https://github.com/open-spaced-rep

## 星数曲线

```mermaid
xychart-beta
    title "open-spaced-repetition/fsrs-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-23 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `c92f894e7860` · [字段定义](../../DATASET.md)*
