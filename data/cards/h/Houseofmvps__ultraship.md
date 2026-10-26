# Houseofmvps/ultraship

⭐ 123 · JavaScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/Houseofmvps/ultraship) · [官网](https://www.npmjs.com/package/ultraship) · 个人维护

**Claude Code 插件：43 技能+40 工具+13 Agent 覆盖开发到上线全流程**

面向 Claude Code 用户的插件，以斜杠命令触发 43 个 markdown 技能、40 个独立 Node.js 脚本工具（JSON 输出、无构建步骤）与 13 个并行调度的 Agent。能力覆盖开发流程（TDD、代码审查、调试）、上线前审计（SEO/GEO/AEO 扫描 63 规则、WCAG 2.2 无障碍、密钥泄露、渗透测试、bundle 体积）与运维（金丝雀监控、事件响应、成本追踪），ship-gate 可阻塞部署。Currency Guard 与 Context7 MCP 使 Claude 参考实时文档而非过期训练数据。0 依赖、274 个测试，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 个独立 Node.js 工具：JSON 输出、无构建步骤
- ship-gate 阻塞式上线门禁，密钥泄露/严重发现即退出码 1
- seo-scanner 含 39 SEO + 20 GEO（AI 爬虫访问/llms.txt）+ 4 AEO 规则
- eval-scanner 定位 8 类 LLM 调用点（含 Anthropic/OpenAI/Ollama 等）并检查 eval 覆盖

## 适用场景

- 发布前用 /ship 一键跑 6 项审计并输出评分卡
- 配置 CI 阻塞门禁拦截密钥泄露与无障碍问题
- 让 Claude Code 按斜杠命令执行渗透测试、事件响应等专项流程

## 场景标签

`代码审查` `编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L1: Ultraship — Claude Code Plugin
> L175: Skills are markdown instruction files that shape Claude's behavior during your session. They activate based on con
> L37:     U["You type a<br/>slash command"] --> S["Skill<br/>(markdown instructions)"]

## 星数曲线

```mermaid
xychart-beta
    title "Houseofmvps/ultraship 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-26 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `92bba291f1cd` · [字段定义](../../DATASET.md)*
