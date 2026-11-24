# ark-forge/mcp-eu-ai-act

⭐ 12 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/ark-forge/mcp-eu-ai-act) · [官网](https://arkforge.fr/mcp-eu-ai-act.html) · 组织维护

**扫描代码库中 AI 框架使用并检测 EU AI Act/GDPR 合规的 CLI 与 MCP 服务器**

以静态分析方式扫描项目源码与配置文件，检测 16 种 AI 框架的使用，将每项发现映射到 EU AI Act 具体条款并输出 pass/fail 与修复说明；提供风险分类建议、合规文档模板、Annex IV 打包、GDPR 扫描及双合规热点识别共 10 个工具。可通过 CLI、MCP 服务器（Claude Desktop/Code、Cursor）与 REST API 运行，支持 CI/CD 集成。限制：仅静态分析不覆盖运行时行为，扫描上限 5,000 个文件、单文件 1 MB；Pro/Certified 功能需订阅，免费层每天 5 次扫描。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 检测 16 种 AI 框架并映射到具体 EU AI Act 条款
- 10 个 MCP 工具：扫描、合规打分、路线图、Annex IV 打包、GDPR 扫描等
- 支持 Claude Desktop/Code、Cursor 与 REST API 三种接入方式
- Trust Layer 认证生成防篡改合规证明

## 适用场景

- 在 2026 年执法期限前扫描项目识别 EU AI Act 合规缺口
- 为审计准备 Annex IV 技术文档打包
- CI/CD 中对代码库做定期合规检查
- 评估 AI 系统所属的风险类别

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L1: # EU AI Act Compliance Scanner — CLI + MCP Server
> L17: Detects 16 AI frameworks in your codebase, maps each to binding legal articles, returns pass/fail with fix instruct
> L146: Detects AI framework usage in source code and config/manifest files. Supports 16 frameworks across Python, JS, TS,

## 星数曲线

```mermaid
xychart-beta
    title "ark-forge/mcp-eu-ai-act 星数(近 3 点)"
    x-axis ["2026-10-21", "2026-11-08", "2026-11-24"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-21 11 → 2026-11-24 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `aaf4759d97bd` · [字段定义](../../DATASET.md)*
