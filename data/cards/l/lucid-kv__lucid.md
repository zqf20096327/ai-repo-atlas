# lucid-kv/lucid

⭐ 393 · Rust · MIT · 推送 2026-04-22 · [GitHub](https://github.com/lucid-kv/lucid) · [官网](https://lucid-kv.dev) · 组织维护

**带 REST API 的分布式高性能键值存储，供后端/云原生使用**

Lucid KV 是一个通过 HTTP/REST API 访问的分布式键值存储，采用模块化配置，可按需启用持久化、加密 SSE、压缩、复制等特性。提供二进制发行版（lucid init/server 启动）与 Docker 部署两种运行方式，部署前需本地准备 lucid.yml 配置文件；另有在线演示节点、GitBook 文档与 CLI。README 声明持久化与加密功能处于开发中，Web UI 为规划功能。面向需要缓存/键值存储的开发者与运维场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 HTTP/REST API 访问的分布式键值存储
- 模块化配置：可启用持久化、加密 SSE、压缩、复制
- 提供二进制发行与 Docker 两种部署方式
- 持久化与加密为 README 声明的开发中功能

## 适用场景

- 作为后端服务的高性能键值存储或分布式缓存
- 通过 REST API 在多个服务间共享配置与状态数据
- 用 Docker 快速部署 KV 节点并按需开启复制等特性

## 场景标签

 · 领域:存储/中间件

## 证据(README 行号)

> L9: Lucid is a high performance, secure and distributed key-value store accessible through an HTTP API, that is built ar
> L5:  High performance and distributed KV store w/ REST API. 🦀

## 星数曲线

```mermaid
xychart-beta
    title "lucid-kv/lucid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 391 --> 393
    line [392, 392]
```

2026-10-18 392 → 2026-10-25 392（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `11abaa0bf673` · [字段定义](../../DATASET.md)*
