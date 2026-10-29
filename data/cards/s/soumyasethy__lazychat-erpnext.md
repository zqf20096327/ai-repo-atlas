# soumyasethy/lazychat-erpnext

⭐ 21 · JavaScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/soumyasethy/lazychat-erpnext) · 个人维护

**嵌入 ERPNext 工作台的 AI 助手：对话查数据、起草报表、确认后落库**

以 Frappe/ERPNext 应用形式安装的聊天面板，面向 ERPNext 顾问与业务用户：用自然语言发起请求，助手通过 95 个权限作用域工具（describe_doctype、run_sql_select、make_chart 等）调度数据，返回内联表格、Vega 图表与 KPI 卡片。写操作采用两阶段机制——变更先暂存于 Redis token，用户点击 Apply 才提交（低风险操作有 3 秒自动确认），并有 30 秒 composer-critic 二次意见。模型由用户自带：粘贴任意 OpenAI 兼容或 Anthropic 提供商的 curl 片段即自动解析端点与鉴权，API key 仅存浏览器。另随附 MCP 服务器。安装途径为 Frappe Cloud 市场一键安装或自托管 bench。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 95 个权限作用域工具，全部以 frappe.session.user 运行，继承 Frappe 权限与审计
- 两阶段变更：写操作暂存后需点击 Apply 提交，附 composer-critic 二次意见
- BYO LLM：粘贴 curl 片段自动解析端点/鉴权/流式参数，API key 仅存浏览器
- 工具结果在聊天内渲染为 Vega 图表、KPI 卡片、Markdown 表格与 Mermaid 图

## 适用场景

- 把干系人的口头需求直接转为 Query Report 并分享 URL
- 跨 doctype 对账、差异报告与临时审计的对话式查询
- 在聊天面板内直接生成图表与仪表盘
- 自托管 LM Studio 或自有 API key 的企业内使用

## 场景标签

`AI 助手` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L23: That ask used to mean opening 3 Frappe doctypes, writing a custom Query Report, debugging joins, fixing field names
> L47: Self-hosted LM Studio? Anthropic? NVIDIA NIM? OpenRouter? Together? Groq? You don't fill out a form. You **paste a 
> L188: - **Built for ERPNext, not bolted on.** Every tool runs as `frappe.session.user` — Frappe permissions, role checks

## 星数曲线

```mermaid
xychart-beta
    title "soumyasethy/lazychat-erpnext 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cacc5612504a` · [字段定义](../../DATASET.md)*
