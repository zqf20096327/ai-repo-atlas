# nitsan-technologies/ns_t3af

⭐ 25 · PHP · GPL-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/nitsan-technologies/ns_t3af) · [官网](https://t3planet.de/ai-foundation-fur-typo3) · 组织维护

**TYPO3 的 AI 基础扩展：内置 MCP 服务器与多 LLM 管理**

面向 TYPO3 CMS 的 PHP 扩展（GPL-2.0-or-later，Packagist/TER 分发）。提供内置 MCP 服务器使 TYPO3 成为原生 MCP 端点，Claude Desktop、Cursor、n8n 等可直接读写内容；支持 7 种传输方式、OAuth 2.1 与网关代理模式。后端模块集中管理多 LLM 供应商（OpenAI/Anthropic/Gemini/Ollama 及兼容接口）及优先级、预算、权限、用量日志，并提供 MCP 工具目录、AI 上下文配置、批量操作与 63 个可编辑提示模板。需 TYPO3 12.4+ 与 PHP 8.2+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TYPO3 原生 MCP 服务器（7 种传输、OAuth 2.1、网关/代理模式）
- 多 LLM 管理与按扩展的月度预算上限、故障转移排序
- 请求级用量日志（模型/token/费用/时长）与 CSV 导出
- 63 个可编辑提示模板、批量 AI 操作与 Symfony Console/Scheduler 自动化

## 适用场景

- 让 Claude、Cursor、n8n 等 agent 直接读写我的 TYPO3 站点内容
- 在 TYPO3 后台统一管理 AI 供应商、预算与权限
- 批量生成元标签、翻译、alt 文本等内容操作

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: AI Foundation gives TYPO3 CMS a built-in MCP server, AI tools and multi-LLM management to connect Claude, Cursor, n
> L37: * **MCP Server:** TYPO3 becomes a native MCP endpoint. Claude Desktop, Cursor, n8n, Windsurf and VS Code Copilot ca
> L41: * **Multi-LLM Management:** Configure OpenAI, Anthropic, Gemini, Ollama and any OpenAI-compatible provider. Set pri

## 星数曲线

```mermaid
xychart-beta
    title "nitsan-technologies/ns_t3af 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cfc5f9ff86c6` · [字段定义](../../DATASET.md)*
