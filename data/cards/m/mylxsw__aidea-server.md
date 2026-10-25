# mylxsw/aidea-server

⭐ 1,765 · Go · 推送 2026-10-22 · [GitHub](https://github.com/mylxsw/aidea-server) · [官网](https://ai.aicode.cc) · 个人维护 · 中文 README

**AIdea 全栈 AI 应用的服务端：集成多家 LLM 与图像生成模型**

用 Golang 编写的开源应用服务端，为 AIdea 客户端 APP 提供 AI 对话、协作与图像生成（含 Stable Diffusion 文生图/图生图）的后端服务，内置多家大模型与图像生成模型的接口实现，并将所有对话模型封装为兼容 OpenAI Chat Stream 协议的统一接口，同时暴露 OpenAI 兼容 API 供第三方软件调用。附带任务队列、计费定价、支付、短信、限流、SOCKS5 代理等业务组件。支持自托管（提供 Docker 部署仓库与协助部署），从源码用 go build 构建。限制：代码注释与技术文档目前有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一抽象接口封装各家对话模型，兼容 OpenAI Chat Stream 协议
- 提供 OpenAI 兼容 API，第三方软件可直接调用
- 内置任务队列、计费定价、在线支付、限流、短信等业务组件
- 提供 Docker 部署仓库与自托管/协助部署两种方式

## 适用场景

- 自托管部署 AIdea 聊天与图像生成应用的完整后端
- 让支持 OpenAI 协议的第三方软件复用其模型接入能力
- 基于其公共包（pkg）在自己的项目中复用 AI 接口实现

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L7: A fully open-source APP server built with Golang that integrates mainstream large language models and image generati
> L43: |api|OpenAI-compatible API; endpoints here can be used directly by any third-party software that supports the OpenA
> L49: |⌞ ai|AI model interface implementations for various providers|

## 星数曲线

```mermaid
xychart-beta
    title "mylxsw/aidea-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 1764 --> 1766
    line [1765, 1765]
```

2026-10-18 1,765 → 2026-10-25 1,765（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `070523e3fdc5` · [字段定义](../../DATASET.md)*
