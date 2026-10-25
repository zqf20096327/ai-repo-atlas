# brave-chat/brave-chat-server

⭐ 41 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/brave-chat/brave-chat-server) · [官网](https://server-wzxp.onrender.com/docs) · 组织维护

**Brave Chat 的全异步后端：实时聊天服务端**

基于 FastAPI、SQLAlchemy、Redis 的聊天应用后端，支持私聊与聊天室消息、实时文本与图片收发、联系人全文搜索、消息增删改，采用 Redis pub/sub 与 WebSocket 架构，数据存储于 SingleStoreDB（MySQL 协议），图片经 Deta drive 存储。安装依赖 Make、Python>=3.9、Poetry，需配置 SingleStore、Redis Cloud 与 Deta 账号凭据；提供 docker compose 本地运行与 Heroku 部署路径，并附带 Swagger/Redoc 文档、Prometheus 指标与 Grafana 面板。仓库标签含 chatgpt/openai-api，但可见 README 正文未展示 AI 功能细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 私聊/聊天室实时消息，基于 Redis pub/sub 与 WebSocket
- 消息与图片收发，图片经 Deta drive 存储
- SingleStoreDB 多模型关系数据库存储
- 提供 Swagger/Redoc 文档、Prometheus 指标与 Grafana 面板

## 适用场景

- 自托管一个支持聊天室的即时通讯服务
- 学习和扩展基于 FastAPI+WebSocket 的实时后端架构
- 通过 docker compose 在本地运行完整聊天平台

## 场景标签

 · 领域:通信/聊天后端

## 证据(README 行号)

> L15: A Fully Async-based backend for Brave Chat. It is a multi-model server that is fully functional and supports all th
> L379: ## Core Dependencies

## 星数曲线

```mermaid
xychart-beta
    title "brave-chat/brave-chat-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `0a622924362d` · [字段定义](../../DATASET.md)*
