# nityansuman/marvin

⭐ 121 · CSS · GPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/nityansuman/marvin) · 个人维护 · 中文 README

**Flask Web 考试系统：用 NLP 自动生成题目并评分**

基于 Python、Flask、NLTK 与 Web 技术构建的自动化考试 Web 应用：通过机器学习与自然语言处理自动生成主观或客观题及对应答案，并在无人工干预的情况下评估考生作答，文本相似度相关标签表明其答案比对机制依赖文本相似度计算。面向需要降低出题与阅卷人力成本的考试场景。安装方式为 git clone 源码后用 Anaconda 建环境、下载 NLTK 数据、运行 runserver.py 启动，属毕业设计性质项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动生成主观/客观题及对应答案
- 无人工干预地评估考生作答
- Flask Web 架构，含登录与成绩界面

## 适用场景

- 教师自动出题生成试卷
- 在线考试后自动批改主观题答案
- 降低考试组织与阅卷的人力成本

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: We implement a model to automatically generate questions with their respective answers and
> L34: >>> nltk.download("all")

## 星数曲线

```mermaid
xychart-beta
    title "nityansuman/marvin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-25 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3b895558d2ea` · [字段定义](../../DATASET.md)*
