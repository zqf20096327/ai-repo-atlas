# PaddlePaddle/Paddle-Inference-Demo

⭐ 269 · C++ · Apache-2.0 · 推送 2025-11-20 · [GitHub](https://github.com/PaddlePaddle/Paddle-Inference-Demo) · 组织维护 · 中文 README

**Paddle Inference 推理引擎的 C++/Python 部署示例集**

PaddlePaddle 官方维护的示例仓库，演示如何使用飞桨核心推理引擎 Paddle Inference 部署模型。内容按语言分为 python 与 c++ 两个目录：Python 侧以真实输入方式提供图像分类、分割、检测及 Ernie/Bert 等 NLP 示例；C++ 侧以单测形式覆盖同类任务，两者均含 Paddle-TRT 与多线程用法示例。面向已了解 Paddle Inference 的开发者，新人需先阅读官方入门文档；使用 2.0 以前版本需参考 release/1.8 分支。

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

- 提供 C++ 与 Python 双语言的推理部署示例
- 覆盖图像分类、分割、检测与 Ernie/Bert NLP 任务
- 包含 Paddle-TRT 与多线程使用示例

## 适用场景

- 学习如何在服务器端部署飞桨训练的模型
- 参考 Paddle-TRT 和多线程推理的接入写法
- 查找分类/分割/检测/NLP 任务的推理代码模板

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Paddle Inference为飞桨核心框架推理引擎。Paddle Inference功能特性丰富，性能优异，针对服务器端应用场景进行了深度的适配优化，做到高吞吐、低时延，保证了飞桨模型在服务器端即训即用，快速部署。
> L5: 为了能让广大用户快速的使用Paddle Inference进行部署应用，我们在此Repo中提供了C++、Python的使用样例。

## 星数曲线

```mermaid
xychart-beta
    title "PaddlePaddle/Paddle-Inference-Demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-26 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a3f70a8f200a` · [字段定义](../../DATASET.md)*
