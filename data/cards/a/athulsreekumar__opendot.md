# athulsreekumar/opendot

⭐ 13 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/athulsreekumar/opendot) · [官网](https://opendot.live) · 个人维护

**本地优先的桌面多 AI 助手团队应用（Mac/Windows）**

Mac 与 Windows 桌面应用（Electron + React），提供名为 Dots 的单职责 AI 助手：每个 Dot 有自己的角色、工具权限与预算，在后台持续运行并响应邮件、日历、文件等事件；SuperDot 可跨 Dot 并行提问并汇总带引用的回答。组织模式含 13 个部门 Dot 与 28 个内置 playbook，SuperDot 制定项目计划、任务并行执行并经审查。支持云端模型（Claude/GPT/Gemini 等）或本地 Ollama/LM Studio，数据以明文 JSON 存于 ~/.opendot，发送云端前做 PII 掩码。暂无签名安装包，需从源码构建或下载 CI 产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单职责 Dot 助手 + Dot Links 权限规则（allow/ask/block、限流、审批、日志）
- SuperDot 跨 Dot 并行提问与带引用的汇总回答
- 组织模式：13 个部门 Dot、28 个内置 playbook、项目看板与交付物
- 本地优先：数据存于 ~/.opendot，云端调用前 PII 掩码，密钥由系统加密

## 适用场景

- 在本机运行一组各司其职的 AI 助手处理邮件、日程与研究
- 让 SuperDot 组织部门 Dot 团队执行并交付项目
- 在不上云的前提下用 Ollama 本地模型驱动助手

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L7: A Mac and Windows app that gives you **Dots**: AI assistants that each do one job brilliantly,
> L24: Most AI apps give you one chat that forgets everything and can't do anything on its own. OpenDot gives you a **team
> L88:  Claude, GPT, Gemini, Grok, Mistral, DeepSeek, OpenRouter, Groq, or fully local with Ollama, LM Studio, llama.cpp o


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e31821c030b1` · [字段定义](../../DATASET.md)*
