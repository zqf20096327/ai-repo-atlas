# tigusigalpa/manus-ai-go

⭐ 23 · Go · MIT · 推送 2026-10-04 · [GitHub](https://github.com/tigusigalpa/manus-ai-go) · 个人维护 · 中文 README

**面向 Manus API v2 的 Go 语言社区 SDK**

独立社区维护的 Manus API v2 Go 客户端库，以惯用 Go 代码封装任务的创建、查询、更新、停止与删除，支持任务消息读取与追问、文件上传槽位与附件管理（FileID/URL/Base64/本地路径）、webhook 注册与载荷解析，以及项目、技能、agent、用量与网站发布等方法。可配置 base URL、HTTP 客户端与超时，支持 API key 与 Bearer Token 两种认证；错误类型可用 errors.As 检查。行为受 Manus API 控制，升级需参照官方文档。

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

- 覆盖任务、文件、webhook、项目、用量、网站等 API 方法
- 附件四类来源 helper（FileID/URL/Base64/FilePath）与上传流
- API key 与 OAuth Bearer Token 双认证方式
- 响应时间戳兼容数字/字符串/RFC3339 并统一为 Unix 毫秒

## 适用场景

- 在 Go 应用中创建并管理 Manus 自动化任务
- 通过 webhook 接收任务事件代替轮询
- 将本地或远程文件作为附件上传给 Manus 任务

## 场景标签

 · 领域:AI 应用开发/SDK

## 证据(README 行号)

> L21: A small, idiomatic Go client for the Manus API v2. It helps an application create and manage Manus tasks, continue 
> L25: > This is an independent community SDK. Manus API behaviour, available agent profiles, and accepted option values a

## 星数曲线

```mermaid
xychart-beta
    title "tigusigalpa/manus-ai-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `aeae16ad54e7` · [字段定义](../../DATASET.md)*
