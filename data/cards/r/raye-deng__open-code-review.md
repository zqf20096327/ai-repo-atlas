# raye-deng/open-code-review

⭐ 40 · TypeScript · NOASSERTION · 推送 2026-04-16 · [GitHub](https://github.com/raye-deng/open-code-review) · [官网](https://codes.evallab.ai) · 个人维护

**面向 AI 生成代码的开源 CI/CD 质量门禁与代码审查工具**

面向使用 AI 编程助手的团队、开源维护者与 DevOps 工程师的代码质量检查工具：检测幻觉导入（npm/PyPI/Maven/Go modules）、过时 API、过度工程与安全反模式，覆盖 TypeScript/JavaScript、Python、Java、Go、Kotlin 等语言。三层分析（结构检测、语义分析、LLM 深扫），LLM 层可接本地 Ollama 或任意 OpenAI 兼容端点，支持 ocr heal 自动修复预览。提供 CLI、GitHub Actions、GitLab CI 集成与 MCP Server（接入 Claude Desktop、Cursor 等），输出 terminal/JSON/SARIF/HTML 格式。许可为 BUSL-1.1，个人与非商业使用免费，2030 年转为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 幻觉导入检测，覆盖 npm/PyPI/Maven/Go modules 包数据库
- 三层分析：结构检测 + 语义分析 + LLM 深扫（A+ 到 F 评分）
- ocr heal AI 自动修复，支持 dry-run 预览
- CLI + GitHub Actions + GitLab CI + MCP Server 多形态交付，SARIF/JSON/HTML 输出

## 适用场景

- 合并前审查 AI 助手生成的 PR，拦截幻觉依赖与过时 API
- 在 CI/CD 流水线加代码质量门禁且不把代码送到云端
- 在 Claude Desktop/Cursor/Windsurf 中通过 MCP 直接调用扫描与修复

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: > **The first open-source CI/CD quality gate built specifically for AI-generated code.**
> L72: **Powered by local LLMs or any OpenAI-compatible API.** Run Ollama for 100% local analysis, or connect to any remot
> L173: ## MCP Server — Use in Claude Desktop, Cursor, Windsurf

## 星数曲线

```mermaid
xychart-beta
    title "raye-deng/open-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f13087654841` · [字段定义](../../DATASET.md)*
