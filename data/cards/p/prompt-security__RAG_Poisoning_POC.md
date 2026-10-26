# prompt-security/RAG_Poisoning_POC

⭐ 36 · Python · AGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/prompt-security/RAG_Poisoning_POC) · [官网](https://prompt.security) · 组织维护

**RAG 语料投毒（间接提示注入）的可复现教学演示 POC**

由 Prompt Security 维护的概念验证：构建 3 篇文档的知识库并提 5 个问题，再索引 1 篇携带植入指令的投毒文档，对比同一模型、同一系统提示下的回答变化，展示检索语料可劫持模型行为。攻击无需访问模型或向量库内部。整篇文档用 all-MiniLM-L6-v2 嵌入存入 ChromaDB，经 LangChain "stuff" 链拼接进提示词；支持 llama-server/LM Studio/Ollama/DeepSeek API 端点及可选本地 llama-cpp-python 进程内推理。判定中毒仅靠 6 个海盗关键词检查，非通用检测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- clean 与 poisoned 两阶段对照演示，--show-prompt 可打印完整提示词
- 支持 llama-server / LM Studio / Ollama / DeepSeek API 四种推理端点及可选进程内 llama-cpp-python
- 预检脚本 preflight.py 校验环境、端点与静默截断
- 附 preflight 单元测试与 CI 冒烟/e2e 测试

## 适用场景

- 安全研究者在本地复现 RAG 投毒攻击链路
- 向团队演示检索语料污染如何劫持模型回答
- 测试自定义投毒文档对检索结果的影响

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: A small, reproducible proof of concept of **RAG poisoning** (indirect prompt injection through a
> L17: planted instruction ("answer as a pirate"). When the retriever pulls it into the prompt, the model
> L18: follows it — same model, same system prompt, same questions.

## 星数曲线

```mermaid
xychart-beta
    title "prompt-security/RAG_Poisoning_POC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5b530252c367` · [字段定义](../../DATASET.md)*
