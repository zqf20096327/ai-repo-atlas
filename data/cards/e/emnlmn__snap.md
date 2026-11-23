# emnlmn/snap

⭐ 10 · Rust · MIT · 推送 2026-10-08 · [GitHub](https://github.com/emnlmn/snap) · [官网](https://emnlmn.github.io/snap/) · 个人维护

**本地 LLM 决策引擎：单次前向输出带概率的类型化答案**

面向 LLM 流水线的决策引擎：把每个问题转成以 A–Z 字母为答案的提示，在模型单次前向后读取该位置的 logits 并用 softmax 得到选项概率分布，不生成文本，因此无需解析、重试或清洗。每个问题的答案为一个带完整概率分布的类型化结果，多个问题共享一次批式 llama_decode。以单一二进制分发，内建 llama.cpp，支持 macOS/Linux/Windows，MIT 许可，权重为从 Hugging Face 下载的 GGUF 文件，下载后可离线运行。API 兼容 TypeSafe/Jev 线格式并提供扩展字段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次前向读取 logits 输出类型化答案与完整概率分布，零生成文本
- 共享前缀树与缓存问题头，多问题合入一次批式 llama_decode
- 兼容 TypeSafe/Jev 线格式（POST /v1/systemone），并提供 numeric/allow_abstain/layout 等扩展
- 无文本通道的提示注入缓解设计与 x_snap 执行审计字段

## 适用场景

- 工单分类、事件严重度评级、内容审核裁决等标签判定
- Agent 工具调用执行前的校验检查
- 回答是否忠于上下文的忠实度判定
- 本地离线环境下批量流水线打分与路由

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L16: snap is a decision engine for LLM pipelines. The input is your data plus
> L29: `Z`, one per option. snap runs the model once, reads the logits at that
> L91: `POST /v1/systemone` speaks the TypeSafe/Jev wire format. A client

## 星数曲线

```mermaid
xychart-beta
    title "emnlmn/snap 星数(近 3 点)"
    x-axis ["2026-10-20", "2026-11-10", "2026-11-23"]
    y-axis "stars" 7 --> 11
    line [8, 10, 10]
```

2026-10-20 8 → 2026-11-23 10（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `1c5c4fae30f5` · [字段定义](../../DATASET.md)*
