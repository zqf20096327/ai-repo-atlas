# manjunathshiva/opendecider

⭐ 36 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/manjunathshiva/opendecider) · [官网](https://manjunathshiva.github.io/opendecider/) · 个人维护

**开放校准的 System 1 决策模型：为每个选项输出概率**

提供 400M–80B 的 System 1 决策模型（nano 0.8GB、small 4B 等），对任意状态（文本、工单、JSON）回答 choice/score/yes-no 类型问题，并为每个选项给出校准概率。以 Python 库、opendecider serve 服务器（兼容 TypeSafe Jev 的 /v1/systemone 协议）、MCP 服务器形式交付；支持 CPU、NVIDIA、Apple Silicon，以及 LM Studio/Ollama/vLLM 运行 GGUF 或 LoRA 版本。并提供 LangGraph、CrewAI 等多框架路由集成。限制：Ollama 自带 /v1/systemone 的 prompt 与本模型不同会损失约 9 个点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- choice/score/noul 类型问题输出每个选项的校准概率
- nano 在 NVIDIA GPU 上 17ms、Mac 上 18ms 的响应
- GGUF 构建可运行于 LM Studio/Ollama，vLLM 以 LoRA 适配器方式服务
- MCP 服务器与 LangGraph/CrewAI/Google ADK 等 9 类 agent 框架的路由集成

## 适用场景

- 按置信度自动分流工单到对应团队或 agent
- agent 工作流中用毫秒级路由替代 LLM 调用做分类决策
- 对大批状态批量做类型化判断（batch API）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Open, calibrated System 1 decision models.** Ask typed questions (`choice`, `score`, `noul`) about any state (text
> L49: model = load("manjunathshiva/opendecider-nano")   # 0.8 GB, downloaded on first use; "…/opendecider-small" for the 

## 星数曲线

```mermaid
xychart-beta
    title "manjunathshiva/opendecider 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-26"]
    y-axis "stars" 33 --> 37
    line [34, 35, 36, 36]
```

2026-10-18 34 → 2026-10-26 36（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a39e794a2bb7` · [字段定义](../../DATASET.md)*
