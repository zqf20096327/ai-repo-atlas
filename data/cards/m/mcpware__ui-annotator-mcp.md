# mcpware/ui-annotator-mcp

⭐ 21 · JavaScript · MIT · 推送 2026-03-24 · [GitHub](https://github.com/mcpware/ui-annotator-mcp) · 组织维护 · 中文 README

**给网页元素加悬浮标签的 MCP server，让人与 AI 共用元素名**

通过反向代理运行：代理抓取本地页面，注入注释脚本，扫描 DOM 中的命名元素，用户在任意浏览器中悬停即可看到元素名称、CSS 选择器、内容预览与尺寸；提供 annotate、get_elements、highlight_element、inspect_mode 等 MCP 工具，供 Claude 等 AI 助手查询与确认页面元素。面向需要与 AI 编码助手协作修改 UI 的开发者、QA、设计师等角色。零浏览器扩展、零代码改动、零外部依赖（Node.js 内置 http + MCP SDK stdio），通过 npx 启动，代理默认端口 7077 可用环境变量修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向代理注入注释脚本，任意浏览器可用、零扩展零代码改动
- 悬停显示元素名/CSS 选择器/内容预览/尺寸
- 提供 annotate、get_elements、highlight_element、rescan_elements、inspect_mode 五个 MCP 工具
- 零外部依赖：Node.js 内置 http + MCP SDK stdio，无 WebSocket/Express

## 适用场景

- 与 Claude 等 AI 助手协作修改前端时，用真实元素名指代要改的组件
- QA、PM、设计师无需 DevTools 知识即可查看并复述元素名称
- 让 AI 读取页面元素清单并高亮确认目标元素

## 场景标签

 · 领域:开发工具/MCP

## 证据(README 行号)

> L76: ### MCP Tools for AI
> L130: - **MCP server**: `@modelcontextprotocol/sdk` (stdio transport)

## 星数曲线

```mermaid
xychart-beta
    title "mcpware/ui-annotator-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a474a04ba2bc` · [字段定义](../../DATASET.md)*
