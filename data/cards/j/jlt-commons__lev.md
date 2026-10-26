# jlt-commons/lev

⭐ 29 · Clojure · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/jlt-commons/lev) · 组织维护

**System 1 决策引擎：对状态回答带校准概率的类型化问题**

运行于 jolt（Clojure on Chez Scheme）之上的决策引擎：接受针对状态的类型化问题，输出经温度校准的概率答案。模型分两类：ModernBERT-large/mmBERT-base 编码器（一次前向覆盖整次调用的问题，笔记本 CPU 约 100ms）； thinker 通过链接的 llama.cpp 加载任意 GGUF 聊天模型，先思考后按 token 对数概率给候选打分。支持置信度门控先走编码器、不确定再升级到 thinker。权重需从 Hugging Face 下载并用 jolt prepare 转换，需编译原生内核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编码器一次前向回答整次调用的问题，CPU 约 100ms，概率经校准
- 置信度门控：编码器先答，不确定的问题升级到 GGUF thinker
- jolt -M:calibrate 按问题类型/选项数分桶重拟合温度，报告 NLL 与 ECE
- 支持 english / typed-decisions / multilingual（100+ 语言）三套检查点

## 适用场景

- 在 CPU 上以低延迟对消息做主题路由等分类决策
- 用大模型 thinker 处理需要推理或弃权的问题
- 对业务工作流（发票、安全事件、客服）做类型化决策

## 场景标签

 · 领域:NLP/机器学习推理

## 证据(README 行号)

> L3: Lev is a System One decision engine which accepts typed questions
> L10: - **the encoders**: ModernBERT-large / mmBERT-base with a decision head,
> L14: - **a thinker**: any GGUF chat model through a linked llama.cpp.

## 星数曲线

```mermaid
xychart-beta
    title "jlt-commons/lev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-26 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ff4c5d46e2f1` · [字段定义](../../DATASET.md)*
