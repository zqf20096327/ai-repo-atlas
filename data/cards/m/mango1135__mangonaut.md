# mango1135/mangonaut

⭐ 16 · Kotlin · 推送 2026-05-24 · [GitHub](https://github.com/mango1135/mangonaut) · 个人维护

**监听 Sentry 报错并用 Claude 自动生成修复 PR 的开源服务**

基于 Kotlin + Spring Boot 的服务：接收 Sentry Webhook（HMAC-SHA256 验签），提取错误堆栈与相关源码，交由 Claude 以 agentic 循环方式通过 read_file/list_directory/search_code 工具调用主动探索仓库，随后以片段级查找替换应用修复并在 GitHub 创建修复 PR。内置多层安全防护：阻断幻觉路径、跳过歧义匹配、拒绝无 sha 写入，并按置信度（HIGH/MEDIUM/LOW）过滤自动建 PR。通过 GitHub App 自动映射 Sentry 项目与仓库。运行需 Java 25+、Sentry Internal Integration、GitHub App 与 Anthropic API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude 通过工具调用主动探索仓库定位修复（agentic loop）
- 片段级 find-and-replace 编辑，保留文件其余部分
- 多层安全防护：阻断幻觉路径、跳过歧义匹配、拒绝无 sha 写入、提交时二次校验
- Sentry 项目与 GitHub 仓库经 GitHub App 自动映射，免手动配置

## 适用场景

- 生产环境出错后自动获得带修复代码的 Pull Request
- 团队在 Sentry 告警接入后缩短从报错到修复提案的周期
- 按 LLM 置信度控制是否自动创建 PR

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Mangonaut detects production errors in real-time, automatically analyzes them with AI, and creates fix Pull Requests
> L8: When a Sentry Webhook is received, it extracts the error's stack trace and related source code, sends them to an LLM

## 星数曲线

```mermaid
xychart-beta
    title "mango1135/mangonaut 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4f1aca06bd51` · [字段定义](../../DATASET.md)*
