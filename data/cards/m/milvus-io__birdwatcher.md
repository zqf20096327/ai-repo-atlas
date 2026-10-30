# milvus-io/birdwatcher

⭐ 67 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/milvus-io/birdwatcher) · 组织维护

**Milvus 2.x 的调试工具：连接 etcd 检查系统状态与备份**

milvus-io 组织维护的 Milvus 2.0 及以上版本调试命令行工具。通过连接 Milvus 所依赖的 etcd（支持指定地址与 rootPath），提供查看集合等元数据、备份 etcd 键值（按 meta 前缀导出压缩文件）等检查操作，内置 help 命令列出全部命令。以 Go 编写，要求 go 1.18 或更高版本，通过克隆源码后 go install 安装；若 module 存在 replace/exclude 指令，正确方式是克隆源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 etcd 检查 Milvus 系统状态
- 支持指定远程实例 etcd 地址与自定义 rootPath
- 查看集合等元数据并按前缀备份 etcd 键值

## 适用场景

- 排查 Milvus 实例的元数据状态
- 备份 Milvus 的 etcd 数据
- 检查非默认 rootPath 的多实例部署

## 场景标签

 · 领域:向量数据库/运维工具

## 证据(README 行号)

> L5: A debug tool for Milvus 2.0 or later. This tool connects to etcd and inspects some status of the Milvus system.
> L3: linter status

## 星数曲线

```mermaid
xychart-beta
    title "milvus-io/birdwatcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-30 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2bc0bf9244f0` · [字段定义](../../DATASET.md)*
