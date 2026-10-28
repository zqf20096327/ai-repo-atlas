# gergchen/astock-market-engine

⭐ 22 · Python · MIT · 推送 2026-05-31 · [GitHub](https://github.com/gergchen/astock-market-engine) · [官网](https://github.com/gergchen/astock-market-engine) · 个人维护 · 中文 README

**面向个人用户的 A 股市场分析 AI 助手（非自动交易）**

自托管的 A 股市场分析系统：FastAPI 后端 + Next.js 14 前端，通过 akshare 等多源数据获取行情，规则引擎计算主力行为阶段、情绪周期、龙头识别、板块轮动等结构化评分，可接入 Claude / OpenAI 兼容（DeepSeek）API 生成自然语言分析，结果存入 Qdrant 供 RAG 复盘检索。三层降级管线：不配置 API Key 时纯本地规则引擎运行，数据源全不可用时降级到 Mock 模板。含策略回测、WebSocket 实时工作台与飞书通知，Docker Compose 一键部署。仅供学习研究，不构成投资建议。

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

- 主力行为阶段识别（吸筹/洗盘/主升/出货）与情绪周期判断
- 无需 API Key 的本地规则引擎，断网可用
- RAG 增强的每日 AI 复盘（Qdrant 检索相似历史交易日）
- 内置 MA 交叉/放量突破/龙头跟随策略回测与 Docker 一键部署

## 适用场景

- 输入股票代码获取主力行为、技术面、资金面的综合分析
- 每日查看市场情绪复盘与相似历史交易日对比
- 跟踪板块轮动、龙头识别与涨停跌停归因
- 对内置策略做历史回测与绩效评估

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L16: |**AI 个股分析**|输入股票代码，输出大白话综合分析（主力行为 + 技术面 + 资金面）|
> L28: |**本地规则引擎**|**无需 API Key**，纯规则驱动的分析能力，即使断网也能用|
> L124: ① 真实数据 + LLM   →  完整 AI 综合分析  (需配置 API Key)

## 星数曲线

```mermaid
xychart-beta
    title "gergchen/astock-market-engine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ddd2729edfc9` · [字段定义](../../DATASET.md)*
