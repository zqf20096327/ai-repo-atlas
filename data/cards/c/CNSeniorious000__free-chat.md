# CNSeniorious000/free-chat

⭐ 195 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/CNSeniorious000/free-chat) · [官网](https://endless-chat.vercel.app) · 个人维护 · 中文 README

**基于 chatgpt-demo 分叉的 LLM 聊天 Web UI，通过环境变量配置**

Fork 自 anse-app/chatgpt-demo 的 LLM 聊天界面，提供线上站点 free-chat.asia，采用 Astro/SolidJS 技术栈。通过环境变量控制行为：OPENAI_API_KEY、自定义 API base URL 与模型 ID、HTTPS 代理、站点密码、页面注入脚本等；使用 tiktoken（cl100k_base）相关资源 URL 配置。分支包括 main（基础样式）、endless（基于 token 的消息裁剪）与 promplate-demo（演示 promplate 用法，活跃开发）。部署说明指向原仓库，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过环境变量配置 API Key、base URL、模型与代理等
- endless 分支提供基于 token 的消息列表裁剪
- 支持站点密码与 API 调用签名（PUBLIC_SECRET_KEY）

## 适用场景

- 部署一个可自定义模型与 API 端点的聊天网页
- 为自己的 API 服务搭建前端聊天界面
- 了解 promplate 库的使用方式（promplate-demo 分支）

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: Free Chat
> L5: > Forked from chatgpt-demo. Find deployment instructions in the original repository.

## 星数曲线

```mermaid
xychart-beta
    title "CNSeniorious000/free-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 194 --> 197
    line [196, 195, 195]
```

2026-10-18 196 → 2026-10-24 195（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `363f6a03da2b` · [字段定义](../../DATASET.md)*
