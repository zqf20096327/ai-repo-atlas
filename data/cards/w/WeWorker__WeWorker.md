# WeWorker/WeWorker

⭐ 158 · JavaScript · Apache-2.0 · 推送 2026-11-01 · [GitHub](https://github.com/WeWorker/WeWorker) · [官网](https://www.weworker.cc) · 组织维护 · 中文 README

**让 AI Agent 通过浏览器扩展实际操作网站的开源桌面应用**

面向终端用户的桌面 Agent：将自然语言任务交给 AI，通过 Chrome 扩展（Extension Adapter）或内置运行时（Toolkit Adapter）在真实浏览器中执行操作，统一经 webcli call 调用。内置 33 个网站 Adapter（QQ/163 邮箱、京东、小红书、B 站、GitHub 等），支持定时任务、站点记忆、消息通知与多模型配置（Anthropic、智谱、DeepSeek 及兼容接口）；登录、支付等关键步骤需用户确认。提供 Windows/macOS 安装包，也可从源码运行（Node.js 22.x、uv、Chrome）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 33 个网站 Adapter，覆盖邮箱、电商、社区等站点的读取与操作
- Extension 与 Toolkit 两类 Adapter 共享 webcli call 统一调用入口
- 网站探索 Agent 辅助创建、验证和维护网站工具
- 支持 Anthropic、智谱、DeepSeek 及兼容接口的多模型配置

## 适用场景

- 用自然语言跨站查询并汇总信息，如 GitHub Trending 加 Hacker News
- 自动化重复网页工作：查邮件、填表单、定时任务
- 通过编写 Adapter 扩展新站点能力供 AI 调用

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: WeWorker 将自然语言任务交给 AI Agent，通过浏览器扩展或内置 Toolkit Adapter 调用网站能力；涉及登录、提交、下单、支付等关键步骤时，仍由用户确认。
> L41: - **自然语言操作网站**：通过桌面端对话描述任务，由 AI 选择并调用网站工具。
> L47: - **多模型配置**：支持 Anthropic、智谱、DeepSeek 和兼容接口的自定义模型配置。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `d67917bacddb` · [字段定义](../../DATASET.md)*
