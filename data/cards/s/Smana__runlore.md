# Smana/runlore

⭐ 20 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Smana/runlore) · 个人维护

**开源 SRE agent：调查事故根因并把经验沉淀为自有知识库**

单一 Go 二进制、部署在用户集群内的 SRE agent：由 Alertmanager webhook、GitOps 失败等事件触发，读取集群、指标、日志与网络流做 ReAct 调查，向 Slack/Matrix 发送带置信度评分的根因卡片；默认只读，仅通过需人工审核的 PR 写入用户自有的 Git 知识库。相同故障再次发生时经检索与对抗性验证后即时召回。LLM 后端可插拔（Anthropic、Gemini、任意 OpenAI 兼容端点如 vLLM/Ollama），另支持作为 MCP server/client。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件触发的 ReAct 调查，输出置信度评分的根因与证据链到 Slack/Matrix
- 每次调查开 PR 沉淀到用户自有 Git 知识库，人工审核合并后可即时召回
- 默认只读，写入仅限经审核的 Git PR；召回需通过结构匹配、边际胜出与战绩加权三道门槛
- 单一 Go 二进制，LLM 后端可插拔（Anthropic/Gemini/OpenAI 兼容端点）

## 适用场景

- SRE 团队让 agent 自动调查告警并给出带证据的根因分析
- 把历次事故经验沉淀为自托管、可迁移的知识库
- GitOps（Flux/Argo CD）环境下把『什么变了』定位到具体 commit

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L18: RunLore is an open-source SRE agent that investigates any incident — *what changed? what's wrong?*
> L33: **First time — a full investigation.** **6 model calls, 79,471 tokens.** A verdict-first card: the

## 星数曲线

```mermaid
xychart-beta
    title "Smana/runlore 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0d0b33ee9409` · [字段定义](../../DATASET.md)*
