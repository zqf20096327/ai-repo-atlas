# itsmesherry/claude-audit

⭐ 15 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/itsmesherry/claude-audit) · [官网](https://www.npmjs.com/package/claude-audit) · 个人维护

**命令行代码审计工具：静态检查为主，可选 Claude 深度审计**

Node.js 命令行工具，对项目按类别打分并列出带文件、行号与修复建议的问题项，报告输出为终端、Markdown、HTML 或 JSON。无 API key 时仅运行基于正则的静态检查，数据不出本机；配置 ANTHROPIC_API_KEY 后可运行 Agentic 模式（Claude 通过一组只读工具自主检查代码）或 One-shot 模式（单次 API 调用消化项目摘要）。静态规则覆盖安全（硬编码密钥、SQL 拼接等）、依赖（内置少量已知漏洞包）、质量/测试/文档；性能与架构仅在 AI 审计时评分。可作 GitHub Action 使用，报告中的密钥一律脱敏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 静态检查离线毫秒级运行，无需 API key
- Agentic 模式下 Claude 使用 7 个只读工具（限路径、限轮次、限预算、全程 trace 记录）
- 三种模式：Static / Agentic / One-shot（--fast）
- 提供 GitHub Action 集成，输出 score/grade/critical-count 等

## 适用场景

- 在 CI 中对项目做安全与质量检查并按严重度决定是否失败
- 本地快速扫描硬编码密钥等常见问题
- 让 Claude 对代码库做深度审计并引用代码位置

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L19: # Static checks only. No API key, nothing leaves your machine.
> L96: Your code is sent to the Anthropic API in the two AI modes. It is not sent anywhere in `--static` mode.

## 星数曲线

```mermaid
xychart-beta
    title "itsmesherry/claude-audit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `09e3e0ea2529` · [字段定义](../../DATASET.md)*
