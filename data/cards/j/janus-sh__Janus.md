# janus-sh/Janus

⭐ 6,556 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/janus-sh/Janus) · 个人维护

**终端里用免费模型的编码 agent：读码、改文件、跑命令**

以 npm 全局包分发的终端编码 agent，读取代码、编辑文件并运行 shell 命令。核心机制是免费模型路由：仓库维护免费模型排名清单（启动时下载最新副本），请求发送到当前可用的最佳免费模型，遇速率限制或中断自动切换下一个。需用户提供至少一个免费 key（OpenRouter/Gemini/Groq），并明确忽略环境中的付费 key。基于 pi 引擎构建，由 AI agent 维护发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免费模型排名清单自动更新，支持中断/限流时自动切换模型
- 默认忽略 shell 中付费 key，保证不产生费用
- janus doctor 输出诊断信息供提交 bug 报告
- 模型断流时自动重试下一个模型

## 适用场景

- 在没有付费订阅的情况下在终端完成编码任务
- 多服务免费额度拼合以增加每日可用请求数
- 单任务模式一键修复失败测试（janus -p）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: **A free coding agent in your terminal.** It reads your code, edits files and runs commands, like the paid ones. The
> L32: - Janus keeps a ranked list of free models: which ones are smartest, and which answered a ping in the last hours. T
> L34: - Each request goes to the best model on the list that you have a key for and that is awake.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e4d77ac435d1` · [字段定义](../../DATASET.md)*
