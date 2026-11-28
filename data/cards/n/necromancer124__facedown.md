# necromancer124/facedown

⭐ 3 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/necromancer124/facedown) · 个人维护

**AI 代理可用不可读的密钥保管库：按名使用但看不到值**

facedown 将项目密钥存入加密的 `.env.facedown` 文件（AES-256-GCM，解锁密钥在用户主目录且绑定 Windows 账户）：AI 代理通过 MCP server 或 CLI 按名称读取密钥用途与允许站点，真实值只进入程序环境变量或白名单站点请求，日志中以 `***KEY_NAME***` 形式脱敏。提供 `run --keys` 按需注入、实验性 `--proxy` 模式（程序只拿占位符）、导出/导入迁移与使用日志。仅支持 Windows（Linux/macOS 计划中），需 Node 20+，声明不防御蓄意窃取密钥的程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP server + CLI + Claude Code 插件三种使用形态
- 密钥值 AES-256-GCM 加密，解锁密钥绑定用户 Windows 账户
- 站点白名单与限时授权，改动需用户窗口确认
- 输出自动脱敏与 `--proxy` 占位符模式

## 适用场景

- AI 编码代理需要调用 API 时避免密钥进入聊天记录
- 把明文 `.env` 中的密钥迁移到加密保管库
- 允许程序调用指定站点时控制密钥去向并留存审计日志

## 场景标签

 · 领域:开发者工具/安全

## 证据(README 行号)

> L16: **facedown** is a `.env` file the AI can **use** but never **read**. It sees
> L42:  The AI asks to use GITHUB_TOKEN. facedown gives the real value to your program or to an allowed API, blocks other 
> L71: **Claude Code** (the MCP server plus five slash commands, in every project).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `699ff9304fe6` · [字段定义](../../DATASET.md)*
