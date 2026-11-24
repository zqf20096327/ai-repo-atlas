# OmniJev/Flide

⭐ 553 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/OmniJev/Flide) · [官网](https://flide.org) · 组织维护 · 中文 README

**Jev 式决策模型的快速推理引擎，支持精确状态分叉**

面向 Jev 式决策模型的 GPU 推理基础设施：通过精确状态分叉（exact state forking）将一个状态分叉为多个问题并在单次前向传播中作答，服务 Jev /v1/systemone API。README 称其比 vLLM 和 SGLang 快至多 9.5 倍，支持 40 余个决策/聊天模型家族（含文本、图像、视频输入），提供会话缓存、批不变、FP8 量化等选项。需 NVIDIA GPU，运行于 Linux 或 Windows WSL2，Apache-2.0 许可，附 arXiv 论文。

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

- 精确状态分叉：一个状态分叉多个问题，单次前向传播作答
- 支持 40 余个决策模型家族（部分支持图像/视频输入）
- 支持 FP8 量化，Gemma 4 12B 可装入单张 24GB 显卡
- 提供会话状态缓存与批不变模式选项

## 适用场景

- 部署决策模型并以 /v1/systemone API 提供服务
- 批量问题解答场景（如邮件分拣 demo：H200 上 10,000 封邮件 28 秒）
- Agent 多步流程中复用会话状态降低推理开销

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L15: Flide is fast inference infrastructure for Jev-style decision models. With exact state forking it is up to 9.5 time
> L46: Flide runs on an NVIDIA GPU under Linux or Windows WSL2. See the docs for every model, images, the API and all opti

## 星数曲线

```mermaid
xychart-beta
    title "OmniJev/Flide 星数(近 18 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-24"]
    y-axis "stars" 0 --> 608
    line [3, 4, 7, 8, 29, 358, 445, 475, 489, 501, 508, 525, 538, 543, 545, 550, 553, 553]
```

2026-10-29 3 → 2026-11-24 553（+550）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `c79c852a6259` · [字段定义](../../DATASET.md)*
