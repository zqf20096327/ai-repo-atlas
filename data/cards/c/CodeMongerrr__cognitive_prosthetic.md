# CodeMongerrr/cognitive_prosthetic

⭐ 18 · Python · MIT · 推送 2026-07-27 · [GitHub](https://github.com/CodeMongerrr/cognitive_prosthetic) · 个人维护

**把 ChatGPT 网页版封装成本地 REST API 的工具**

通过 Playwright 浏览器自动化操作 ChatGPT 网页界面，在其上封装出 Flask REST API 服务器（/chat、/new-chat、/health、/status 等端点），使开发者可用现有 ChatGPT 账号免费获得本地 HTTP/JSON 接口，供任意语言调用。使用前需一次性运行 manual_login.py 保存浏览器会话。README 声明受网页端速率限制、需保持本机运行、可能违反 OpenAI ToS，仅限个人/教育用途，不建议生产使用。附带可选 React 测试前端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatGPT 网页界面转本地 REST API（POST /chat 等端点）
- Playwright 浏览器自动化 + 一次性会话保存脚本
- 标准 HTTP/JSON 接口，Python/JavaScript/Go 等任意语言可调用
- 附 React Web 测试界面（npm 运行）

## 适用场景

- 不付费官方 API，用现有 ChatGPT 账号本地搭建接口做原型
- 个人自动化脚本与数据分类等轻量任务
- 学习 AI 开发时降低成本实验

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L1: # ChatGPT Local API
> L9: This project converts ChatGPT's web interface into a REST API server that runs locally on your computer. Instead of 

## 星数曲线

```mermaid
xychart-beta
    title "CodeMongerrr/cognitive_prosthetic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `d88b000ee49a` · [字段定义](../../DATASET.md)*
