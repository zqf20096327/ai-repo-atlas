# Algoritmica-ai/deeploans

⭐ 17 · Python · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/Algoritmica-ai/deeploans) · [官网](https://algoritmica.ai/) · 组织维护

**结构化金融贷款级数据的处理与建模开源框架**

Apache 2.0 许可的信贷数据工具集合，覆盖贷款级数据的摄取、校验、标准化到建模全流程。组件包括：GCP 湖仓 ETL 管道（覆盖车贷、中小企业贷、消费贷、住宅与商业抵押贷款）、信用基础模型训练框架（键-值-时间序列 token 化、预训练、微调、组合评分）、ESMA Annex 2 对齐的荷兰 RMBS 合成数据生成器（默认不调用 LLM）、FastAPI 数据接口、浏览器参考应用与 MCP 服务器。各组件独立文档与依赖，需分别安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 类结构化金融资产的 ETL 标准化管道
- 配置驱动的信用基础模型训练与组合评分框架
- 默认无 LLM 调用的合成荷兰 RMBS 月度面板生成器
- 供 AI 客户端发现数据与采样 API 的 MCP 服务器

## 适用场景

- 把碎片化贷款级数据整理为可分析的标准数据集
- 训练并评估信贷序列模型，对组合进行评分
- 生成对齐监管格式的合成房贷面板用于测试
- 让 AI 客户端通过 MCP 接入信贷数据 API

## 场景标签

`金融量化` `微调` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L24: |**Credit Foundation Model**|Config-driven framework for tokenising credit-event sequences, pretraining credit foun
> L28: |**MCP server**|Standalone Model Context Protocol server that lets AI clients discover the platform, inspect schema

## 星数曲线

```mermaid
xychart-beta
    title "Algoritmica-ai/deeploans 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d5508a594380` · [字段定义](../../DATASET.md)*
