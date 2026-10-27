# yashksaini-coder/Hack-Agent-Server

⭐ 25 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/yashksaini-coder/Hack-Agent-Server) · [官网](https://hack-agent-server.onrender.com/) · 个人维护

**FastAPI 后端：提供网络搜索与股票分析 AI agent 的 REST API**

基于 FastAPI 与 Agno 构建的 REST API 后端服务器，托管于 Render。服务器负责处理前端请求，调用 Agno 构建的 AI agent 团队进行网络搜索抓取与股票价格预测/分析，暴露 /chat、/agent、/stock、/stock-analysis、/stock-news、/top-stocks 等端点，自带 Swagger 文档页面。技术栈含 Redis（缓存/消息）。本地开发使用 uv 管理依赖，可用 Docker Compose 构建运行。README 未给出 agent 具体模型配置与环境变量说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 FastAPI + Agno 的 AI agent 团队后端服务
- 提供 /stock-analysis、/stock-news、/top-stocks 等 6 个 REST 端点
- 使用 uv 管理依赖，支持 Docker Compose 构建运行
- 托管于 Render，自带 /docs API 文档页

## 适用场景

- 为前端应用提供股票分析与实时数据的 API 服务
- 搭建本地开发环境调试 AI agent 后端
- 通过 Postman 等工具测试 AI agent 接口

## 场景标签

`多智能体` `金融量化` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L7: > Main Backend server hosted on Render. It is a REST API server built using **FastAPI** and **Agno**. It is hosted o
> L9: > It also interacts with the Agno AI to get the predictions for the stock prices.

## 星数曲线

```mermaid
xychart-beta
    title "yashksaini-coder/Hack-Agent-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4c44503b2370` · [字段定义](../../DATASET.md)*
