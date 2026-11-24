# PratikRai0101/tally

⭐ 4 · Swift · MIT · 推送 2026-11-22 · [GitHub](https://github.com/PratikRai0101/tally) · [官网](https://tally-site.vercel.app) · 个人维护

**macOS 菜单栏应用：汇总 AI 编码订阅的额度、重置与花费**

读取 Claude Code、Codex、Pi、OpenCode、Grok CLI、Antigravity、Gemini CLI 等工具已写入的本地会话日志，并调用各家已登录的用量端点，把多个订阅计划的额度剩余、重置倒计时、pace 预测和按 API 价折算的计划价值集中显示在菜单栏。提供 80%/95% 告警、可自定义 hook 脚本、按模型/项目的花费统计和 Wrapped 分享卡片。无账号、无服务器、不上传数据；依赖至少一个已登录的 CLI；应用未经 Apple 公证。

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

- 每个订阅计划一个菜单栏计量条，含 % 用量、重置倒计时与 pace 预测
- 读取各 CLI 已有的本地日志与登录凭据对应的使用端点，无需额外配置
- 按模型/项目的花费统计与 API 价对比的计划价值计算
- 告警触发时可运行用户自定义 hook 脚本

## 适用场景

- 同时使用多个 AI 编码订阅时统一查看剩余额度
- 在额度用尽前收到告警并自动提交工作区代码
- 查看各模型和项目的实际花费与订阅价值

## 场景标签

 · 领域:开发者工具/AI 订阅用量监控

## 证据(README 行号)

> L7:  A native macOS menu bar app for Claude, Codex, Cursor, Grok, Gemini, and OpenCode.
> L48: Tally reads the session logs your agents already write and the usage endpoints your CLIs already sign in to, and pu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `34d8819bbcde` · [字段定义](../../DATASET.md)*
