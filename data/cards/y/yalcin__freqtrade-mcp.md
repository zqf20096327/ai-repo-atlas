# yalcin/freqtrade-mcp

⭐ 18 · Python · GPL-3.0 · 推送 2026-08-08 · [GitHub](https://github.com/yalcin/freqtrade-mcp) · [官网](https://github.com/yalcin/freqtrade-mcp) · 个人维护

**Freqtrade 代码库内省的只读 MCP 服务器，辅助 LLM 写策略代码**

面向 LLM agent 的只读 MCP 服务器，提供 Freqtrade 代码库内省数据：可列出与检查 IStrategy 可覆写方法的签名/类型提示/docstring、类与枚举、配置 schema、DataFrame 列及 markdown 文档检索，共 13 个工具。安全模型限定只读、stdio 本地传输、输入白名单校验、搜索用 ast 静态解析不触发导入。要求 Python>=3.13、freqtrade>=2026.2，需装在与 freqtrade 相同的环境。作者声明为研究/个人用途项目，不执行交易。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 13 个内省工具：策略方法签名、类、枚举、配置 schema、文档检索
- 只读安全模型：白名单输入校验、ast 静态搜索、stdio 本地传输、仅限 freqtrade.* 命名空间
- 兼容 Claude Code、OpenAI Codex CLI 及通用 stdio 接入
- 文档工具需设置 FREQTRADE_DOCS_PATH，缓存 1 小时 TTL

## 适用场景

- 让 Claude/Codex 等 agent 在写策略前查询真实的 Freqtrade API 签名与文档
- 检查策略回调方法的参数与类型提示
- 检索 Freqtrade 配置键与枚举取值

## 场景标签

`编码 Agent` `金融量化` · 领域:编码与开发

## 证据(README 行号)

> L5: A **read-only MCP (Model Context Protocol) server** that provides LLM tools with introspection data about the Freqtr
> L17: It is a read-only reference layer for LLM agents. The goal is to help agents check the actual docs, public strategy

## 星数曲线

```mermaid
xychart-beta
    title "yalcin/freqtrade-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f8feb40f5739` · [字段定义](../../DATASET.md)*
