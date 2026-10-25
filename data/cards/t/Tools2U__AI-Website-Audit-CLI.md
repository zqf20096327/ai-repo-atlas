# Tools2U/AI-Website-Audit-CLI

⭐ 63 · Python · MIT · 推送 2026-06-07 · [GitHub](https://github.com/Tools2U/AI-Website-Audit-CLI) · 个人维护

**网站审计 CLI：确定性规则检查加 OpenAI 生成改进报告**

Python 命令行工具，将公开网站 URL 转为结构化审计包：抓取页面提取事实数据，运行规则化的确定性检查与打分（SEO、UX、可访问性、信任、性能、内容），再用 OpenAI Responses API 基于已保存证据生成 Markdown/HTML 报告，支持英德双语与配置推理开销。无 API key 时可仅运行本地确定性审计。面向开发者、自由职业者、代理商与小企业，MIT 许可，可本地或 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性规则审计输出 SEO/UX/可访问性/信任/性能等分数与分级发现
- OpenAI Responses API 基于提取证据生成报告（默认 gpt-5.5，可选小模型）
- inspect 模式无需 API key 即可本地审计
- 输出 Markdown/HTML 报告及提取 JSON、审计 JSON、响应元数据 JSON

## 适用场景

- 从终端对公开网站跑一次快速审计并拿到改进清单
- 交付给客户或团队的可分享 HTML 审计报告
- 核对发送给 AI 层的原始证据以保证透明

## 场景标签

 · 领域:Web 开发/网站质量审计

## 证据(README 行号)

> L16: `ai-website-audit-cli` turns a public website URL into a structured audit package:
> L34: - **AI last:** use OpenAI to write a deeper report grounded in the saved evidence.

## 星数曲线

```mermaid
xychart-beta
    title "Tools2U/AI-Website-Audit-CLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-25 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `36d96ad1cbec` · [字段定义](../../DATASET.md)*
