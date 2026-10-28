# momenbasel/vulnhawk

⭐ 90 · Python · NOASSERTION · 推送 2026-06-10 · [GitHub](https://github.com/momenbasel/vulnhawk) · [官网](https://github.com/marketplace/actions/vulnhawk-security-scan) · 组织维护

**面向开发者的 AI 代码安全扫描器，检测规则工具遗漏的逻辑漏洞**

通过 pip 安装的 CLI 工具，用 LLM 分析代码库检测缺失授权、IDOR、业务逻辑缺陷等问题。核心机制是 enrichment 步骤：为每个代码块附加同目录相关代码与全库认证中间件模式作为上下文，让模型对比相似组件发现不一致。支持 Claude Code CLI、Codex CLI（订阅免费）、Claude API、OpenAI API 与 Ollama（本地、8GB+ VRAM）后端；提供 GitHub Action、SARIF 输入/输出链式协作。限制：代码块会发送给 LLM 服务商（Ollama 可离线）；源码可得许可（source-available）而非标准开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨文件上下文 enrichment：附加同目录代码与全库认证模式供 AI 对比
- 5 种扫描模式（auth/injection/secrets/config/crypto）与 JSON/SARIF/Markdown 输出
- 可接收 Semgrep/CodeQL 的 SARIF 结果做验证、扩展与攻击链构建
- GitHub Action 支持基线扫描与 PR 增量扫描，结果上传 Code Scanning

## 适用场景

- 在 CI/CD 中补充 Semgrep/CodeQL 检测业务逻辑与授权缺陷
- PR 合并前发现规则引擎无法表达的漏洞
- 用 Ollama 后端做完全本地的私有代码安全扫描

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3:  AI-powered code security scanner that finds vulnerabilities Semgrep and CodeQL miss.
> L24: VulnHawk analyzes code with AI, and for every piece of code it examines, it includes **related code from elsewhere 

## 星数曲线

```mermaid
xychart-beta
    title "momenbasel/vulnhawk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 88 --> 91
    line [89, 90, 90]
```

2026-10-18 89 → 2026-10-28 90（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b92eb38c8679` · [字段定义](../../DATASET.md)*
