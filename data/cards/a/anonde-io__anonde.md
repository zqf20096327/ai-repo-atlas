# anonde-io/anonde

⭐ 19 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/anonde-io/anonde) · [官网](https://anonde.io) · 组织维护

**本地优先的 PII 匿名化/还原工具包，供 LLM 前置脱敏**

Go 编写的开发者工具包，用于在数据进入 LLM 前匿名化个人身份信息（PII），并在许可边界内还原。核心机制：GLiNER 开放集 NER 加约 70 个地区感知的规则识别器，生成稳定可逆令牌，还原调用需 actor+purpose 审计元数据；令牌映射存于内存 vault。支持文本/JSON/PDF（含 OCR）输入，提供 Docker 镜像、Go 库、REST/gRPC/Connect 三种传输及 OpenAI 兼容代理。面向医疗、金融、日志与企业内 copilot 场景，无云端调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GLiNER 开放集 NER + 约 70 个模式识别器，多语言（英德西法意等）
- 可逆令牌化：还原需 actor+purpose，令牌按 (tenant, doc) 稳定
- 单二进制/Docker 自托管，NER 模型内置于镜像，请求时无外部流量
- PDF/扫描件 OCR 自动处理，OpenAI 兼容代理匿名化请求并还原响应

## 适用场景

- 在调用第三方 LLM 前对医疗病历、KYC 材料等做脱敏
- 对应用日志、SIEM 导出中的 PII 化后再送入 LLM 或 BI
- 构建合规的企业内 RAG/copilot，并审计谁在什么目的下还原了明文

## 场景标签

 · 领域:数据安全/LLM 基础设施

## 证据(README 行号)

> L7:  A developer toolkit for building copilots, RAG, and agents over healthcare, finance, and enterprise data.
> L41: - **Drop-in for any LLM workflow.** Same shape in, same shape out. Plug it between your app and OpenAI, Anthropic, 
> L43: - **Local-first.** Ships as a Go library or a Docker image you run yourself. No cloud calls. NER models are baked i

## 星数曲线

```mermaid
xychart-beta
    title "anonde-io/anonde 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `af2f3bc66298` · [字段定义](../../DATASET.md)*
