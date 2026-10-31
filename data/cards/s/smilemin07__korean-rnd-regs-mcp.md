# smilemin07/korean-rnd-regs-mcp

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/smilemin07/korean-rnd-regs-mcp) · [官网](https://pypi.org/project/korean-rnd-regs-mcp/) · 个人维护

**韩国国家R&D法规审查MCP服务器，向AI提供66部法规检索**

面向研究者、R&D专业机构职员与政府R&D担当公务员的法规审查MCP服务器。通过韩国国家法令信息中心OpenAPI拉取法规原文，按[法律>施行令>施行规则>行政规则]层级对具体案例做多层审查；内置审查用prompt与7个MCP工具（health、法规列表、条款关键词检索等），收录66部法规（创新法系列、各部委R&D法规、核心行政规则）。以远程MCP URL方式接入Claude网页/Claude Code/ChatGPT/Codex，需自备OpenAPI API Key；使用时依赖AI实际调用工具，且支持范围限于66部法规。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖66部韩国国家R&D法规（法律/施行令/施行规则/行政规则）的多层法规审查
- 经国家法令信息中心OpenAPI自动拉取条款原文
- 提供7个MCP工具：状态检查、法规列表、条款·附表关键词检索等
- 支持Claude网页/Claude Code/ChatGPT/Codex的远程MCP接入指南

## 适用场景

- 审查具体R&D案例需要适用哪些法规条款
- 比较相似法规（如部委规定与泛部委标准指南）的差异
- 确认研究费、技术费等行政程序要求

## 场景标签

 · 领域:法律科技/政府R&D合规

## 证据(README 行号)

> L7: 연구행정 규정 검토용 MCP server. AI를 활용하여 아래와 같은 정보를 얻을 수 있습니다.
> L54: ## 연결 방법
> L335: **7개 MCP tool**:

## 星数曲线

```mermaid
xychart-beta
    title "smilemin07/korean-rnd-regs-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-31"]
    y-axis "stars" 10 --> 15
    line [11, 12, 14, 14]
```

2026-10-18 11 → 2026-10-31 14（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c30cf08a2858` · [字段定义](../../DATASET.md)*
