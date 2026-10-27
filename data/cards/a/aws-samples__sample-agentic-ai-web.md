# aws-samples/sample-agentic-ai-web

⭐ 53 · Python · MIT-0 · 推送 2026-02-21 · [GitHub](https://github.com/aws-samples/sample-agentic-ai-web) · 组织维护

**AWS Bedrock 渐进式示例集：构建带视觉的网页自动化助手**

aws-samples 出品的渐进式教学项目：通过 11 个步骤演示如何用 Amazon Bedrock 调用 Anthropic Claude 与 Amazon Nova 模型构建网页自动化助手，能力逐步叠加——从无工具 API 调用到 Playwright 无头浏览器导航、截图视觉分析、点击/输入/滚动、文件写入，再到 Step 10 用 MCP（FastMCP、stdio 传输）重构为客户端-服务器架构，Step 11 增加对话历史管理（用 Nova Micro 做摘要以降低 token 用量）。前提是用户已配置 AWS CLI 凭证并拥有 Bedrock API 权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个渐进式步骤从基础 API 调用到完整网页自动化助手
- Playwright 无头浏览器导航、截图与视觉点击
- MCP 客户端-服务器重构（FastMCP、stdio 传输）
- 对话历史管理：媒体内容移除 + 小模型摘要以降低 token 用量

## 适用场景

- 学习如何用 Bedrock 模型构建带工具调用的 agent
- 参考 MCP 客户端-服务器架构的落地实现
- 实现视觉驱动的网页自动化（点击、输入、滚动、表单提交）

## 场景标签

`浏览器自动化` `教程课程` · 领域:效率与自动化

## 证据(README 行号)

> L3: This project demonstrates how to use Amazon Bedrock with Anthropic Claude and Amazon Nova models to create a web aut
> L52: `10-mcp-client` - Refactors the application to use the Model Context Protocol:

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-agentic-ai-web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-27 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8f02bf7433ce` · [字段定义](../../DATASET.md)*
