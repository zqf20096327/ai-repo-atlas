# Micha0827/snapjudge

⭐ 14 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/Micha0827/snapjudge) · 个人维护

**Apple Silicon 上本地 Qwen 模型的类型化决策引擎**

面向 Mac（Apple Silicon + MLX）的本地决策服务：读取状态文本与问题，直接从模型 next-token logits 读取各允许标签的概率，输出 choice/score/yes-no 结构化决策，不做文本生成。HTTP API 兼容 TypeSafe System One 格式（POST /v1/systemone），附带 prompt 头缓存、标签前缀树与单次批量前向等机制。支持 Qwen 3.5 系列 MLX 4-bit 模型；限制包括概率未证明校准、仅 Apple Silicon、单请求串行处理、长文档弱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 概率直接从 logits 读取，无文本生成与 JSON 解析
- 兼容 TypeSafe System One 格式的 HTTP API（Choice/Score/Noul）
- prompt 头缓存 + 标签前缀树 + 单次批量前向的推理机制
- 附带 /game/ 跑酷演示与 eval 评测脚本

## 适用场景

- 自动化流程中让本地模型做分类/打分/是否判断并按置信度分流
- 在 Mac 上以低延迟获得带概率分布的决策结果
- 用自己的标注数据校准和评测决策模型

## 场景标签

 · 领域:LLM 推理/决策服务

## 证据(README 行号)

> L3: **Typed decisions from local Qwen models on your Mac.** Ask a question about some text, get
> L5: probabilities are read straight from the model's next-token logits.
> L24: reads the probability of each allowed label from a single forward pass. Your code gets a

## 星数曲线

```mermaid
xychart-beta
    title "Micha0827/snapjudge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `35917b99cbc3` · [字段定义](../../DATASET.md)*
