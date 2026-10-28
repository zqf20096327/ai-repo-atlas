# akanthed/SecureAI-Scan

⭐ 24 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/akanthed/SecureAI-Scan) · [官网](https://www.npmjs.com/package/secureai-scan) · 个人维护

**离线扫描 LLM/MCP/RAG 代码安全漏洞的 CLI 工具**

面向开发者的本地静态安全扫描器，扫描与 LLM、MCP 服务器、向量库、Agent Skills 相关的代码与配置：检测提示注入、MCP 命令注入与路径穿越、工具投毒、RAG 数据泄露、恶意技能包等，每条发现附 source→sink 数据流证据与证据分级（proven/likely/heuristic）。支持 TypeScript/JavaScript/Python/MCP 配置/Skill 包，可审计本机已装 MCP 服务器，输出 SARIF/JSON/HTML 报告，并提供 GitHub Action 与 Claude Code 插件。48 条规则映射 OWASP LLM Top 10 等。限制：单一维护者、无 SLA，非通用 SAST。

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

- 48 条规则覆盖提示注入、MCP 工具投毒、RAG 访问控制等，映射 OWASP LLM/ASI/MCP Top 10
- 每条发现带 source→sink 追踪证据与 proven/likely/heuristic 分级
- 可审计本机已安装的 MCP 服务器与 Skills（读取 Claude Code、Cursor、VS Code 等客户端配置）
- 全离线运行，扫描前不执行任何被检目标（npm pack / shallow clone）

## 适用场景

- 提交前检查 Agent/MCP 代码中的提示注入与命令注入漏洞
- 审计本机 AI 客户端已信任的 MCP 服务器与技能是否含恶意或易受攻击版本
- 安装前扫描第三方 MCP 服务器或 Agent Skill 包
- 在 CI 中通过 GitHub Action 持续扫描并输出 SARIF 报告

## 场景标签

`网络安全` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L14: **An offline scanner for the code that talks to LLMs, MCP servers, vector stores, and Agent Skills. It finds prompt
> L16: A default scan reports only what it can prove. No account, no upload, nothing leaves your machine. TypeScript, Java
> L104: **48 rules** mapped to the OWASP Top 10 for LLM Applications (2026), the Agentic (ASI) list, and the OWASP MCP Top

## 星数曲线

```mermaid
xychart-beta
    title "akanthed/SecureAI-Scan 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `86eaaa5ce2dd` · [字段定义](../../DATASET.md)*
