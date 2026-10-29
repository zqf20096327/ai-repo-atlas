# JehanneDussert/govllm

⭐ 31 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/JehanneDussert/govllm) · [官网](https://arxiv.org/abs/2605.24737) · 个人维护

**自托管 LLM 治理监控平台：面向欧盟 AI Act/GDPR/ANSSI 持续评分**

面向受监管环境（公共部门、医疗、金融）的自托管 LLM 治理监控系统。每个 LLM 响应由本地 LLM-as-a-judge（默认 Ollama 上的 ministral-3:8b）按可配置治理配置文件在 14 项标准上持续评分，标准锚定 EU AI Act、GDPR、ANSSI、OWASP LLM Top 10 等框架；评分矩阵驱动动态路由，按治理标准而非原始性能自动选模型。数据不出本地基础设施。技术栈为三个 FastAPI 微服务 + LiteLLM + Langfuse + Prometheus/Grafana，Docker Compose 部署。附带预印本论文、49 例标注语料与基准测试；judge 有效性（51.5%–69.0% 一致率）与多项实验结果统计上多不显著，身份访问治理配置文件无标注语料、默认关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM-as-a-judge 持续评分，14 项标准锚定监管框架，UI 可配置
- 4 个内置治理配置文件，运行时切换无需重启服务
- 基于治理评分矩阵的动态模型路由，judge 被排除出自动路由并防自我评判
- 全部本地运行：Ollama 推理，无数据外发，可用 Grafana/Prometheus 观测

## 适用场景

- 受监管行业上线 LLM 后按 AI Act 第 9 条做持续风险管理记录
- 按治理标准而非性能指标自动选择各用例的最佳模型
- 离线/内网环境下对 LLM 输出做合规与安全监控

## 场景标签

`LLM 可观测性` `模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L20: govllm scores LLM outputs continuously against configurable governance profiles. Each response is evaluated by a lo
> L23: Request → Governance profile → LLM-as-a-judge scoring → Dynamic routing → Model A / B / C / D
> L169: **Governance from metrics.** Model selection is driven by governance criteria, not performance alone. The score ma

## 星数曲线

```mermaid
xychart-beta
    title "JehanneDussert/govllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c7bbcebe3faa` · [字段定义](../../DATASET.md)*
