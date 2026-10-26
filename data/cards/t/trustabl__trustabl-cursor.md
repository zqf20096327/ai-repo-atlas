# trustabl/trustabl-cursor

⭐ 25 · JavaScript · NOASSERTION · 推送 2026-09-10 · [GitHub](https://github.com/trustabl/trustabl-cursor) · [官网](https://trustabl.ai) · 组织维护

**面向 Cursor 的 MCP server 插件：静态扫描 AI-agent 代码库的可靠性与安全问题**

Trustabl for Cursor 是一个 Cursor 插件，向 Cursor agent 提供 MCP server 与两个工具（trustabl_scan / trustabl_last_findings）。扫描时对代码库进行清点，识别 Claude Agent SDK、OpenAI Agents SDK、Google ADK、LangChain、CrewAI、Pydantic AI、AutoGen、MCP server 等代理框架，输出按严重度分级的问题、生产就绪评分，并在被扫描目录写入 SARIF 2.1.0 / JSON / 文本三种报告文件。扫描器二进制首次运行时下载（约 14 MB）并做 sha256 校验，校验失败即中止；Windows（amd64）、macOS、Linux 均支持。同一 server 也可在 Claude Code、Windsurf、VS Code 等任意 MCP client 中使用。

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

- 识别 9 类以上 agent 框架与 MCP server 的风险模式，按严重度分级
- 输出生产就绪评分与 SARIF 2.1.0 / JSON / 文本三份报告文件
- 扫描器二进制下载后经 sha256 校验，未验证通过不执行
- server 预打包无运行时依赖，可在任意 stdio MCP client 中注册

## 适用场景

- 在 Cursor 中用自然语言触发代码库的 agent 可靠性扫描
- CI 前检查 AI-agent 代码的高严重度风险并获取可跳转代码位置的问题清单
- 把扫描结果以 SARIF 形式在编辑器内查看

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6: The plugin adds an **MCP server** whose tools the Cursor agent can call. Ask it to
> L12: Detects Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangChain, CrewAI,
> L132: |`trustabl_scan`|Scan a directory. Returns a severity table, the readiness score, the scan report, and findings (w

## 星数曲线

```mermaid
xychart-beta
    title "trustabl/trustabl-cursor 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-26"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-23 24 → 2026-10-26 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c952e05a8853` · [字段定义](../../DATASET.md)*
