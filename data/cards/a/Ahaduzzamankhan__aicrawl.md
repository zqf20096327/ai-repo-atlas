# Ahaduzzamankhan/aicrawl

⭐ 5 · Rust · MIT · 推送 2026-11-16 · [GitHub](https://github.com/Ahaduzzamankhan/aicrawl) · 个人维护

**面向 AI agent 与脚本的单二进制网页爬取与结构化数据提取引擎**

用 Rust 实现的确定性网页抓取与结构化提取引擎，单个 aicrawl 二进制提供 CLI、REST API、MCP 服务器与内嵌 React 仪表盘四种接口，共享同一套版本化 JSON 请求契约。请求路径中不含模型，不调用 LLM API，通过 CSS/XPath 选择器抽取 JSON-LD、Open Graph、表格等内容并支持 JSON Schema 校验。内置 SQLite 存储、SSRF 防护、robots.txt 默认遵守、限速与 prompt-injection 模式标记。提供 release 二进制安装脚本与源码构建两种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个二进制提供 CLI、REST API、MCP、仪表盘四种接口
- 请求路径无模型：JSON 请求进出，结果确定可复现，无需 API key
- 10 个带严格 JSON schema 的 MCP 工具供 AI agent 调用
- SSRF 防护、robots.txt 默认强制、注入模式仅报告不执行

## 适用场景

- 把网页抓取作为 MCP 工具接入 AI agent 工作流
- 在脚本、cron、CI 中批量提取与导出结构化页面数据
- 通过内嵌仪表盘编写、校验并测试提取请求
- 对页面元数据、JSON-LD、表格做结构化报告与探测

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: no model in the request path, so results are fast, predictable and reproducible —
> L43: |MCP|`aicrawl mcp` (stdio) or `--http`|AI agents with strict tool schemas|
> L172: Ten task-oriented tools, each with a strict JSON schema:

## 星数曲线

```mermaid
xychart-beta
    title "Ahaduzzamankhan/aicrawl 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-22"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-22 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `1dc2e5c4e29d` · [字段定义](../../DATASET.md)*
