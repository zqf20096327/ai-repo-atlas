# Synta-ai/n8n-mcp-workflows

⭐ 27 · 推送 2026-04-14 · [GitHub](https://github.com/Synta-ai/n8n-mcp-workflows) · [官网](https://synta.io) · 组织维护

**面向 n8n 的生产级工作流示例集，按 7 类用例组织**

由 Synta 维护的 n8n 工作流示例仓库：从 synta mcp 使用数据中导出并匿名化的真实生产工作流，按内容社交、线索获取、客服、招聘、财务、文档处理、研究情报 7 类组织为 JSON 文件。工作流内部调用 Claude、Gemini、GPT-4、Perplexity Sonar 等模型及 WhatsApp、Slack、Airtable 等服务。使用方式为复制 JSON 内容，在 n8n 中通过 Workflows → Import from JSON 导入，再重接凭据。所有凭据与 API key 已脱敏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 大类生产级 n8n 工作流 JSON 示例
- 导出自真实用户部署并匿名化处理
- 导入说明：n8n 内 Import from JSON 粘贴即可

## 适用场景

- 查找与我业务场景相近的 n8n 工作流模板直接导入
- 学习线索评分、客服分流、文献综述等 AI 工作流的搭建方式

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Real n8n workflows from production, exported and anonymised from synta mcp usage data. Each one is deployed by real 
> L50: 1. Copy the contents of any `.json` file
> L51: 2. In n8n, go to **Workflows → Import from JSON**

## 星数曲线

```mermaid
xychart-beta
    title "Synta-ai/n8n-mcp-workflows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `019782741c37` · [字段定义](../../DATASET.md)*
