# devadutta/cook

⭐ 18 · TypeScript · 推送 2026-10-22 · [GitHub](https://github.com/devadutta/cook) · [官网](https://getcook.dev/) · 个人维护

**终端自然语言 AI 代理：单二进制，多 LLM 提供商可用**

以单一二进制分发的终端 AI 代理，用户用自然语言下达任务，agent 通过四个内置工具（Read/Write/Edit/Bash）循环执行；文件写入与破坏性命令默认需人工确认，支持路径限定与 dry-run。可接入 Vercel AI Gateway、OpenAI API、ChatGPT 登录（OAuth）、Anthropic、Google、Groq，一个参数切换模型。支持管道输入、.md 命令别名、多 agent 配置与跳过工具循环的 decision agent（选项/评分/是非判断）。面向在终端与脚本环境中使用 AI 执行任务的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一二进制、零运行时依赖，适配管道/脚本/cron 场景
- 6 类提供商接入与自动选择（Gateway→OpenAI→ChatGPT→Anthropic→Google→Groq）
- 四内置工具（Read/Write/Edit/Bash）加变更审批、路径限定与 dry-run 安全机制
- decision agent 输出 choice/score/boolean 判定及概率

## 适用场景

- 在终端用一句话让 AI 执行代码检索、重构、写 changelog 等任务
- 把常用提示词存为命令别名，纳入管道与脚本自动化
- 用 decision agent 对输入做选项、评分或是非判断

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11:  A portable terminal AI agent that runs tasks in natural language.
> L64: cook has four built-in tools it can use to accomplish tasks:
> L182: cook works with multiple AI providers. Sign in with ChatGPT or set the appropriate API key, and cook picks the rig

## 星数曲线

```mermaid
xychart-beta
    title "devadutta/cook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5db452a0983d` · [字段定义](../../DATASET.md)*
