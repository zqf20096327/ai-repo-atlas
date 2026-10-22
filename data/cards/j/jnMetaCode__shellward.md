# jnMetaCode/shellward

⭐ 139 · TypeScript · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/jnMetaCode/shellward) · [官网](https://jnmetacode.github.io/shellward/) · 个人维护 · 中文 README

**面向中国监管的 AI Agent 安全合规网关与扫描器**

面向中国监管环境（网安法/PIPL/等保2.0/数据出境/AI标识）的 AI 应用安全工具。核心两条路径：①确定性静态扫描 `npx shellward scan`，检出境外模型端点、硬编码密钥、中文 PII、.env 暴露，输出映射法规的红黄绿评分卡与境内模型替代建议（含 OpenAI 兼容 base_url）；②运行时防护，以 MCP Server/SDK/插件形式接入 Claude Code、Cursor、LangChain 等平台，提供 8 层防御：提示注入检测（中英 37 规则）、PII 识别（含身份证/手机号/银联卡）、数据外泄链拦截、MCP 工具投毒扫描等。另提供 Agent Skill 三闸审计流程与 GitHub Action CI 门禁。零依赖、数据不出本机；声明为技术自查材料而非法律意见。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 静态扫描输出映射网安法/PIPL/等保2.0/数据出境/AI标识的评分卡，精确到文件:行
- 8 层运行时防御：注入检测、PII 识别、外泄链拦截、MCP 工具投毒与 rug-pull 检测
- 检出境外模型依赖后给出 12 家境内厂商的 OpenAI 兼容 base_url 替代表
- MCP Server / SDK / OpenClaw 插件 / GitHub Action 多种接入方式，零依赖

## 适用场景

- 一行命令体检 AI 项目是否踩数据出境、硬编码密钥、PII 暴露红线
- 在 Claude Code/Cursor 等 agent 运行时拦截提示注入与数据外泄
- 在 CI/PR 门禁中阻断密钥与境外模型依赖合并
- 让编码 agent 按三闸流程产出带取证引用的合规审计报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **AI 应用合规网关** — 为中国监管而生的 AI Agent 安全合规工具（网安法 2026 / PIPL / 等保2.0 / 数据出境 / AI标识）。先一行命令体检项目合规风险，再在运行时拦截提示注入、数据外泄与危险命令。
> L154: |**Claude Desktop**|MCP Server|Add to `claude_desktop_config.json` — 8 security tools|
> L168: - **8 defense layers**: prompt guard, input auditor, tool blocker, output scanner, security gate, outbound guard, 

## 星数曲线

```mermaid
xychart-beta
    title "jnMetaCode/shellward 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-22 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fafab36d8afb` · [字段定义](../../DATASET.md)*
