# trustabl/trustabl-vscode

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/trustabl/trustabl-vscode) · 组织维护

**VS Code/Cursor 扩展：保存时扫描 AI agent 代码的可靠性问题**

面向 VS Code、Cursor、Windsurf、VSCodium 的编辑器扩展，在保存相关文件（Python/TypeScript 源码、.claude/agents/*.md、依赖清单）时调用外部 trustabl CLI 运行 `trustabl scan --format json` 并解析 JSON 报告，以原生诊断、活动栏侧边视图与 webview 详情面板呈现结果。覆盖 Claude SDK、OpenAI SDK、Google ADK、MCP、LangChain、CrewAI、AutoGen 等检测类别，另提供依赖物料清单、基于 OSV 的 CVE 匹配与各面就绪评分。CLI 二进制按设置/PATH/GitHub Releases 顺序解析并校验 sha256。VS Code 可从 Marketplace 安装，其他编辑器需构建 VSIX；需 Node.js 18+ 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 保存/打开工作区时自动运行扫描并渲染为原生诊断与多视图面板
- 支持 9 类检测器（claude_sdk/openai_sdk/google_adk/mcp/langchain/crewai/pydantic_ai/vercel_ai/autogen）
- 依赖物料清单与 OSV CVE 漏洞匹配（可选开启）
- CLI 二进制自动解析或从 GitHub Releases 下载并校验 sha256

## 适用场景

- 在编辑器中实时发现 agent 代码的可靠性问题
- 查看仓库依赖清单与已知 CVE 匹配结果
- 按 severity/file/scope/rule 分组浏览扫描发现

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L3: Runs the Trustabl
> L16: The extension does not bundle a scanner, import SARIF, or run a language
> L94:  (`claude_sdk`, `openai_sdk`, `google_adk`, `mcp`, `langchain`, `crewai`,

## 星数曲线

```mermaid
xychart-beta
    title "trustabl/trustabl-vscode 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-23 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4e77501046fa` · [字段定义](../../DATASET.md)*
