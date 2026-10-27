# stefanoamorelli/sec-edgar-mcp

⭐ 378 · Python · AGPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/stefanoamorelli/sec-edgar-mcp) · [官网](https://sec-edgar-mcp.amorelli.tech/) · 个人维护

**供 AI 助手访问 SEC EDGAR 财务数据的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 AI 助手接入 SEC EDGAR：提供 CIK 查询、公司信息、10-K/10-Q/8-K 文件检索与章节提取、XBRL 解析的资产负债表/利润表/现金流量表，以及 Form 3/4/5 内部人交易数据，所有响应附 SEC 文件 URL 供核验。构建于 sec-edgar-toolkit 之上，需 Python 3.11+，支持 stdio 与 streamable HTTP 两种传输（后者面向 Dify 等平台），HTTP 模式无鉴权、限私网使用。含 Promptfoo 评测套件。AGPL-3.0 许可并另提供商业授权联系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XBRL 解析的三大财务报表与 Form 3/4/5 内部人交易查询
- 10-K/10-Q/8-K 检索与章节提取，响应附 SEC 文件 URL
- 支持 stdio 与 streamable HTTP（面向 Dify 等平台）两种传输
- Promptfoo 评测套件与 DOI 学术引用格式

## 适用场景

- 让 AI 助手查询上市公司的财报与申报文件
- 金融分析场景中核验带来源的精确财务数据
- 在 Dify 等平台上通过 HTTP 接入 SEC 数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L9: MCP server for accessing SEC EDGAR filings. Connects AI assistants to company filings, financial statements, and ins
> L50: For platforms like Dify, use streamable HTTP instead of stdio:

## 星数曲线

```mermaid
xychart-beta
    title "stefanoamorelli/sec-edgar-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26", "2026-10-27"]
    y-axis "stars" 372 --> 379
    line [373, 374, 377, 378]
```

2026-10-18 373 → 2026-10-27 378（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6c612a43f8ea` · [字段定义](../../DATASET.md)*
