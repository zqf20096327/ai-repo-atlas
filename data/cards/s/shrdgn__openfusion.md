# shrdgn/openfusion

⭐ 34 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/shrdgn/openfusion) · 个人维护

**开源复合模型代理：将请求并发分发至多模型面板并由裁判模型合成单一回答**

基于 FastAPI 的 OpenAI 兼容代理：把 model=openfusion 的请求并行发给一组面板 LLM，再由裁判模型读取全部回答（共识/矛盾/盲点）合成单一答案并以 SSE 流式返回。面板、裁判、策略（self_fusion/panel/debate/pipeline）、聚合器（judge/vote/ranked）、可选 Auto Router、限流与成本预估均通过 openfusion.yaml 配置。上游默认 OpenRouter，也支持 OpenAI/Together/本地 vLLM/Ollama 及原生 Anthropic Messages API。提供终端聊天、Web playground 与 Docker 镜像，自述为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 面板并行调用 + 裁判模型合成，SSE 流式输出
- 四种策略：self_fusion/panel/debate/pipeline，三种聚合器：judge/vote/ranked
- 每个面板成员为 {base_url, api_key, model}，支持原生 Anthropic Messages API
- Auto Router 按提示难度决定单模型或融合，含 EMA 结果学习（仅内存）

## 适用场景

- 让 Cursor/OpenAI SDK 等工具直接获得多模型融合回答
- 研究/比对/综合类任务上用面板+裁判获得合成答案
- 自托管一个可配置策略与限流的多模型网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: An open-source, drop-in compound-model proxy. Point any OpenAI-compatible tool at it,
> L220: - **Drop-in.** OpenAI-compatible `POST /v1/chat/completions` + `/v1/models`, real SSE streaming,
> L222: - **No lock-in.** Each panel member + judge is `{base_url, api_key, model}`. OpenRouter is the

## 星数曲线

```mermaid
xychart-beta
    title "shrdgn/openfusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0d757f8e5bda` · [字段定义](../../DATASET.md)*
