# nebius/gosdk

⭐ 16 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/nebius/gosdk) · [官网](https://nebius.com) · 组织维护

**Nebius AI Cloud 的 Go 客户端 SDK：管理云资源与鉴权**

Nebius AI Cloud 官方 Go SDK，基于 gRPC 封装 nebius.com 全部 API，供开发者在 Go 项目中管理云资源、鉴权与服务通信。提供 IAM Token 与服务账号（JWT 换取并后台刷新 token）两种鉴权方式，支持 Create/Get/Update/List/Filter/Delete 等资源操作，变更加 Operation 对象并用 Wait 轮询完成。最低要求 Go 1.24，通过 go get 安装，MIT 许可。IAM Token 需手动刷新，官方推荐服务账号方式用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 gRPC 支持 Nebius API 仓库定义的全部 API
- 服务账号鉴权：JWT 换取 IAM token 并后台自动刷新
- 资源 CRUD 操作配合 Operation 的 Wait 轮询机制
- Filter 方法跨分页迭代资源列表

## 适用场景

- 在 Go 服务中以服务账号身份自动化管理 Nebius 云资源
- 通过 SDK 编写资源创建、查询与删除的工具脚本
- 服务端集成需要自动刷新凭证的生产场景

## 场景标签

 · 领域:云基础设施/AI 云服务

## 证据(README 行号)

> L3: The Nebius AI Cloud SDK for Go is a comprehensive client library for interacting with nebius.com services.
> L4: Built on gRPC, it supports all APIs defined in the Nebius API repository.

## 星数曲线

```mermaid
xychart-beta
    title "nebius/gosdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a4b7fc44cdb6` · [字段定义](../../DATASET.md)*
