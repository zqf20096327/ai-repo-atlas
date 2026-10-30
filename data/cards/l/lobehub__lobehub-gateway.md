# lobehub/lobehub-gateway

⭐ 27 · Go · 推送 2026-10-14 · [GitHub](https://github.com/lobehub/lobehub-gateway) · 组织维护

**LobeHub 网关服务的 Go 自托管单实例重实现**

用 Go 重实现的 LobeHub 网关服务，面向自部署用户：提供 device-gateway（设备连接路由、状态查询、工具调用、agent-run 请求）与 agent-gateway（中继浏览器 WebSocket 会话与服务端 agent 事件），并有统一二进制同进程运行两者。状态保存在内存中，不依赖 Cloudflare Workers、Durable Objects、Redis 等外部服务；设备指标历史最多保留 48 小时，重启即丢失。不支持多实例协调、Admin API、Workspace 共享设备等能力。提供 Docker 与 Compose 运行方式及 Linux amd64/arm64 二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- device-gateway 与 agent-gateway 双网关，统一二进制单进程运行
- 无 Cloudflare 绑定与 Redis/PostgreSQL/NATS 等外部依赖，状态在内存
- 设备健康采样与 48 小时内存历史查询
- Docker/Compose 与 Linux amd64/arm64 发布产物

## 适用场景

- 在自有服务器上部署 LobeHub 网关而不使用 Cloudflare 平台
- 以 systemd/Docker/Kubernetes 等进程管理器运行单实例网关
- ARM 设备上自托管 LobeHub 设备与代理网关

## 场景标签

 · 领域:LLM 基础设施/网关

## 证据(README 行号)

> L5: `lobehub-gateway-go` is a Go reimplementation of the LobeHub gateway services. It is intended for self-hosted deploy
> L42: |`device-gateway-go`|Implemented|Device gateway for routing LobeHub device connections, status queries, tool calls,
> L43: |`agent-gateway-go`|Implemented|Agent gateway for relaying browser WebSocket sessions and server-pushed agent event

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobehub-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `faa4681e074e` · [字段定义](../../DATASET.md)*
