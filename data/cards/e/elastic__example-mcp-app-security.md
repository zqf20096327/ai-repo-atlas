# elastic/example-mcp-app-security

⭐ 25 · TypeScript · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/elastic/example-mcp-app-security) · [官网](https://modelcontextprotocol.io/extensions/apps/overview) · 组织维护

**为 SOC 分析师在 Claude/Cursor 内提供交互式安全运营面板的 MCP 应用**

基于 Model Context Protocol 的 Elastic Security 参考应用：提供告警分诊、攻击链分析、案件管理、检测规则管理、威胁狩猎工作台和样本数据生成六个工具，每个工具在 MCP 宿主（Claude Desktop、Cursor、VS Code、Claude Code）调用时返回内联渲染的 React 交互界面；界面直接调用服务端数据与操作工具，保持 LLM 上下文精简。需要连接用户的 Elasticsearch/Kibana 与 API key，附 Claude Skills 目录与匿名遥测（跟随 Kibana opt-in）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个安全运营工具，每个附带内联渲染的 React 交互 UI
- UI 直接调用服务端数据/操作工具，保持 LLM 上下文精简
- 支持一键 .mcpb 安装到 Claude Desktop，也支持 Cursor/VS Code/Claude Code/Claude.ai
- 附 SKILL.md 形式的 Claude Skills 指导工具使用时机

## 适用场景

- 在 Claude 对话中直接分诊和调查 Elastic Security 告警
- SOC 团队在 AI 宿主内管理案件与检测规则
- 通过 ESQL 工作台和调查图开展威胁狩猎
- 生成 4 种攻击链场景的 ECS 样本数据做演示

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: An MCP App that brings interactive blue-team security operations directly into Claude, VS Code, and other MCP-compat
> L17: This project provides six interactive security operations tools, each with a rich React-based UI that renders inlin

## 星数曲线

```mermaid
xychart-beta
    title "elastic/example-mcp-app-security 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1171886643e4` · [字段定义](../../DATASET.md)*
