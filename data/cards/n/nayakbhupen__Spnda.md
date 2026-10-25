# nayakbhupen/Spnda

⭐ 33 · Python · NOASSERTION · 推送 2026-09-17 · [GitHub](https://github.com/nayakbhupen/Spnda) · [官网](https://doi.org/10.5281/zenodo.22233648) · 个人维护

**LLM 认知不确定性与幻觉检测库，零依赖、微秒级计算**

面向 LLM 生产服务的认知不确定性量化与幻觉检测工具：以精确匹配归一化熵指标 R_sc 替代基于 NLI 交叉编码器的语义熵聚类，对 K 条采样答案做词法等价类划分并计算风险分数，纯 Python 标准库实现、零第三方依赖；另提供 Rust 引擎（需 cargo 编译）形式的 OpenAI 兼容反向代理网关，输出 Prometheus 指标与决策 header。限制：不适用于开放式自由文本（README 建议改用神经语义熵），且在大模型无接地事实任务上存在 Confident Mode Collapse 风险，需配合 RAG。采用 MIT（Python SDK）与 BSL 1.1（Rust 引擎，2030 年转 Apache 2.0）双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- R_sc 指标对采样答案做词法等价类熵计算，无需 NLI 模型与 GPU
- spanda.wrap 一行封装 OpenAI/Groq/Ollama 等客户端，自动多路采样与幻觉拦截
- Rust 网关提供 OpenAI 兼容代理、Prometheus /metrics 与健康探针
- 提供 LangChain/LlamaIndex/LiteLLM 集成与 Docker 部署

## 适用场景

- 生产 API 中对模型输出做微秒级幻觉与不确定性检测
- 在高吞吐网关层按风险分数拦截发散回答
- 为 RAG 与 agent 工具调用参数做级联安全护栏

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L12: *Detect LLM hallucinations and quantify uncertainty in microseconds without secondary NLI cross-encoders.*
> L102: Wrap any standard OpenAI, Groq, Ollama, or OpenAI-compatible client with transparent multi-path epistemic uncertai
> L183: - `GET /metrics`: Standard Prometheus format for Grafana (`spanda_requests_total`, `spanda_evaluations_total`, `sp

## 星数曲线

```mermaid
xychart-beta
    title "nayakbhupen/Spnda 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `12d7db478128` · [字段定义](../../DATASET.md)*
