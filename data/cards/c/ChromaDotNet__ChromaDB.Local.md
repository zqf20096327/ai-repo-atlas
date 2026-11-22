# ChromaDotNet/ChromaDB.Local

⭐ 3 · C# · MIT · 推送 2026-11-17 · [GitHub](https://github.com/ChromaDotNet/ChromaDB.Local) · 个人维护

**.NET 库：在 Windows/Linux/macOS 上免 Docker 启动本地 Chroma 向量库**

为 ChromaDotNet.Client 提供 .NET 本地服务器管理能力：ChromaLocalServer.StartAsync 将 Chroma（或 VecturaDB）引擎作为子进程启动在 127.0.0.1，等待心跳就绪，Dispose 或应用结束时停止。引擎可执行文件随 NuGet 运行时包分发或首次启动时从 GitHub release 下载并做 SHA-256 校验，支持 SHA256SUMS 与 Sigstore 签名。需要 .NET 8 及以上（或 Windows 上的 .NET Framework 4.8，经 netstandard2.0）。项目为独立社区项目，与 Chroma Inc. 无隶属关系，包仍为 prerelease。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 免 Docker、免 Python 在 127.0.0.1 启动 Chroma 子进程服务器
- 两个可互换引擎：Chroma 1.5.9 与兼容 Chroma API 的 VecturaDB
- 可执行文件哈希校验，release 附 Sigstore 签名与构建溯源
- 支持 5 个平台运行时包，兼容 trimming 与 NativeAOT

## 适用场景

- 在 .NET 应用中进程内嵌入 Chroma 向量库而无需运维容器
- 让单元测试或示例以临时数据目录启动/停止向量库服务器
- 通过同一个库切换 Chroma 与 VecturaDB 引擎

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L8: ChromaDotNet.Client. `ChromaLocalServer.StartAsync` starts the server of an
> L11: ChromaDotNet is an independent community project that provides .NET libraries and tools for Chroma. Independent pro

## 星数曲线

```mermaid
xychart-beta
    title "ChromaDotNet/ChromaDB.Local 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-22 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `3ed70aebc7c7` · [字段定义](../../DATASET.md)*
