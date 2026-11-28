# sao-coding/locus

⭐ 108 · Rust · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/sao-coding/locus) · 个人维护 · 中文 README

**面向 Windows 用户的 GPU 渲染数据库客户端**

用 Rust 与 GPUI 编写的 Windows 数据库客户端，单个 exe，支持 MySQL/MariaDB、PostgreSQL、SQLite、Redis、Oracle、SQL Server 连接。查询结果以流式虚拟化表格呈现，支持服务端取消、生产连接只读保护、定时解锁写入与审计日志、SSH 隧道、执行计划、CSV/Excel 导入与多种格式导出。仅支持 Windows 10/11 64 位，构建未经代码签名；Oracle/SQL Server 通过内置 Go 辅助程序连接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式虚拟化表格加载查询结果，支持服务端取消
- 生产连接默认只读，写入需定时解锁并记录审计日志
- 支持 SSH 隧道，密码存于 Windows Credential Manager
- Oracle/SQL Server 通过内置纯 Go 驱动辅助程序连接

## 适用场景

- 在 Windows 上管理多种关系数据库与 Redis 连接
- 对生产库执行受限写入并保留审计记录
- 导入 CSV/Excel 并导出多种格式数据

## 场景标签

 · 领域:数据库工具

## 证据(README 行号)

> L12: A database client for Windows that stays smooth. GPU-rendered, written in Rust, one small exe.
> L14: Locus talks to MySQL / MariaDB, PostgreSQL, SQLite, Redis, Oracle and SQL Server. Results stream into the
> L5:  Windows 10 and 11


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `230ee83fc222` · [字段定义](../../DATASET.md)*
