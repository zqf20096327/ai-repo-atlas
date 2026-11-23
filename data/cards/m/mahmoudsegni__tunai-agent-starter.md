# mahmoudsegni/tunai-agent-starter

⭐ 3 · Python · MIT · 推送 2026-11-09 · [GitHub](https://github.com/mahmoudsegni/tunai-agent-starter) · 个人维护

**TunAI API 上的工具调用 agent 参考实现与分步教程**

在 TunAI API 上构建 tool-calling agent 的参考实现，附带分步教程。示例 agent 是一家虚构突尼斯陶瓷网店的客服助手：带引用回答店铺政策、查询订单、精确计算金额、接受语音留言。使用四个端点：chat completions function calling、embeddings、rerank、speech-to-text。代码按模块展示工具 schema、受限步数循环、检索缓存等机制，示例仅依赖官方 openai SDK。安装需 Python 3.10+，从源码 pip 安装。

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

- 工具调用循环：max_steps 步数预算、错误以 JSON 回传模型、tool_choice=none 兜底作答
- embeddings 召回 + rerank 精排的两级检索，向量缓存于 .cache/ 按变更复用
- examples/ 下五个自包含脚本逐步演示流式、工具调用、检索、语音转写
- 通过 OpenAI 兼容 API 与官方 openai SDK 接入

## 适用场景

- 学习在 OpenAI 兼容 API 上实现 function calling agent
- 搭建带引用回答与语音留言的客服问答助手
- 参考受限步数 agent 循环与检索缓存的设计实现

## 场景标签

`RAG` `教程课程` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L7: A reference implementation of a **tool-calling agent** on the TunAI API, with a step-by-step guide. It uses four Tun
> L33: The model never runs anything itself. On each turn it either answers, or replies with **tool calls** (a function na

## 星数曲线

```mermaid
xychart-beta
    title "mahmoudsegni/tunai-agent-starter 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e53eeffdf046` · [字段定义](../../DATASET.md)*
