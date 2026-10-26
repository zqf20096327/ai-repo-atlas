# GetGoAPI/Free-GPT-API-Proxy-Gateway

⭐ 44 · HTML · 推送 2026-03-14 · [GitHub](https://github.com/GetGoAPI/Free-GPT-API-Proxy-Gateway) · [官网](https://getgoapi.com) · 组织维护 · 中文 README

**面向中国用户的 OpenAI/Claude API 转发网关服务**

由 getgoapi.com 提供的 API 中转服务：将官方 OpenAI/Claude API 域名替换为其加速域名 api.getgoapi.com/v1，自动路由到全球节点，解决国内连接超时、IP 封禁与信用卡支付问题。使用方式是在官网注册获取以 sk-getgoapi- 为前缀的 Key，并给出 Curl 等常用框架的接入示例。本质为托管商业服务，需付费/注册获取 Key，而非可自建的开源代理工具。

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

- 兼容 OpenAI 协议的 API Gateway，替换 Base URL 即可接入
- 自动路由到全球节点，解决连接超时与 Region Not Supported
- 提供 sk-getgoapi- 前缀 Key 与 Curl 接入示例

## 适用场景

- 国内开发 AI 应用时中转 OpenAI/Claude API 请求
- 无法绑定国外信用卡时通过第三方 Key 调用 API

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: > 你不需要自己购买服务器搭建反向代理。本项目提供**企业级 API 转发网关**，一行代码解决 `Connection Refused` 和 `Region Not Supported` 问题。
> L19: **getgoapi.com** 是最终解决方案。我们提供兼容 OpenAI 协议的 **API Gateway**，自动路由到全球最快的节点。

## 星数曲线

```mermaid
xychart-beta
    title "GetGoAPI/Free-GPT-API-Proxy-Gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `47e6f77d1332` · [字段定义](../../DATASET.md)*
