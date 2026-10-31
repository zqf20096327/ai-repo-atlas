# THREATRADAR-Pipeline/ThreatRadar

⭐ 21 · Python · MIT · 推送 2026-05-24 · [GitHub](https://github.com/THREATRADAR-Pipeline/ThreatRadar) · 组织维护

**面向 SOC 的威胁情报流水线：AI 检测投毒 IOC 并推送 MISP**

由 Docker 微服务组成的端到端威胁情报处理流水线，服务于安全运营中心与威胁情报团队。流程为：从 NVD、OTX、AbuseIPDB 等多源摄取 IOC，归一化到 7 类 Elasticsearch 索引，经 Cortex 分析器（VirusTotal 等 6 个服务）富化与打分，再用 IsolationForest 异常检测与 LLM（OpenRouter 接入）按 8 类矛盾规则语义校验，判定情报是否被投毒，随后推送 MISP 并依据分析师生成反馈增量重训模型。需自建 Elasticsearch/Cortex/MISP 栈并配置多个 API key，Windows 仅支持 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IsolationForest 异常检测 + LLM 按 8 类矛盾规则语义校验 IOC 投毒
- Cortex 编排 6 个情报服务（VirusTotal/AbuseIPDB 等）产出分级复合评分
- 7 类 IOC 分类索引与 180 天滚动数据过期机制
- 基于 MISP 生成与分析师确认的反馈驱动的模型增量重训

## 适用场景

- SOC 团队在大规模消费情报前过滤投毒 IOC
- 自动化聚合多源 feed、富化并推送 MISP 平台
- 通过 Kibana 面板查看 feed 覆盖与 IOC 评分分布

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L19: ThreatRadar is an open-source Threat Intelligence pipeline designed for Security Operations Centers and threat inte
> L29: - Flags statistically anomalous IOCs using a trained IsolationForest model and an LLM that semantically validates I
> L50:  Flagged IOCs then undergo LLM semantic analysis (OpenAI GPT-4o via OpenRouter) that validates intelligence against

## 星数曲线

```mermaid
xychart-beta
    title "THREATRADAR-Pipeline/ThreatRadar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `790df896c32a` · [字段定义](../../DATASET.md)*
