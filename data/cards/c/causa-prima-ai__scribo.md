# causa-prima-ai/scribo

⭐ 18 · NOASSERTION · 推送 2026-06-03 · [GitHub](https://github.com/causa-prima-ai/scribo) · [官网](https://scribo.causaprima.ai) · 组织维护

**对话式生成 EN 16931 合规电子发票的免费工具**

由 Causa Prima（慕尼黑公司，面向 CFO 办公室的 agentic AI）提供的免费电子开票工具：用自然语言描述发票内容，即生成结构化、经过 EN 16931 规则集校验的合规发票（PDF+内嵌 XML）。以五种形态交付：Claude/Codex skill、托管 MCP server、npm CLI、公开 HTTP API 与 Web 应用，均对接同一后端。已上线德国 ZUGFeRD/XRechnung 与美国纯 PDF；Factur-X、Facturae、Peppol BIS 3.0 标注即将推出。首次开票需邮箱验证码验证。许可证为专有（UNLICENSED），非开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言描述即生成合规发票草稿
- EN 16931 输出在生成时经 Invopop 托管校验器验证，不通过不出交付
- 五种交付形态：skill / MCP server / npm CLI / HTTP API / Web 应用，同一后端
- 匿名 HTTP API（限流、OpenAPI 3.1），CLI 带 sysexits 风格退出码可入 CI

## 适用场景

- 让 Claude/ChatGPT 等 agent 在对话中直接替我开发票
- 在脚本或 CI 中用 CLI 批量生成德国合规电子发票
- 不动手填表，在浏览器里描述一句话就下载发票 PDF

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: Scribo is a free, conversational e-invoicing tool. Describe an invoice in plain language — "bill Acme GmbH €2,400 f
> L84: Scribo is built to be operated by an agent. It ships as an **MCP server**, a **CLI**, and a **Claude/Codex skill**,

## 星数曲线

```mermaid
xychart-beta
    title "causa-prima-ai/scribo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `16af545d66b3` · [字段定义](../../DATASET.md)*
