# MrPeker/turbopuffer-gui

⭐ 23 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/MrPeker/turbopuffer-gui) · [官网](https://mrpeker.github.io/turbopuffer-gui/) · 个人维护

**Turbopuffer 向量数据库的第三方桌面 GUI 客户端**

基于 Electron/React/TypeScript 的非官方桌面客户端，用于管理 Turbopuffer 向量与全文搜索引擎：支持加密存储多连接 API key、浏览命名空间、文档检索与过滤、可视化 Schema 设计（向量维度/全文/属性索引）、分组聚合查询。API key 用 OS 原生 safeStorage 加密，出站请求限定 *.turbopuffer.com 等域名。README 声明为 Beta 软件，不建议用于生产数据。提供 macOS/Windows/Linux 预编译安装包，也可 npm 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 加密存储多 Turbopuffer 连接与命名空间/文档浏览
- 可视化 Schema 设计与过滤构建器、分组聚合查询
- 出站网络限制在 *.turbopuffer.com 等白名单域名
- macOS/Windows/Linux 预编译安装包

## 适用场景

- 给 Turbopuffer 实例做可视化数据浏览与查询调试
- 配置命名空间的向量维度与全文/属性索引
- 在不写代码的情况下管理多个 Turbopuffer 连接

## 场景标签

 · 领域:数据库工具/向量检索

## 证据(README 行号)

> L10:  A third-party, open-source desktop GUI client for Turbopuffer - the blazing-fast vector and full-text search engin
> L104: - **@turbopuffer/turbopuffer** - Official Turbopuffer SDK

## 星数曲线

```mermaid
xychart-beta
    title "MrPeker/turbopuffer-gui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b4f206199b50` · [字段定义](../../DATASET.md)*
