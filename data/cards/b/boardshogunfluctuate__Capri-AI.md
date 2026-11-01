# boardshogunfluctuate/Capri-AI

⭐ 287 · MIT · 推送 2026-10-30 · [GitHub](https://github.com/boardshogunfluctuate/Capri-AI) · 个人维护

**Windows 桌面 AI 代理：用自然语言指挥 Claude Code 等助手操作电脑**

面向 Windows 10+ 的桌面应用，作为代理层运行在 Claude Code、Codex、Antigravity 等 AI 助手之上：用户用自然语言描述任务，Capri 将其路由到所选引擎，引擎制定步骤后由 Capri 调用工具在本机执行文件整理、代码编写调试、项目脚手架、定时备份等操作。敏感操作需用户审批。账户与 API key 由用户自带，费用由 AI 供应商计费。以 .exe 安装包分发，macOS/Linux 版本在规划中。非官方同人项目，与 CD PROJEKT RED 等无关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引擎路由器支持 Claude Code、Codex、Antigravity，可随时切换，其他助手经自定义适配器接入
- 计划-工具调用-检查-汇报的完整代理流程，敏感操作执行前需用户审批
- 无需终端的 Windows 原生桌面应用（.exe 安装包），自带 AI 账户或 API key

## 适用场景

- 不熟悉终端的用户用自然语言整理文件、总结 PDF
- 让 AI 助手在本机查找并修复项目代码 bug
- 通过审批机制控制 AI 对本机文件的操作范围

## 场景标签

`编码 Agent` `AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L31: Under the hood, Capri is a desktop interface and agent layer on top of the AI assistants you already use. It works 
> L112: ### Supported engines
> L116: |Claude Code|✅ Supported|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8e818456b665` · [字段定义](../../DATASET.md)*
