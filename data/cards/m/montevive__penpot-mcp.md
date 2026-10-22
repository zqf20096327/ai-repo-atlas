# montevive/penpot-mcp

⭐ 241 · Python · 推送 2025-11-01 · [GitHub](https://github.com/montevive/penpot-mcp) · 个人维护

**连接 Claude/Cursor 等 LLM 与 Penpot 设计文件的 MCP 服务器**

基于 Model Context Protocol 的服务器，通过 Penpot API 让 Claude Desktop、Cursor IDE 等 MCP 兼容 AI 助手读取与操作 Penpot 设计文件。提供 list_projects、get_file、export_object、search_object 等 6 个工具和服务器状态、API schema、渲染组件图等 5 类资源；另附 Python SDK、CLI 工具（penpot-tree/penpot-validate）与 REST API。需 Python 3.12+ 与 Penpot 账号凭据；README 提示 penpot.app 云端有 CloudFlare 防护可能拦截 API 请求，需浏览器完成人机验证。以 PyPI 包、uvx 或源码方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 MCP 工具：列项目、取文件、导出对象为图片、按名搜索对象等
- 提供 Claude Desktop 与 Cursor IDE 的配置接入说明
- 附 Python SDK、CLI 工具与 REST API 供自定义集成
- penpot-tree / penpot-validate 命令行工具做文件可视化与 schema 校验

## 适用场景

- 在 Cursor 或 Claude Desktop 里用自然语言查询我的 Penpot 项目与组件
- 让 AI 分析设计组件并导出设计资产为图片
- 为设计系统生成文档并做一致性检查

## 场景标签

 · 领域:设计工具/AI 集成

## 证据(README 行号)

> L23: **Penpot MCP** is a revolutionary Model Context Protocol (MCP) server that bridges the gap between AI language mode
> L42: - **MCP Protocol Implementation**: Full compliance with Model Context Protocol standards

## 星数曲线

```mermaid
xychart-beta
    title "montevive/penpot-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 240 --> 242
    line [241, 241]
```

2026-10-18 241 → 2026-10-22 241（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `971cbfe470bc` · [字段定义](../../DATASET.md)*
