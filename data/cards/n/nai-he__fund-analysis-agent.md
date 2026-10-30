# nai-he/fund-analysis-agent

⭐ 35 · Python · MIT · 推送 2026-06-18 · [GitHub](https://github.com/nai-he/fund-analysis-agent) · 个人维护 · 中文 README

**国内公募基金数据采集与 AI 辅助分析工具（FastAPI+React）**

输入基金代码后自动采集数据（AKShare→efinance→Tencent 优先级 fallback），生成基金画像、多维技术指标、0-100 结构化风险评分、历史回测验证（方向准确率、Brier 分数、概率校准）与概率化走势情景，并通过 OpenAI 兼容 API 输出中文 LLM 分析总结；LLM 为可选模块，不可用时回退规则化文本。含个人持仓管理与宏观仪表盘。后端 Python/FastAPI，前端 React 18 + Vite，无 Docker，需分别启动前后端服务。声明仅用于个人学习研究，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AKShare → efinance → Tencent 三级数据源 fallback
- 结构化风险评分（0-100 分，多维度加权分解）
- 回测验证：方向准确率、Brier 分数、概率校准与基线对比
- LLM 可选，无 API Key 时自动回退规则化分析

## 适用场景

- 输入基金代码获取技术指标、风险评分与走势情景分析
- 管理个人持仓并做个性化分析
- 在无网络/无 LLM 环境下用 mock 数据运行测试

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 国内公募基金数据采集与 AI 辅助分析工具。输入基金代码，自动获取基金信息、技术指标、风险评分、回测验证和走势情景分析，并通过 LLM 输出中文辅助判断。
> L32: - LLM 中文分析总结（偏积极 / 中性 / 偏谨慎 / 风险较高）
> L129: ### 不配置 LLM API Key

## 星数曲线

```mermaid
xychart-beta
    title "nai-he/fund-analysis-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b44bfaf0c869` · [字段定义](../../DATASET.md)*
