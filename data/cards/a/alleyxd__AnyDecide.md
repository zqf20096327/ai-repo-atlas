# alleyxd/AnyDecide

⭐ 41 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/alleyxd/AnyDecide) · 个人维护

**把本地语言模型变成返回类型化概率答案的决策 API 库**

Python 库，基于本地 Hugging Face 对话模型提供决策接口：以选择题、评分、是否等类型化提问，从 next-token 概率直接读出类型化答案与概率，无需解析生成文本；同一输入的多个问题共享单次批量前向传播。附带 FastAPI HTTP 服务、基于少量标注的 Platt scaling/温度偏置校准、以及用 36,194 条决策数据训练 LoRA 的流程。限制：答案编码须为 tokenizer 单 token，改写检测等任务训练后分数下降。面向需把 LLM 用作快速分类/路由组件的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类型化提问（choice/score/yes-no/数值）从 next-token 概率直接读出答案与概率
- 多问题共享单次前向传播，6 问题约 57ms（RTX 5090）
- 几十条标注即可做 Platt scaling/温度偏置校准，降低校准误差
- 内置 LoRA 训练流程：36,194 条来自 15 个公开数据集的决策问答

## 适用场景

- 用本地小模型做快速意图路由、情感/垃圾/毒性分类
- 需要带校准概率、可设阈值的 LLM 决策输出
- 把分类决策部署为 HTTP 服务供其他系统调用

## 场景标签

 · 领域:LLM 应用/分类决策

## 证据(README 行号)

> L7: Turn a local language model into a fast decision API. Instead of generating text you have to parse, you ask typed
> L9: about one input run in a single batched forward pass, and each answer is read straight from the next-token
> L29: ANYDECIDE_MODEL=Qwen/Qwen3-4B uvicorn anydecide.server:app --port 8009

## 星数曲线

```mermaid
xychart-beta
    title "alleyxd/AnyDecide 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-24 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `dd492f356ee5` · [字段定义](../../DATASET.md)*
